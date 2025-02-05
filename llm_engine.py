from huggingface_hub import InferenceClient
from langchain.prompts import ChatPromptTemplate
from langchain_core.prompt_values import PromptValue

from utils import config, read_file


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


def extract_ingredients(scraped_recipe_title, scraped_recipe: str):
    prompt_template_text = read_file("prompts\\extract_ingredients.txt")
    prompt = ChatPromptTemplate.from_template(template=prompt_template_text)

    # Format the prompt
    formatted_prompt = prompt.format(
        title=scraped_recipe_title,
        recipe=scraped_recipe
    )
    
    response = llm_invoke(formatted_prompt)
    print(response)


if __name__ == '__main__':
    scraped_recipe_title = "Superfood-Frühstücksbrot mit Avocado und Ei von Wiktorija| Chefkoch"
    scraped_recipe = """
    PLUSDeine Plus InhalteUnsere PLUS ProfileRezepte des MonatsRezepte aus MagazinenMehr über PLUS erfahren1 Monat kostenlos testen Unsere PLUS Profile Rezepte 
des Monats Rezepte aus Magazinen RezepteEmpfehlungenWas koche ich heute?Was backe ich heute?RezeptsammlungenRezeptempfehlungenDas Perfekte DinnerAlle RezepteRezepte findenBeliebte Rezepte heuteRezepte – schnell und einfachUnsere PLUS RezepteNeue RezepteMarkenrezepte Was koche ich heute? Was backe ich heute? Rezeptsammlungen Rezeptempfehlungen Das Perfekte Dinner Beliebte Rezepte heute Rezepte – schnell und einfach Unsere PLUS Rezepte Neue Rezepte MagazinÜbersichtAlltagskücheWintergerichteVegetarisch & VeganLänderkücheBackenLow Carb & ErnährungÜber den TellerrandUnsere Top-RezepteMagazin ÜbersichtAktuellesPunkt 12 unter SternenDas perfekte DinnerUnsere Produkt-LieblingeKüchengeräte im VergleichDie NFL bei ChefkochNachhaltigkeit in der KücheDie Redaktion empfiehltChefkoch trifft Fackelmann Alltagsküche Wintergerichte Vegetarisch & Vegan Länderküche Backen Low Carb & Ernährung Über den Tellerrand Unsere Top-Rezepte Punkt 12 unter Sternen Das perfekte Dinner Unsere Produkt-Lieblinge Küchengeräte im Vergleich Die NFL bei Chefkoch Nachhaltigkeit in der Küche Chefkoch trifft Fackelmann VideosVideosShared TableProbier was Neues!Mit Chefkoch um die WeltLieblingsrezepteEinfach leckerRikes BackschuleFabios KochschuleHack'n'RollBrot backenVideo ÜbersichtSchwäbische LinsenEinfache Low-Carb-PizzaTexas Chili Shared Table Probier was Neues! Mit Chefkoch um die Welt Lieblingsrezepte Einfach lecker Rikes Backschule Fabios Kochschule Hack'n'Roll Brot backen Schwäbische Linsen Einfache Low-Carb-Pizza Texas Chili CommunityCommunityAktuelle BeiträgeKochenPlaudereckeBackenLifestyleSonstige KochthemenAlle ForenAlle Gruppen Aktuelle Beiträge Kochen Plauderecke Backen Lifestyle Sonstige Kochthemen Unsere PLUS Profile Rezepte des Monats Rezepte aus Magazinen Was koche ich heute? Was backe ich heute? Rezeptsammlungen Rezeptempfehlungen Das Perfekte Dinner Beliebte Rezepte heute Rezepte – schnell und einfach Unsere PLUS Rezepte Neue Rezepte Alltagsküche Wintergerichte Vegetarisch & Vegan Länderküche Backen Low Carb & Ernährung Über den Tellerrand Unsere Top-Rezepte Punkt 12 unter Sternen Das perfekte Dinner Unsere Produkt-Lieblinge Küchengeräte im Vergleich Die NFL bei Chefkoch Nachhaltigkeit in der Küche Chefkoch trifft Fackelmann Shared Table Probier was Neues! Mit Chefkoch um die Welt Lieblingsrezepte Einfach lecker Rikes Backschule Fabios Kochschule Hack'n'Roll Brot backen Schwäbische Linsen Einfache Low-Carb-Pizza Texas Chili Aktuelle Beiträge Kochen Plauderecke Backen Lifestyle Sonstige Kochthemen Presse Jobs Impressum AGB Meldung rechtswidrige Inhalte Verträge hier kündigen Datenschutz Datenschutz-Einstellungen Werben Sie bei uns Nutzungsbasierte Online Werbung Rezepte finden Was koche ich heute Was backe ich heute Magazin Übersicht Foren Videos Übersicht Zum Newsletter anmelden FAQ 
...  Startseite  Rezepte  Zubereitungsarten  Snacks und kleine Gerichte 2 Scheibe/n Vollkornbrot 2 TL Hanfsamen 2 TL Chiasamen 2 Ei(er), weich gekocht 2 
kleine Avocado(s), reife 50 g Erbsen gekochte, grüne 1 EL Olivenöl 1 Spritzer Zitronensaft n. B. Salz und Pfeffer evtl. Koriandergrün zum Garnieren
    """
    extract_ingredients(scraped_recipe_title, scraped_recipe)