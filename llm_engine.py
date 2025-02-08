from typing import List, Tuple, Dict
import logging
import json

from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompt_values import PromptValue

from utils import config, read_file
from database_engine import SessionLocal, Recipe, Instruction, Ingredient


logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')


def llm_invoke(prompt: PromptValue) -> str:
    """
    invoke llm with given prompt and return answer
    """
    # Step 1: Initialize Hugging Face API with a Model Endpoint
    client = InferenceClient(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
        token=config["api_key"]
    )

    # Step 2: Invoke LLM using the formatted prompt
    response = client.text_generation(prompt)

    # Step 3: process Response
    return response


def llm_test():
    prompt = ChatPromptTemplate.from_template("You are an AI. Answer this: {question}")

    # Format the prompt
    formatted_prompt = prompt.format(question="What is the capital of CZ?")
    
    response = llm_invoke(formatted_prompt)
    print(response)


def process_all_recipes(extraction_modes: List[str] = ["content_structured", "content_freetext"]) -> None:
    """
    reads all recipes with scraped content from database and run against prompt
    extraction_modes defines which scraping/content extraction type should be analyzed with the prompt
    """
    session = SessionLocal()

    # get all recipes and filter for scraped contents
    recipes = Recipe.get_all(session)
    recipes = [r for r in recipes if r.content_structured is not None or r.content_freetext is not None]
    logging.info(f"Start prompt extraction of {len(recipes)} recipes that have scraped content available.")

    # try all given extraction_modes
    for extraction_mode in extraction_modes:
        for idx, recipe in enumerate(recipes[:2]):
            logging.info(f"Prompt recipe {idx} ('{recipe.title}') with extraction mode '{extraction_mode}'")
            try:
                prompt_response_dict = prompt_recipe(recipe, extraction_mode)
                logging.info(prompt_response_dict)
                ingredients, instructions = create_object_lists(prompt_response_dict, recipe, extraction_mode)
                logging.info(f"Write {len(ingredients)} ingredients and {len(instructions)} to the database")
                update_recipe_in_database(session, recipe, ingredients, instructions)
            except HfHubHTTPError as e:
                logging.warning(f"Model was too busy - skipped prompt for '{recipe.title}' with extraction mode '{extraction_mode}'")

    session.close()


def prompt_recipe(recipe: Recipe, content_attr: str) -> Dict:
    """
    extract ingredients and instructions from a given scraped recipe
    the title may be helpful to get the model focussed
    content_attr: flag if the freetext or structured content should be used for analysis
    """
    prompt_template_text = read_file("prompts\\extract_recipe_info.txt")
    prompt = ChatPromptTemplate.from_template(template=prompt_template_text)

    # Format the prompt
    formatted_prompt = prompt.format(
        title=recipe.title,
        recipe=getattr(recipe, content_attr)
    )
    
    # call model and process output
    response = llm_invoke(formatted_prompt)
    # limit to json dict
    response_cleaned = "{" + response.split("{", 1)[1]
    logging.info(f"LLM response dict for {recipe.title}: \n {response_cleaned}")

    # return parsed dictionary
    return json.loads(response_cleaned)


def create_object_lists(prompt_response_dict: Dict, recipe: Recipe, extraction_mode: str) -> Tuple[List[Ingredient], List[Instruction]]:
    """
    creates a list of Ingredient and Instruction objects from the prompts response dict
    """
    ingredients = [Ingredient(
        recipe=recipe,
        name=ingredient["name"],
        quantity=ingredient["quantity"],
        extraction_mode=extraction_mode
    ) for ingredient in prompt_response_dict["ingredients"]]

    instructions = [Instruction(
        recipe=recipe,
        text=ingredient["instruction"],
        order_number=ingredient["order_number"],
        extraction_mode=extraction_mode
    ) for ingredient in prompt_response_dict["instructions"]]

    return ingredients, instructions

def update_recipe_in_database(session, recipe: Recipe, ingredients: List[Ingredient], instructions: List[Instruction]) -> None:
    """
    updates the recipe object with extracted ingredients and instructions in the database
    """
    recipe.ingredients.extend(ingredients)
    recipe.instructions.extend(instructions)
    Recipe.update(session, recipe.recipe_id)


