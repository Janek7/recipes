import os
import logging
from typing import Dict, Tuple, List
import unicodedata
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import json
import shutil
import glob

import pandas as pd
import yaml
import instaloader

from database_engine import SessionLocal, insert_recipe_from_dataframe, truncate_tables, Recipe, Tag, Resource


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SOURCE_BOOKS = [
    "Italienische Feierabendküche",
    "Emmi kocht einfach",
    "Emmi kocht einfach: 75 vegetarische Rezepte",
    "Emmi kocht einfach: 85 Rezepte für das ganze Jahr",
    "The Taste of GBS CEE"
]

SOURCE_INTERNET = "Internet"
SOURCE_INSTAGRAM = "Instagram"
SOURCE_COOKBOOK = "Kochbuch"
SOURCE_KPTNCOOK = "KptnCook"
SOURCE_FAMILY = "Familien Rezept"

COOK_BOOK_URL = "https://drive.google.com/file/d/1OTIuJo0opKTimU0gug9hlcpmTNJdstUg/view"

time_icon_element = '''<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-clock" width="17" height="17" viewBox="0 0 22 22" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z"></path>
  <circle cx="12" cy="12" r="9"></circle>
  <polyline points="12 7 12 12 15 15"></polyline>
</svg>'''


def transfer_recipes_to_database(recipes: pd.DataFrame) -> None:
    """
    iterate over dataframe and insert every recipe and related data into the database
    """
    logging.info("start inserting all recipes to database")
    recipes = recipes[recipes['Recipe'].notnull()]

    truncate_tables(tables=[Recipe, Tag, Resource])
    session = SessionLocal()

    for idx, row in recipes.iterrows():
        print(f"{idx + 1}. Process {row['Recipe']}".center(100, '-') + "\n")
        insert_recipe_from_dataframe(session, idx, row)
    session.close()
    logging.info("successfully inserted all recipes to the database")


def process_recipes(recipes: pd.DataFrame) -> None:
    """
    iterate over df and process single recipes
    outputs recipes into posts and injects into proposal scripts and page
    """
    recipes = recipes[recipes['Recipe'].notnull()]

    # 1) delete current folders to avoid "orphan" recipes (renamed in excel, old ones stay)
    delete_recipes()

    # 2) prepare data, copy images and generate posts
    recipes_data = []
    for idx, row in recipes.iterrows():
        print(f"{idx + 1}. Process {row['Recipe']}".center(100, '-') + "\n")
        recipe_data, markdown_text = format_recipe_data(row)
        recipes_data.append(recipe_data)
        # generate folder and post
        post_folder = generate_recipe_post(recipe_data, markdown_text)
        # copy image (and resize?)
        copy_image(row, post_folder)

    # 2) inject data into into web files
    inject_recipes_into_proposal_js(recipes_data)
    inject_categories_into_search_html(recipes_data)


