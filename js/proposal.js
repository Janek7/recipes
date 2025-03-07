// This is only test data
//const exampleRecipesData = [
    // {"slug": "brokoli-suppe", "title": "Brokoli Suppe", "category": "Suppe", "preview": "..."},
    // {"slug": "reisauflauf", "title": "Reisauflauf", "category": "Auflauf", "preview": "..."},
    // {"slug": "spinatlasagne", "title": "Spinatlasagne", "category": "Auflauf", "preview": "..."}
//];

// Real data is injected by python script process_recipe_data.py into recipesData
const recipesData = [
    {
        "slug": "kurbis-gugelhupf",
        "title": "K\u00fcrbis Gugelhupf",
        "category": "Backen",
        "preview": "Schmeck mit Butterk\u00fcrbis am besten Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "tortellinierbsenauflauf",
        "title": "Tortellini-Erbsen-Auflauf",
        "category": "Auflauf",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "sue-buchteln",
        "title": "S\u00fc\u00dfe Buchteln",
        "category": "Sonstiges",
        "preview": "Mit F\u00fcllungen: Quark und Marmelade Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kartner-reindling",
        "title": "K\u00e4rtner Reindling",
        "category": "Backen",
        "preview": "Haben wir mit Nussf\u00fcllung gebacken. Vergleichbar mit Oma Irmas ber\u00fchmtem gewickelten Kranz Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kefir-pernik",
        "title": "Kefir Pern\u00edk",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "onepotorzo",
        "title": "One-Pot-Orzo",
        "category": "Risotto",
        "preview": "Wo gefunden? Im Kochbuch 'Italienische Feierabendk\u00fcche'. Guten Appetit! :)"
    },
    {
        "slug": "cacio-e-pepe",
        "title": "Cacio e Pepe",
        "category": "Pasta",
        "preview": "Endless Pastabilities ... Wichtig: Nudeln etwas abk\u00fchlen lassen, bevor die Parmesan Creme dazu gegeben wird, damit es keine F\u00e4den zieht Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "safran-risotto",
        "title": "Safran Risotto",
        "category": "Risotto",
        "preview": "Freestyled Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "joghurt-pancakes",
        "title": "Joghurt Pancakes",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Schmeckt mit Joghurt oben drauf sehr cremig! Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "avocado-brot-mit-ruhrei",
        "title": "Avocado Brot mit R\u00fchrei",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Avocado k\u00f6nnen alternative auch nur in Scheiben geschnitten werden Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kokos-gugelhupf",
        "title": "Kokos Gugelhupf",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "chili-sin-carne",
        "title": "Chili sin Carne",
        "category": "Reis",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "couscous-gemuse-salat",
        "title": "Couscous Gem\u00fcse Salat",
        "category": "Sonstiges",
        "preview": "Schmeckt gut mit Pesto und jeglichem Gem\u00fcse Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "overnight-oats-mit-quark",
        "title": "Overnight Oats mit Quark",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Alle m\u00f6glichen N\u00fcsse k\u00f6nnen gehackt als Topping verwendet werden Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "blumenkohlsuppe",
        "title": "Blumenkohlsuppe",
        "category": "Suppe",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "porridge-mit-quark",
        "title": "Porridge mit Quark",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "gefullte-paprika",
        "title": "Gef\u00fcllte Paprika",
        "category": "Reis",
        "preview": "Kann mit Fleisch- oder Frischk\u00e4sef\u00fcllung zubereitet werden Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "omlette-wrap",
        "title": "Omlette Wrap",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Kommt mit Barbecue Sauce gef\u00e4hrlich Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "fantakuchen",
        "title": "Fantakuchen",
        "category": "Backen",
        "preview": "Lissis ber\u00fchmter Kranz, den sie immer gebacken hat! Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "linsensuppe",
        "title": "Linsensuppe",
        "category": "Suppe",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "semmel-baba",
        "title": "Semmel Baba",
        "category": "Sonstiges",
        "preview": "Vergleichbar mit Armer Ritter Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "smazeny-syr",
        "title": "Sma\u017een\u00fd S\u00fdr",
        "category": "Sonstiges",
        "preview": "Zubereitet in der Hei\u00dfluftfrit\u00f6se Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "apfel-smoothie",
        "title": "Apfel Smoothie",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Schmeckt besser mit tschechischem Joghurt als mit deutschem ;) Die Zubereitung dauert ca. 5 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "focaccia",
        "title": "Focaccia",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "salzige-caramel-platzchen",
        "title": "Salzige Caramel Pl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "dal-makhani-mit-belugalinsen",
        "title": "Dal Makhani mit Belugalinsen",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 70 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kartoffel-mit-dip",
        "title": "Kartoffel mit Dip",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "honiglebkuchen",
        "title": "Honiglebkuchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "nusseckenplatzchen",
        "title": "Nusseckenpl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "ruhrei-mit-getrockneten-tomaten-auf-knackebrot",
        "title": "R\u00fchrei mit getrockneten Tomaten auf Kn\u00e4ckebrot",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Die Zubereitung dauert ca. 15 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "froschmauler",
        "title": "Froschm\u00e4uler",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "buzzerl",
        "title": "Buzzerl",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 90 Minuten. Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "kuhflecken-platzchen",
        "title": "Kuhflecken Pl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "vanocka",
        "title": "Vanocka",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 120 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "pistazienkipferl",
        "title": "Pistazienkipferl",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "spekulatiuskipferl-mit-mandeln",
        "title": "Spekulatiuskipferl mit Mandeln",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kokos-barentatzen",
        "title": "Kokos B\u00e4rentatzen",
        "category": "Weihnachten",
        "preview": "Erstes Pl\u00e4tzchenrezept 2024! Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "gefullte-zucchini-mit-linsenbolognese",
        "title": "Gef\u00fcllte Zucchini mit Linsenbolognese",
        "category": "Auflauf",
        "preview": "Perfekt mit Linsenbolognese vom Vortag. Schnelle Zubereitung Die Zubereitung dauert ca. 40 Minuten. Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "kurbis-halusky",
        "title": "K\u00fcrbis Halu\u0161ky",
        "category": "Sonstiges",
        "preview": "Tolles Rezept Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "tomaten-mozarella-risotto",
        "title": "Tomaten Mozarella Risotto",
        "category": "Risotto",
        "preview": "Wo gefunden? Im Kochbuch 'Italienische Feierabendk\u00fcche'. Guten Appetit! :)"
    },
    {
        "slug": "thuna-pasta",
        "title": "Thuna Pasta",
        "category": "Pasta",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "ofen-gemuse-pasta",
        "title": "Ofen Gem\u00fcse Pasta",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "linsencurry",
        "title": "Linsencurry",
        "category": "Reis",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "spinatlasagne",
        "title": "Spinatlasagne",
        "category": "Auflauf",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "kurbis-puffer",
        "title": "K\u00fcrbis Puffer",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "mac-and-cheese-emmi",
        "title": "Mac and Cheese Emmi",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "brokoli-suppe",
        "title": "Brokoli Suppe",
        "category": "Suppe",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "tofu-reis",
        "title": "Tofu Reis",
        "category": "Reis",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 75 vegetarische Rezepte'. Guten Appetit! :)"
    },
    {
        "slug": "zucchini-risotto",
        "title": "Zucchini Risotto",
        "category": "Risotto",
        "preview": "Wo gefunden? Im Kochbuch 'Italienische Feierabendk\u00fcche'. Guten Appetit! :)"
    },
    {
        "slug": "schlagsahnekuchen-mit-fruchten",
        "title": "Schlagsahnekuchen mit Fr\u00fcchten",
        "category": "Backen",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "spaghetti-kurbis",
        "title": "Spaghetti K\u00fcrbis",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "linsen-bolognese",
        "title": "Linsen Bolognese",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach: 85 Rezepte f\u00fcr das ganze Jahr'. Guten Appetit! :)"
    },
    {
        "slug": "franzbrotchen",
        "title": "Franzbr\u00f6tchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "apfel-crumble",
        "title": "Apfel Crumble",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "karottenkuchen",
        "title": "Karottenkuchen",
        "category": "Backen",
        "preview": "In Tarragona gabs es das jeden Tag zum Fr\u00fchst\u00fcck! Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "erdbeer-quark-knodel",
        "title": "Erdbeer Quark Kn\u00f6del",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "bublani-kuchen-mit-himbeeren",
        "title": "Bublani Kuchen mit Himbeeren",
        "category": "Backen",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "ciabatta-mit-mozarella-tomaten-und-pesto",
        "title": "Ciabatta mit Mozarella, Tomaten und Pesto",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "pfannenlasagne",
        "title": "Pfannenlasagne",
        "category": "Auflauf",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "tomaten-aubergine-auflauf",
        "title": "Tomaten Aubergine Auflauf",
        "category": "Auflauf",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "hackpfanne",
        "title": "Hackpfanne",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "ofengnocchi-mit-paprika",
        "title": "Ofen-Gnocchi mit Paprika",
        "category": "Gnocchi",
        "preview": "Kann man jede Woche kochen und schmeckt immer gut! Die Zubereitung dauert ca. 45 Minuten. Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "orzo-mit-tomaten-mozarella-sauce",
        "title": "Orzo mit Tomaten Mozarella Sauce",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "kasekuchen",
        "title": "K\u00e4sekuchen",
        "category": "Backen",
        "preview": "Schmeckt den M\u00e4nnern gut. Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "mohn-quark-kuchen",
        "title": "Mohn Quark Kuchen",
        "category": "Backen",
        "preview": "Mit zwei F\u00fcllungen schmeckt es sehr gut Die Zubereitung dauert ca. 90 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "toast-mit-ei-in-der-pfanne",
        "title": "Toast mit Ei in der Pfanne",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "frankfurter-suppe",
        "title": "Frankfurter Suppe",
        "category": "Suppe",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "reisauflauf",
        "title": "Reisauflauf",
        "category": "Reis",
        "preview": "Dauert zwar lange im Ofen, kann man aber gut mit ins B\u00fcro nehmen Die Zubereitung dauert ca. 70 Minuten. Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "zucchini-ricotta-pasta",
        "title": "Zucchini Ricotta Pasta",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "zucchini-nudel-auflauf",
        "title": "Zucchini Nudel Auflauf",
        "category": "Auflauf",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "griechischer-joghurt-kuchen-mit-beeren",
        "title": "Griechischer Joghurt Kuchen mit Beeren",
        "category": "Backen",
        "preview": "Wo gefunden? Im Kochbuch 'Emmi kocht einfach'. Guten Appetit! :)"
    },
    {
        "slug": "st-martins-hornchen",
        "title": "St. Martins H\u00f6rnchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "zucker-ei-platzchen",
        "title": "Zucker Ei Pl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kekse-aus-gebackpresse",
        "title": "Kekse aus Geb\u00e4ckpresse",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "barentatzen",
        "title": "B\u00e4rentatzen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "hohe-engelsaugen",
        "title": "Hohe Engelsaugen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "vanillekipferl",
        "title": "Vanillekipferl",
        "category": "Weihnachten",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "gebrannte-mandeln",
        "title": "Gebrannte Mandeln",
        "category": "Weihnachten",
        "preview": "Steffis Rezept Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "marzipan-engelsaugen",
        "title": "Marzipan Engelsaugen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kaiserschmarrn",
        "title": "Kaiserschmarrn",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Kochkurs Guten Appetit! :)"
    },
    {
        "slug": "wiener-schnitzel",
        "title": "Wiener Schnitzel",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Kochkurs Guten Appetit! :)"
    },
    {
        "slug": "kasespatzle",
        "title": "K\u00e4sesp\u00e4tzle",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Kochkurs Guten Appetit! :)"
    },
    {
        "slug": "fritatensuppe",
        "title": "Fritatensuppe",
        "category": "Suppe",
        "preview": "Rinderbr\u00fche mit geschnittenen Pfannkuchen Wo gefunden? Kochkurs Guten Appetit! :)"
    },
    {
        "slug": "halloween-madeleines",
        "title": "Halloween Madeleines",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "schnitzel",
        "title": "Schnitzel",
        "category": "Sonstiges",
        "preview": "Kann mit Kartoffelp\u00fcree oder Salzkartoffeln serviert werden. Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "kinderschokoladenkuchen",
        "title": "Kinderschokoladenkuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "gemuse-curry-mit-reis",
        "title": "Gem\u00fcse Curry mit Reis",
        "category": "Reis",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "reis-mit-paprika-zucchini-und-feta",
        "title": "Reis mit Paprika, Zucchini und Feta",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 40 Minuten. Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "pernicek",
        "title": "Pern\u00ed\u010dek",
        "category": "Backen",
        "preview": "Kann mit Apfel oder Marmelade und Schokolade verziert werden Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "himbeer-wolkchen-torte",
        "title": "Himbeer W\u00f6lkchen Torte",
        "category": "Backen",
        "preview": "Gibt es immer bei Oma Gitte an Ostern und zu Muttertag Die Zubereitung dauert ca. 120 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "hefe-brotchen",
        "title": "Hefe Br\u00f6tchen",
        "category": "Backen",
        "preview": "Idea zur Bor\u0161\u010d Suppe Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "borsc",
        "title": "Bor\u0161\u010d",
        "category": "Suppe",
        "preview": "Slawische Rotebeete Suppe Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "gedeckter-apfelkuchen",
        "title": "Gedeckter Apfelkuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "osterlamm-kuchen",
        "title": "Osterlamm Kuchen",
        "category": "Backen",
        "preview": "Spezielle F\u00fcllung mit ausgestochenem und gef\u00e4rbtem Teig in Lamm Form Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kinderriegel-muffins",
        "title": "Kinderriegel Muffins",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "blumen-kuchlein",
        "title": "Blumen K\u00fcchlein",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "marmor-gugelhupf",
        "title": "Marmor Gugelhupf",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "steppdecken-kuchen",
        "title": "Steppdecken Kuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "hermelin-mit-pommes-oder-kartoffeln",
        "title": "Hermelin mit Pommes oder Kartoffeln",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "kuchen-mit-herzfullung",
        "title": "Kuchen mit Herzf\u00fcllung",
        "category": "Backen",
        "preview": "Spezielle F\u00fcllung mit ausgestochenem und gef\u00e4rbtem Teig in Herzform Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kakao-kefir-kuchen",
        "title": "Kakao Kefir Kuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "waffeln",
        "title": "Waffeln",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "quark-gugelhupf",
        "title": "Quark Gugelhupf",
        "category": "Backen",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "asia-nudeln",
        "title": "Asia Nudeln",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "buchticky-se-sodo",
        "title": "Buchti\u010dky se \u0161od\u00f3",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "nadivka",
        "title": "N\u00e1divka",
        "category": "Sonstiges",
        "preview": "Traditionelles tschechisches Gericht zu Ostern Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "zitronen-mohn-kuchen",
        "title": "Zitronen Mohn Kuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "schnitzel-mit-kartoffelsalat",
        "title": "Schnitzel mit Kartoffelsalat",
        "category": "Weihnachten",
        "preview": "Traditionelles tschechisches Weihnachtsessen an Heiligabend Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "hausfreunde",
        "title": "Hausfreunde",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "linzer-platzchen",
        "title": "Linzer Pl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "nurnberger-elisenlebkuchen",
        "title": "N\u00fcrnberger Elisenlebkuchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "bananen-platzchen",
        "title": "Bananen Pl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "elisenlebkuchen",
        "title": "Elisenlebkuchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "spritzgebackene",
        "title": "Spritzgebackene",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "reispfanne-mit-paprika-und-ei",
        "title": "Reispfanne mit Paprika und Ei",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 25 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "zimtschnecken",
        "title": "Zimtschnecken",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kalter-hund",
        "title": "Kalter Hund",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "aubgerine-zucchini-pasta",
        "title": "Aubgerine Zucchini Pasta",
        "category": "Pasta",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "butter-creme-torte",
        "title": "Butter Creme Torte",
        "category": "Backen",
        "preview": "Gabs zum Valentinstag 2022 :) Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "cinska",
        "title": "\u010c\u00ednska",
        "category": "Reis",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "udon-sesam-nudeln",
        "title": "Udon Sesam Nudeln",
        "category": "Pasta",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "falaffel-salat-mit-gegrilltem-gemuse",
        "title": "Falaffel Salat mit gegrilltem Gem\u00fcse",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "falafel-burger",
        "title": "Falafel Burger",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "raclette",
        "title": "Raclette",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "zucchini-gemuse-schiffchen",
        "title": "Zucchini Gem\u00fcse Schiffchen",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "roulladen-mit-spatzlen",
        "title": "Roulladen mit Sp\u00e4tzlen",
        "category": "Weihnachten",
        "preview": "Mittlerweile traditionelles Weihnachtsessen am 1. Weihnachtsfeiertag bei Oma Gitte Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "mohnplatzchen",
        "title": "Mohnpl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "nussecken",
        "title": "Nussecken",
        "category": "Backen",
        "preview": "Oma Gitte nutzt Teer ;) Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "knusprige-kartoffeln-und-kichererbsen-mit-chili--joghurt",
        "title": "Knusprige Kartoffeln und Kichererbsen mit Chili & Joghurt",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "butterplatzchen",
        "title": "Butterpl\u00e4tzchen",
        "category": "Weihnachten",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "knusprig-gebratene-gnocchi-mit-knoblauchpilzen",
        "title": "Knusprig gebratene Gnocchi mit Knoblauch-Pilzen",
        "category": "Gnocchi",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "gefullte-paprika-im-teigmantel",
        "title": "Gef\u00fcllte Paprika im Teigmantel",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "chilinudeln-mit-gemuse",
        "title": "Chili-Nudeln mit Gem\u00fcse",
        "category": "Pasta",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "curry-maultaschenpfanne",
        "title": "Curry Maultaschenpfanne",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "maultaschenomelett-mit-feta--paprika",
        "title": "Maultaschenomelett mit Feta & Paprika",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "ausflugskuchen",
        "title": "Ausflugskuchen",
        "category": "Backen",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "onepotspatzle-mit-rauchertofu",
        "title": "One-Pot-Sp\u00e4tzle mit R\u00e4uchertofu",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "pilzragout",
        "title": "Pilz-Ragout",
        "category": "Sonstiges",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "kasekuchen-brownies",
        "title": "K\u00e4sekuchen Brownies",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "kokoslimettencurry-mit-garnelen",
        "title": "Kokos-Limetten-Curry mit Garnelen",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 45 Minuten. Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "gnocchi-mac--cheesestyle",
        "title": "Gnocchi Mac & Cheese-Style",
        "category": "Gnocchi",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "nudelpilzpfanne",
        "title": "Nudel-Pilz-Pfanne",
        "category": "Pasta",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "burger",
        "title": "Burger",
        "category": "Sonstiges",
        "preview": "Mit normalem oder vegetarischen Patty, Falafel, Nuggets ... Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "monte-cristo-toast",
        "title": "Monte Cristo Toast",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "lachs-spinat-quiche",
        "title": "Lachs Spinat Quiche",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "porridge",
        "title": "Porridge",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Am besten schmeckt es mit Beeren, Bananen und Ahornsirup als Topping! Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "curry-wurst",
        "title": "Curry Wurst",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "zimt-schoko-porridge",
        "title": "Zimt Schoko Porridge",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Wo gefunden? Auf Instagram. Guten Appetit! :)"
    },
    {
        "slug": "pita-taschen-mit-gemuse",
        "title": "Pita Taschen mit Gem\u00fcse",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "franzosische-salat-sauce",
        "title": "Franz\u00f6sische Salat Sauce",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 5 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "tortelloni-mit-wurziger-tomatenkokossauce",
        "title": "Tortelloni mit w\u00fcrziger Tomaten-Kokos-Sauce",
        "category": "Pasta",
        "preview": "Wo gefunden? In der KptnCook App. Guten Appetit! :)"
    },
    {
        "slug": "cookies",
        "title": "Cookies",
        "category": "Backen",
        "preview": "Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "brioche",
        "title": "Brioche",
        "category": "Backen",
        "preview": "Die Zubereitung dauert ca. 80 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "welcome-meal",
        "title": "Welcome Meal",
        "category": "Pasta",
        "preview": "Kann mit Garden Gourmet Filetstreifen oder H\u00e4hnchen zubereitet werden Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "waldpilz-risotto",
        "title": "Waldpilz Risotto",
        "category": "Risotto",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "champignon-sahne-nudeln",
        "title": "Champignon Sahne Nudeln",
        "category": "Pasta",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "pancakes",
        "title": "Pancakes",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "sukartoffel-chips",
        "title": "S\u00fc\u00dfkartoffel Chips",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "sukartoffel-mit-kase",
        "title": "S\u00fc\u00dfkartoffel mit K\u00e4se",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "reisnudel-pfanne",
        "title": "Reisnudel Pfanne",
        "category": "Pasta",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "kartoffelgratin",
        "title": "Kartoffelgratin",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 40 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "schokoschnecken",
        "title": "Schokoschnecken",
        "category": "Backen",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "penne-allarrabbiata",
        "title": "Penne all\u2019arrabbiata",
        "category": "Pasta",
        "preview": "Originalrezept von Sally Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "maulwurfkuchen",
        "title": "Maulwurfkuchen",
        "category": "Backen",
        "preview": "Die Zubereitung dauert ca. 120 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "reis-mit-curry-sauce",
        "title": "Reis mit Curry Sauce",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "apfelstrudel",
        "title": "Apfelstrudel",
        "category": "Backen",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "pesto-kartoffeln",
        "title": "Pesto Kartoffeln",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "gnocchi-spinat-huhnchen-curry-auflauf",
        "title": "Gnocchi Spinat H\u00fchnchen Curry Auflauf",
        "category": "Gnocchi",
        "preview": "Die Zubereitung dauert ca. 50 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "mac-and-cheese",
        "title": "Mac and Cheese",
        "category": "Pasta",
        "preview": "Gekocht an Silvester 2021 im Salvator Hotel Die Zubereitung dauert ca. 75 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "vegetarischer-gnocchi-auflauf",
        "title": "Vegetarischer Gnocchi Auflauf",
        "category": "Gnocchi",
        "preview": "Die Zubereitung dauert ca. 40 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "toast-mit-ruhrei-und-tomaten",
        "title": "Toast mit R\u00fchrei und Tomaten",
        "category": "Fr\u00fchst\u00fcck",
        "preview": "Die Zubereitung dauert ca. 15 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "garnelen-spaghetti",
        "title": "Garnelen Spaghetti",
        "category": "Pasta",
        "preview": "Spaghetti Aglio e Olio mit gebratenen Garnelen und Ajvar Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "bohnenkraut-kartoffel-feta-pfanne",
        "title": "Bohnenkraut Kartoffel Feta Pfanne",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 50 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "macaroni-gemuse-auflauf",
        "title": "Macaroni Gem\u00fcse Auflauf",
        "category": "Auflauf",
        "preview": "Die Zubereitung dauert ca. 50 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "curry-penne",
        "title": "Curry Penne",
        "category": "Pasta",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "konigsberger",
        "title": "K\u00f6nigsberger",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 60 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "nussschnecken",
        "title": "Nussschnecken",
        "category": "Backen",
        "preview": "Die Zubereitung dauert ca. 110 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "toast-mit-gebackenem-feta",
        "title": "Toast mit gebackenem Feta",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 15 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "kurbissuppe",
        "title": "K\u00fcrbissuppe",
        "category": "Suppe",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "spicy-avokado-pasta",
        "title": "Spicy Avokado Pasta",
        "category": "Pasta",
        "preview": "Wo gefunden? Im Internet. Guten Appetit! :)"
    },
    {
        "slug": "svickova",
        "title": "Svickova",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 180 Minuten. Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "gemuse-feta-auflauf",
        "title": "Gem\u00fcse Feta Auflauf",
        "category": "Auflauf",
        "preview": "Die Zubereitung dauert ca. 35 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "gemuse-spaghetti-auflauf",
        "title": "Gem\u00fcse Spaghetti Auflauf",
        "category": "Auflauf",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "flammkuchen",
        "title": "Flammkuchen",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 75 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "pizza",
        "title": "Pizza",
        "category": "Sonstiges",
        "preview": "Katharians Rezept Die Zubereitung dauert ca. 45 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "tomatenreis",
        "title": "Tomatenreis",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "hahnchen-gyros",
        "title": "H\u00e4hnchen Gyros",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 50 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "hahnchen-curry",
        "title": "H\u00e4hnchen Curry",
        "category": "Reis",
        "preview": "Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "wraps",
        "title": "Wraps",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "waffel-kirsch-desert",
        "title": "Waffel Kirsch Desert",
        "category": "Sonstiges",
        "preview": "Wo gefunden? Familien Rezept Guten Appetit! :)"
    },
    {
        "slug": "bananenbrot",
        "title": "Bananenbrot",
        "category": "Backen",
        "preview": "Die Zubereitung dauert ca. 80 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "gnocchis-mit-geschmolzenen-tomaten",
        "title": "Gnocchis mit geschmolzenen Tomaten",
        "category": "Gnocchi",
        "preview": "Janeks erstes selbst ausprobiertes Rezept (und \u00fcberzeugt noch immer) Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "tortelliniauflauf",
        "title": "Tortelliniauflauf",
        "category": "Auflauf",
        "preview": "Die Zubereitung dauert ca. 65 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "feta-taschen",
        "title": "Feta Taschen",
        "category": "Sonstiges",
        "preview": "Feta Taschen aus Bl\u00e4tterteig - Guter Partysnack zum Mitbringen Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "spaghetti-carbonara",
        "title": "Spaghetti Carbonara",
        "category": "Pasta",
        "preview": "Steffis Rezept und Janeks erster Kochversuch Die Zubereitung dauert ca. 30 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    },
    {
        "slug": "sandwich-toasts",
        "title": "Sandwich Toasts",
        "category": "Sonstiges",
        "preview": "Die Zubereitung dauert ca. 20 Minuten. Wo gefunden? In unserem Kochbuch von 2021. Guten Appetit! :)"
    }
];


