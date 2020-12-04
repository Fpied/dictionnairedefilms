films = {
        0: {"Titre du film": "Le Seigneur des Anneaux",
             "prix": 12},
        1: {"Titre du film": "Harry Potter",
            "prix": 9},
        2: {"Titre du film": "Blade Runner",
            "prix": 7.5},
        }


prix = films[0]["prix"] + films[1]["prix"] + films[2]["prix"]
print(prix)
