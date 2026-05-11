from question import Question
import json
import random
import time

class Quiz:

    def __init__(self):
        self.palmares = []
        self.questions : list[Question] = []


    def lire_json_question(self, questions : str) -> None:
        """Permet de convertir le ficher json en objets

        Args:
            questions (str): le ficher json
        """
        with open("questions.json", "r", encoding="utf-8") as fichier:
    
            donnees = json.load(fichier)

        for dico in donnees:
        

            objet = Question(dico["question"], dico["choix_rep"], dico["reponse"], dico["fichier_image"])


            self.questions.append(objet)


    def sauvegarder_json(self, source : str) -> None:
        """Permet de sauvegarder les médias modifier lors du programme dasn le ficher json

        Args:
            source (str): le ficher json
        """

        liste_dictionnaires = []
        for media in self.liste_medias:
            # 2. On appelle notre méthode pour obtenir la version dictionnaire
            dico_media = media.to_dict()
	        # On ajoute à la liste de dictionnaires
            liste_dictionnaires.append(dico_media)
            
        # 3. On sauvegarde la liste complète d'un seul coup !
        with open("source.json", "w", encoding="utf-8") as fichier:
            # json.dump ajoute la liste de dictio dans le fichier
            json.dump(liste_dictionnaires, fichier, indent=4)
        

    def quiz(self):
        creer_quiz = []
        for _ in range(10):
            index = random.randint(0,25)
            creer_quiz.append(self.questions[index])

        pointage = 0
        for quest in creer_quiz:
            print()
            print(quest.question)
            quest.afficher_image()
            print(quest.choix_rep)
            reponse_uti = input("Entrez la lettre : ")
            if reponse_uti == quest.reponse:
                pointage += 1
                print("Bonne Réponse!")
            else:
                print(f"Mauvaise reponse. La reponse était {quest.reponse}")
            print()
            time.sleep(1.5)

        
            