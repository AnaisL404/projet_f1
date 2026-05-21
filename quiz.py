from question import Question
import json
import random
import time


class Quiz:
    """Représente le quiz sur la f1
    """

    def __init__(self):
        self.palmares: list[dict] = []
        self.questions : list[Question] = []


    def lire_json_question(self, question : str) -> None:
        """Permet de convertir le ficher json en objets

        Args:
            questions (str): le ficher json
        """
        with open(question, "r", encoding="utf-8") as fichier:
    
            donnees = json.load(fichier)

        for dico in donnees:
        

            objet = Question(dico["question"], dico["choix_rep"], dico["reponse"], dico["fichier_image"])


            self.questions.append(objet)


    def sauvegarder_json_palma(self, source : str) -> None:
        """Permet de sauvegarder le palamres dans le ficher json

        Args:
            source (str): le ficher json
        """
            
        # 3. On sauvegarde la liste complète d'un seul coup !
        with open(source, "w", encoding="utf-8") as fichier:
            # json.dump ajoute la liste de dictio dans le fichier
            json.dump(self.palmares, fichier, indent=4, ensure_ascii=False)
        

                
    def lire_json_palma(self, source : str) -> None:
        """Permet de lire le json du palmares et de le sauvegarder dans l'objet quiz

        Args:
            source (str): le nom du fichier json
        """
        self.palmares = []
        
        with open(source, "r", encoding="utf-8") as fichier:
    
            donnees = json.load(fichier)

        for dico in donnees:
            self.palmares.append(dico)


    def quiz(self) -> None:
        """Permet de creer le quiz de dix questions, compter le poitage et sauvegarder dans le parlmares
        """

        creer_quiz = random.sample(self.questions, 10)
        
        pointage = 0
        
        for quest in creer_quiz:
            print()
            print(quest.question)
            print(quest.choix_rep)
            quest.afficher_image()
            reponse_uti = input("Entrez la lettre : ")
            
            if reponse_uti == quest.reponse:
                pointage += 1
                print("Bonne Réponse!")
                
            else:
                print(f"Mauvaise reponse. La reponse était {quest.reponse}")
            print()
            time.sleep(1.5)
        
        print(f"Votre pointage est : {pointage}")

        nom = input("Entrez votre nom pour le palmarès : ")
        dico = {"nom" : nom, "pointage" : pointage}
        self.palmares.append(dico)
        
        Quiz.sauvegarder_json_palma(self, "palmares.json")

            
    def trier_palma(self) -> None:
        """Permet de d'afficher le palmares en ordre de pointage
        """
        scores = []

        # 1. récupérer tous les scores uniques
        for personne in self.palmares:
            if personne["pointage"] not in scores:
                scores.append(personne["pointage"])

        # 2. tri décroissant manuel des scores
        for i in range(len(scores)):
            for j in range(i + 1, len(scores)):
                if scores[j] > scores[i]:
                    scores[i], scores[j] = scores[j], scores[i]

        # 3. affichage
        for score in scores:
            for personne in self.palmares:
                if personne["pointage"] == score:
                    print(f'{personne["nom"]} : {personne["pointage"]}')
        