function proposeRandomRecipe() {
    /**
     * selects a random recipe based on the category selection and updates the page
     */

    // 1) filter recipe data for selection from drop down
    var filteredRecipesData = filterRecipeData(recipesData);

    // check for empty categories
    if (filteredRecipesData.length == 0) {
        return;
    }

    // 2) select a random ones
    var selectedRecipe = selectRandomRecipe(filteredRecipesData);

    // 3) update search result section according to it
    editSearchResultElement(selectedRecipe);
}


function filterRecipeData(recipesData) {
    /**
     * filters the total recipeData based on the selected categories in the dropdown
     */
    // get selected categories
    var dropdown = document.getElementById('categoryDropdown');
    var selectedCategories = Array.from(dropdown.selectedOptions).map(option => option.value);

    // filter recipeData for this categories
    var filteredRecipeData = recipesData.filter(recipe => 
        selectedCategories.includes(recipe.category)
    );
    console.log("Selected categories: " + selectedCategories + " (" + filteredRecipeData.length + " Recipes)");

    return filteredRecipeData;

}


function selectRandomRecipe(recipesData) {
    /**
     * selects random one recipe from a given recipeData array
     */

    // var recipeTitles = recipeData.map(recipe => recipe.title);
    var selectedRecipe = recipesData[Math.floor(Math.random() * recipesData.length)];
    console.log("Randomly selected recipe: " + selectedRecipe.title);
    return selectedRecipe;

}


function editSearchResultElement(selectedRecipe) {
    /**
     * update the search result element according to the selected recipe
     */
    
    // 1) toggle search result box visibilty
    var resultBox = document.getElementById("proposal-result-box");
    resultBox.style.display = "block"; // Show the element

    // 2) Update header
    var titleHeader = document.getElementById("proposal-title");
    titleHeader.innerText = selectedRecipe.title;

    // 3) Update preview
    var titleHeader = document.getElementById("proposal-preview");
    titleHeader.innerText = selectedRecipe.preview;

    // 4) Update href to recipe post
    var titleHeader = document.getElementById("proposal-ref");
    titleHeader.setAttribute("href", "../p/" + selectedRecipe.slug);

}