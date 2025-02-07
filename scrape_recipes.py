import requests
from typing import Tuple, List
import logging
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import instaloader

from database_engine import SessionLocal, Recipe, Image

# Configure logging
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)


def ScrapeException(Exception):
    pass


# SCRAPING WEBSITES

def scrape_website(url: str) -> Tuple[str, str, str]:
    """
    scrapes the title, the whole textual content and the structured textual 
    content (lists and tables) of a given url
    """
    # Step 1: Send a request to the website and fetch the content
    response = requests.get(url)

    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found - ignore the title'

        # A) FULL TEXT
        content_free_text = soup.get_text()

        # B): all structure elements where are usually important infos listed
        ul_elements = soup.find_all('ul')
        ol_elements = soup.find_all('ol')
        table_elements = soup.find_all('table')

        content_structured = ""        
        # Extract all sub elements from the lists
        for element_list, sub_element_key in [(ul_elements, 'li'), (ol_elements, 'li'), (table_elements, 'tl')]:
            for element in element_list:
                content_structured += "\n".join([sub_element.get_text() for sub_element in element.find_all(sub_element_key)]) + "\n"
        

        # clean up the text (e.g., remove extra whitespace)
        content_free_text = ' '.join(content_free_text.split())
        content_structured = " ".join(content_structured.strip().split())

        return title, content_free_text, content_structured

    else:
        raise ScrapeException(f"Failed to retrieve the webpage. Status code: {response.status_code}")


def extract_domain(url):
    """
    Extract the domain of a given url
    """
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the domain (hostname) from the parsed URL
    domain = parsed_url.netloc
    
    return domain


def scrape_all_websites(recipes: List[Recipe], session) -> None:
    """
    scrape website content for all recipe with an URL as source excluding Instagram
    """
    # filter for recipes with website as source
    recipes = [r for r in recipes if r.source_link is not None and "http" in r.source_link and r.source != "Instagram"]
    
    for idx, recipe in enumerate(recipes):
        logging.info(f"Scrape recipe {idx}: {str(recipe)}")

        # extract content
        try:
            title, content_structured, content_freetext = scrape_website(recipe.source_link)
            domain = extract_domain(recipe.source_link)

            # update object
            Recipe.update(session, recipe.recipe_id, **{
                "web_domain": domain,
                "web_title": title,
                "content_structured": content_structured,
                "content_freetext": content_freetext,
            })
        except Exception as e:
            logging.warning(e)


# SCRAPING INSTAGRAM
instagram_loader = instaloader.Instaloader()


def scrape_instagram_post(url: str) -> Tuple[str, str, str, str]:
    """
    get the user name and meta data of an instagram post or reel
    """
    # Extract the short code from the reel or post URL
    # The short code is the unique identifier for each post or reel
    short_code = url.split("/")[4]
    
    # Download the post using the short code
    post = instaloader.Post.from_shortcode(instagram_loader.context, short_code)
    
    # Get the username of the user who posted the reel
    username = post.owner_username
    # Get content info
    caption = post.caption
    video_url = post.video_url
    
    return username, caption, video_url


def scrape_all_instagram_posts(recipes: List[Recipe], session) -> None:
    """
    scrape instagram account names and descriptions
    """
    # filter for recipes with website as source
    recipes = [r for r in recipes if r.source_link is not None and "http" in r.source_link and r.source == "Instagram"]
    
    for idx, recipe in enumerate(recipes):
        logging.info(f"Scrape instagram recipe {idx}: {str(recipe)}")
        username, caption, video_url = scrape_instagram_post(recipe.source_link)

        # update Recipe object and create Resource object
        video_resource = Image(
            recipe=recipe, 
            file_name=video_url,
            image_number=1)        
        recipe.images.append(video_resource)
        
        # update include previously set image update
        Recipe.update(session, recipe.recipe_id, **{
            "instagram_account_name": username,
            "content_freetext": caption,
        })


# MAIN METHOD


def main() -> None:
    """
    invoke scraper methods with all recipes
    """
    session = SessionLocal()
    recipes = Recipe.get_all(session)
    
    # scrape_all_websites(recipes, session)
    scrape_all_instagram_posts(recipes, session)

    session.close()


if __name__ == '__main__':
    main()

    # scrape_website(url="https://www.deepl.com/de/translator")

    # example with lists
    # scrape_website("https://sweetandhealthy.de/overnight-oats-mit-quark/")
    
    # example with tables
    # scrape_website("https://www.chefkoch.de/rezepte/3181731473597718/Superfood-Fruehstuecksbrot-mit-Avocado-und-Ei.html")