def format_recipe_data(recipe_row: pd.Series) -> Tuple[Dict, str]:
    """
    prepares recipe data
    """
    # 1) meta data dict for yaml info header
    recipe_dict = {
        'title': recipe_row['Recipe'],
        # 'description': recipe_row['Description'], # sub title
        'slug': clean_name(recipe_row['Recipe']),
        'date': recipe_row['Date'].strftime('%Y-%m-%d %H:%M:%S'),
        'categories': [recipe_row['Category']],
        'tags': [recipe_row['Source']] + ["Top"] if pd.notna(recipe_row['Top']) else []
    }

    # assume the image is copied into the folder as well
    if pd.notna(recipe_row['Image 1']):
        recipe_dict["image"] = recipe_row['Image 1']

    # 2) text in markdown format

    # 2a) description
    if recipe_row['Description'] is not None:
        desc_formatted = recipe_row['Description'] if pd.notna(recipe_row['Description']) else None

    # 2b) time
    time_formatted = None
    time_formatted_simple = None
    if pd.notna(recipe_row['Time']):
        time = f"Die Zubereitung dauert ca. {int(recipe_row['Time'])} Minuten." if pd.notna(recipe_row['Time']) else None
        time_formatted = f"{time_icon_element} {time}"
        time_formatted_simple = time
    
    # 2c) source
    source = None
    source_simple = None

    # - cookbook recipe
    if recipe_row['Source'] in SOURCE_BOOKS:
        source_simple = f"Im Kochbuch '{recipe_row['Source']}'."
        if pd.notna(recipe_row['Source Link']):
            source = f"Im Kochbuch '{recipe_row['Source']}' auf Seite {recipe_row['Source Link']}."
        else:
            source = source_simple

    
    # - PDF cookbook recipe
    elif recipe_row['Source'] == SOURCE_COOKBOOK:
        source_simple = f"In unserem Kochbuch von 2021."
        if pd.notna(recipe_row['Source Link']):
            source = f"In unserem [Kochbuch]({COOK_BOOK_URL}) von 2021 auf Seite {recipe_row['Source Link']}."
        else:
            source = f"In unserem [Kochbuch]({COOK_BOOK_URL}) von 2021."
    
    # - Internet recipe
    elif recipe_row['Source'] == SOURCE_INTERNET:
        source_simple = "Im Internet."
        if pd.notna(recipe_row['Source Link']):
            page_domain = extract_domain(recipe_row['Source Link'])
            page_title = get_page_title(recipe_row['Source Link'])
            page_text = page_domain + f" > '{page_title}'" if page_title else ''
            source = f"Im Internet unter [{page_text}]({recipe_row['Source Link']})."
        else:
            source = source_simple
    
    # - Instagram recipe
    elif recipe_row['Source'] == SOURCE_INSTAGRAM:
        source_simple = "Auf Instagram."
        if pd.notna(recipe_row['Source Link']):
            instagram_user = get_instagram_username(recipe_row['Source Link'])
            source = f"Auf Instagram bei [{instagram_user}]({recipe_row['Source Link']})."
        else: 
            source = source_simple

    # - KptnCook
    elif recipe_row['Source'] == SOURCE_KPTNCOOK:
        source_simple = "In der KptnCook App."
        if pd.notna(recipe_row['Source Link']):
            page_domain = extract_domain(recipe_row['Source Link'])
            page_title = get_page_title(recipe_row['Source Link'])
            page_text = page_domain + f" > '{page_title}'" if page_title else ''
            source = f"In der KptnCook App: [{page_text}]({recipe_row['Source Link']})."
        else:
            source = source_simple
    
    # - Family recipe
    elif recipe_row['Source'] == SOURCE_INSTAGRAM:
        source = "Das ist ein Familienrezept."
        source_simple = source
    
    else: 
        source = recipe_row['Source']
        source_simple = source

    soure_formatted = f"> Wo gefunden? {source}"
    source_simple_formatted = f"Wo gefunden? {source_simple}"

    # 2d) additional fotos
    fotos_formatted = ""
    if pd.notna(recipe_row['Image 2']):
        fotos_formatted += f"![Foto 1]({recipe_row['Image 2']})"
    if pd.notna(recipe_row['Image 3']):
        fotos_formatted += f" ![Foto 2]({recipe_row['Image 3']})"
    
    # 2e) combined
    text_markdown = ""
    if desc_formatted: text_markdown += "\n" + desc_formatted + "\n"
    if time_formatted: text_markdown += "\n" + time_formatted + "\n"
    if fotos_formatted: text_markdown += "\n" + fotos_formatted + "\n"
    if soure_formatted: text_markdown += "\n" + soure_formatted + "\n"
    text_markdown += "\nGuten Appetit! :)"

    recipe_dict['preview'] = f"{desc_formatted + ' ' if desc_formatted else ''}{time_formatted_simple + ' ' if time_formatted_simple else ''}{source_simple_formatted} Guten Appetit! :)"

    return recipe_dict, text_markdown


def delete_recipes():
    """ delete all current recipes from the folders"""
    posts_folder = "content\\post\\*"
    folders = glob.glob(posts_folder)
    print(f"Info: delete {len(folders)} recipe post folders")
    for f in folders:
        shutil.rmtree(f)


def generate_recipe_post(recipe_data: Dict, markdown_text: str) -> str:
    # 1) prepare file and folder names
    post_folder = f"content\\post\\{recipe_data['slug']}"
    post_index_file = f"{post_folder}\\index.md"

    # 2) prepare string to write
    recipe_data = recipe_data.copy()
    print(recipe_data)
    recipe_data.pop("preview")  # not necessary for post
    print(yaml.dump(recipe_data, indent=4))
    file_content = "---\n" + yaml.dump(recipe_data, indent=4) + "---\n\n" + markdown_text
    # print(file_content)

    # 3) write to file
    os.makedirs(post_folder, exist_ok=True)
    with open(post_index_file, 'w', encoding='utf-8') as file:
        file.write(file_content)
    

    return post_folder