if __name__ == '__main__':
#     scraped_recipe_title = "Superfood-Frühstücksbrot mit Avocado und Ei von Wiktorija| Chefkoch"
#     scraped_recipe = """
#     PLUSDeine Plus InhalteUnsere PLUS ProfileRezepte des MonatsRezepte aus MagazinenMehr über PLUS erfahren1 Monat kostenlos testen Unsere PLUS Profile Rezepte 
# des Monats Rezepte aus Magazinen RezepteEmpfehlungenWas koche ich heute?Was backe ich heute?RezeptsammlungenRezeptempfehlungenDas Perfekte DinnerAlle RezepteRezepte findenBeliebte Rezepte heuteRezepte – schnell und einfachUnsere PLUS RezepteNeue RezepteMarkenrezepte Was koche ich heute? Was backe ich heute? Rezeptsammlungen Rezeptempfehlungen Das Perfekte Dinner Beliebte Rezepte heute Rezepte – schnell und einfach Unsere PLUS Rezepte Neue Rezepte MagazinÜbersichtAlltagskücheWintergerichteVegetarisch & VeganLänderkücheBackenLow Carb & ErnährungÜber den TellerrandUnsere Top-RezepteMagazin ÜbersichtAktuellesPunkt 12 unter SternenDas perfekte DinnerUnsere Produkt-LieblingeKüchengeräte im VergleichDie NFL bei ChefkochNachhaltigkeit in der KücheDie Redaktion empfiehltChefkoch trifft Fackelmann Alltagsküche Wintergerichte Vegetarisch & Vegan Länderküche Backen Low Carb & Ernährung Über den Tellerrand Unsere Top-Rezepte Punkt 12 unter Sternen Das perfekte Dinner Unsere Produkt-Lieblinge Küchengeräte im Vergleich Die NFL bei Chefkoch Nachhaltigkeit in der Küche Chefkoch trifft Fackelmann VideosVideosShared TableProbier was Neues!Mit Chefkoch um die WeltLieblingsrezepteEinfach leckerRikes BackschuleFabios KochschuleHack'n'RollBrot backenVideo ÜbersichtSchwäbische LinsenEinfache Low-Carb-PizzaTexas Chili Shared Table Probier was Neues! Mit Chefkoch um die Welt Lieblingsrezepte Einfach lecker Rikes Backschule Fabios Kochschule Hack'n'Roll Brot backen Schwäbische Linsen Einfache Low-Carb-Pizza Texas Chili CommunityCommunityAktuelle BeiträgeKochenPlaudereckeBackenLifestyleSonstige KochthemenAlle ForenAlle Gruppen Aktuelle Beiträge Kochen Plauderecke Backen Lifestyle Sonstige Kochthemen Unsere PLUS Profile Rezepte des Monats Rezepte aus Magazinen Was koche ich heute? Was backe ich heute? Rezeptsammlungen Rezeptempfehlungen Das Perfekte Dinner Beliebte Rezepte heute Rezepte – schnell und einfach Unsere PLUS Rezepte Neue Rezepte Alltagsküche Wintergerichte Vegetarisch & Vegan Länderküche Backen Low Carb & Ernährung Über den Tellerrand Unsere Top-Rezepte Punkt 12 unter Sternen Das perfekte Dinner Unsere Produkt-Lieblinge Küchengeräte im Vergleich Die NFL bei Chefkoch Nachhaltigkeit in der Küche Chefkoch trifft Fackelmann Shared Table Probier was Neues! Mit Chefkoch um die Welt Lieblingsrezepte Einfach lecker Rikes Backschule Fabios Kochschule Hack'n'Roll Brot backen Schwäbische Linsen Einfache Low-Carb-Pizza Texas Chili Aktuelle Beiträge Kochen Plauderecke Backen Lifestyle Sonstige Kochthemen Presse Jobs Impressum AGB Meldung rechtswidrige Inhalte Verträge hier kündigen Datenschutz Datenschutz-Einstellungen Werben Sie bei uns Nutzungsbasierte Online Werbung Rezepte finden Was koche ich heute Was backe ich heute Magazin Übersicht Foren Videos Übersicht Zum Newsletter anmelden FAQ 
# ...  Startseite  Rezepte  Zubereitungsarten  Snacks und kleine Gerichte 2 Scheibe/n Vollkornbrot 2 TL Hanfsamen 2 TL Chiasamen 2 Ei(er), weich gekocht 2 
# kleine Avocado(s), reife 50 g Erbsen gekochte, grüne 1 EL Olivenöl 1 Spritzer Zitronensaft n. B. Salz und Pfeffer evtl. Koriandergrün zum Garnieren
#     """
#     extract_ingredients(scraped_recipe_title, scraped_recipe)

    process_all_recipes()
