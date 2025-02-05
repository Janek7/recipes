import requests

from bs4 import BeautifulSoup


def scrape_website(url: str) -> str:
    # Step 1: Send a request to the website and fetch the content
    response = requests.get(url)

    # Step 2: Check if the request was successful
    if response.status_code == 200:
        # Step 3: Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title found - ignore the title'
        print(title)
        # print(soup.prettify()) # print html

        # A) FULL TEXT
        if False:
            # Step 4: Extract the text from the parsed HTML
            text = soup.get_text()
            print(text)

            # Step 5: Optionally clean up the text (e.g., remove extra whitespace)
            cleaned_text = ' '.join(text.split())

            # Step 6: Print the extracted text (or use it however you need)
            # print(cleaned_text)

        # B): all structure elements where are usually important infos listed
        if True:
            # Step 4: Find all <ul> (unordered list) and <ol> (ordered list) elements
            ul_elements = soup.find_all('ul')
            ol_elements = soup.find_all('ol')
            table_elements = soup.find_all('table')

            # Step 5: Extract text from the list elements
            list_text = ""
            
            # Extract text from <ul> elements
            for ul in ul_elements:
                list_text += "\n".join([li.get_text() for li in ul.find_all('li')]) + "\n"
            
            # Extract text from <ol> elements
            for ol in ol_elements:
                list_text += "\n".join([li.get_text() for li in ol.find_all('li')]) + "\n"

            # Extract text from <ol> elements
            for table in table_elements:
                list_text += "\n".join([tr.get_text() for tr in table.find_all('tr')]) + "\n"
            
            # Step 6: Print the extracted list items as a string
            print(" ".join(list_text.strip().split()))

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


if __name__ == '__main__':
    # scrape_website(url="https://www.deepl.com/de/translator")

    # example with lists
    # scrape_website("https://sweetandhealthy.de/overnight-oats-mit-quark/")
    
    # example with tables
    scrape_website("https://www.chefkoch.de/rezepte/3181731473597718/Superfood-Fruehstuecksbrot-mit-Avocado-und-Ei.html")