IMAGE_FOLDER = "G:\\Meine Ablage\\Privat\\Kochbuch\\Website\\Converted"


def copy_image(recipe_row: pd.Series, post_folder: str) -> None:
    """
    copy images from source folder into post folders
    """
    for image_keys in ["Image 1", "Image 2", "Image 3"]:
        if pd.notna(recipe_row[image_keys]):
            source_file = f"{IMAGE_FOLDER}\\{recipe_row[image_keys]}"
            destination_file = f"{post_folder}\\{recipe_row[image_keys]}"
            try:
                shutil.copy(source_file, destination_file)
            except FileNotFoundError:
                warning_text = f"WARNING: file not found -> {recipe_row[image_keys]}"
                # raise ValueError(warning_text)
                print(warning_text)
            print(f"copied file {recipe_row[image_keys]}")

    
def inject_recipes_into_proposal_js(recipes_data: List[Dict]) -> None:
    """
    reads the proposal_template.js script, injects full recipe data and writes back to proposal.js
    """
    # prepare data in correct list/dict format
    recipes_data_js = [{
        'slug': r['slug'], 
        'title': r['title'], 
        'category': r['categories'][0] if pd.notna(r['categories'][0]) else None,
        'preview': r['preview']
    } for r in recipes_data]
    recipes_data_js_string = json.dumps(recipes_data_js, indent=4)

    # read template (proposal_template.js)
    with open('assets\js\proposal_template.js', 'r') as file:
        proposal_script = file.read()

    # inject data
    proposal_script = proposal_script.replace("const recipesData = [];", f"const recipesData = {recipes_data_js_string};")

    # write to used script (proposal.js)
    with open('assets\js\proposal.js', 'w') as file:
        file.write(proposal_script)


def inject_categories_into_search_html(recipes_data: List[Dict]) -> None:
    """
    reads the search_template.html file, injects full category data and writes back to search.html
    """
    # prepare data in correct list/dict format
    categories = [r['categories'] for r in recipes_data]
    # flatten, unique and sort
    categories = sorted(list(set([item for sublist in categories for item in sublist if pd.notna(item)])))
    # create dropdown options
    category_options = "".join([f'<option value="{category}">{category}</option>\n' for category in categories])

    # read template (search_template.html)
    with open('layouts\page\search_template.html', 'r', encoding='utf-8') as file:
        search_html = file.read()

    # inject data
    search_html = search_html.replace('<option value="Placeholder">Placeholder</option>', category_options)

    # write to used script (search.html)
    with open('layouts\page\search.html', 'w',encoding='utf-8') as file:
        file.write(search_html)


def clean_name(recipe_name: str) -> str:
    # replace characters as š with s
    removed_special_chars = ''.join([char for char in unicodedata.normalize('NFD', recipe_name) if not unicodedata.combining(char)])
    # remove other special characters as ,
    removed_special_chars = re.sub(r'[^A-Za-z0-9\s]', '', removed_special_chars)
    # replace spaces with -
    removed_special_chars = removed_special_chars.lower().replace(" ", "-")

    return removed_special_chars


def get_page_title(url: str) -> str:
    """
    Get the html title of a page
    """
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the title tag and get its content
    title_tag = soup.find('title')
    
    if title_tag:
        return title_tag.get_text()  # Return the page title
    else:
        return None


def extract_domain(url):
    """
    Extract the domain of a given url
    """
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the domain (hostname) from the parsed URL
    domain = parsed_url.netloc
    
    return domain
    

instagram_loader = instaloader.Instaloader()


def get_instagram_username(url: str) -> str:
    """
    get the user name of an instagram account
    """
    # Extract the short code from the reel or post URL
    # The short code is the unique identifier for each post or reel
    short_code = url.split("/")[4]
    
    # Download the post using the short code
    post = instaloader.Post.from_shortcode(instagram_loader.context, short_code)
    
    # Get the username of the user who posted the reel
    username = post.owner_username
    
    return username


if __name__ == '__main__':

    df = pd.read_excel("G:\\Meine Ablage\\Recipes.xlsx")
    # df = pd.read_excel("Recipes.xlsx", engine='openpyxl')
    
    process_recipes(recipes=df)
    
    # transfer_recipes_to_database(recipes=df)
