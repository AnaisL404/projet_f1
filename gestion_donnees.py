from saison import Saison
import requests

class Gestion_donnees:
    def __init__(self):
        self.lst_saison : list[Saison] = []

    def call_api(self):

        url_base = "https://api.jolpi.ca/ergast/f1/"

        #url de base + année et results = https://api.jolpi.ca/ergast/année/results/
        try:
            for x in range(2025,2026):
                reponse = requests.get(f"{url_base}{x}/results/")
                data = reponse.json()
                print(data["MRData"]["RaceTable"]["Races"])

                

        except:
            pass


gestion = Gestion_donnees()

gestion.call_api()
