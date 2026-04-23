import requests
import json
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



    def charger_json(self, donnee : str) -> None:
        """Permet de convertir le ficher json en objets

        Args:
            source (str): le ficher json
        """
        with open("donne.json", "r", encoding="utf-8") as fichier:
    
            donnees = json.load(fichier)

        for course in donnees:
            saison = course["saison"]
            date = course["date"]
            nom_circuit = course["nom_circuit"]
            pays = course["pays"]

            new_course = Course(saison, date, nom_circuit, pays)
            self.lst_courses.append(new_course)

            #recuper result pour boucler dessus tantot
            results = course["lst_resultats"]


            for resultat in results:
                #creation du pilote
                dico_driver = resultat["pilote"]
                new_driver = Pilote(dico_driver["driver_id"], dico_driver["prenom"], dico_driver["nom"], dico_driver["nationalite"], dico_driver["date_naissance"])
                            
                if new_driver not in self.lst_pilotes:
                    self.lst_pilotes.append(new_driver)

                #creation de l'écurie
                dico_ecurie = resultat["ecurie"]
                new_ecurie = Ecurie(dico_ecurie["nom"], dico_ecurie["nationalite"])

                if new_ecurie not in self.lst_ecuries:
                    self.lst_ecuries.append(new_ecurie)

                #creation des resultats
                new_resultat = Resultats(
                new_driver,
                new_ecurie,
                resultat["position"],
                resultat["points"],
                resultat["tours"],
                resultat["statut"],
                resultat["meilleur_tour"]
                )

                new_course.ajouter_resultat(new_resultat)


    def sauvegarder_json(self, donnee : str) -> None:
        """Permet de sauvegarder les médias modifier lors du programme dasn le ficher json

        Args:
            source (str): le ficher json
        """

        liste_dictionnaires = []
        for course in self.lst_courses:
            # 2. On appelle notre méthode pour obtenir la version dictionnaire
            dico_course = course.to_dict()
            # On ajoute à la liste de dictionnaires
            liste_dictionnaires.append(dico_course)

            
        # 3. On sauvegarde la liste complète d'un seul coup !
        with open("donnee.json", "w", encoding="utf-8") as fichier:
            # json.dump ajoute la liste de dictio dans le fichier
            json.dump(liste_dictionnaires, fichier, indent=4)