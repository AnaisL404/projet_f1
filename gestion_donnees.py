import requests
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
import time

class Gestion_donnees:
    def __init__(self):
        self.lst_courses : list[Course] = []
        self.lst_pilotes : list[Pilote] = []
        self.lst_ecuries : list[Ecurie] = []

    def _get_with_retry(self, url):
        for x in range(5):
            reponse = requests.get(url)
            if reponse.status_code == 429:
                print(f"Rate limit atteint, attente de {2}s...")
                time.sleep(2)
            else:
                return reponse
        raise Exception(f"Echec après 5 tentatives pour {url}")

    def call_api(self):

        url_base = "https://api.jolpi.ca/ergast/f1/"

        #url de base + année et results = https://api.jolpi.ca/ergast/année/results/
        try:
            for x in range(1950,2026):
                for offset in range(0,401,100):

                    time.sleep(0.5)

                    reponse = self._get_with_retry(f"{url_base}{x}/results/?limit=100&offset={offset}")
                    data = reponse.json()

                    race_list = data["MRData"]["RaceTable"]["Races"]

                    for race in race_list:
                        saison = int(race["season"])
                        date = race["date"]
                        nom_course = race["raceName"]
                        pays = race["Circuit"]["Location"]["country"]

                        #recuper result pour boucler dessus tantot
                        results = race["Results"]

                        if len(self.lst_courses) != 0:
                            if self.lst_courses[len(self.lst_courses)-1].nom_circuit == nom_course:
                                new_course = self.lst_courses[len(self.lst_courses)-1]
                            else:
                                new_course = Course(saison, date, nom_course, pays)
                                self.lst_courses.append(new_course)
                        else:
                            new_course = Course(saison, date, nom_course, pays)
                            self.lst_courses.append(new_course)


                        for resultat in results:
                            #creation du pilote
                            dico_driver = resultat["Driver"]
                            new_driver = Pilote(dico_driver["driverId"], dico_driver["givenName"], dico_driver["familyName"], dico_driver["nationality"], dico_driver["dateOfBirth"])
                            
                            if new_driver not in self.lst_pilotes:
                                self.lst_pilotes.append(new_driver)

                            #creation de l'écurie
                            dico_ecurie = resultat["Constructor"]
                            new_ecurie = Ecurie(dico_ecurie["name"], dico_ecurie["nationality"])
                            if new_ecurie not in self.lst_ecuries:
                                self.lst_ecuries.append(new_ecurie)

                            #creation des resultats
                            new_resultat = Resultats(
                                new_driver,
                                new_ecurie,
                                int(resultat["position"]),
                                float(resultat["points"]),
                                int(resultat["laps"]),
                                resultat["status"],
                                resultat["FastestLap"]["Time"]["time"] if "FastestLap" in resultat else 0 
                            )

                            new_course.ajouter_resultat(new_resultat)
                    
        except Exception as e :
            print(e)


gestion = Gestion_donnees()

gestion.call_api()

for race in gestion.lst_courses:
    print(race.nom_circuit)


