from question import Question
import json
import random
import time

class Quiz:

    def __init__(self):
        self.palmares = []
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
        with open("source.json", "w", encoding="utf-8") as fichier:
            # json.dump ajoute la liste de dictio dans le fichier
            json.dump(self.palmares, fichier, indent=4)
        

    def lire_json_palma(self, source : str):
        with open(source, "r", encoding="utf-8") as fichier:
    
            donnees = json.load(fichier)

        for dico in donnees:
            self.palmares.append(dico)


    def quiz(self):
        creer_quiz = []
        for _ in range(10):
            index = random.randint(0,25)
            creer_quiz.append(self.questions[index])

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
        dico = {nom : pointage}
        self.palmares.append(dico)

        
    def trier_palma(self):
        valeurmax = 10
        for _ in range(10):
            for personne in self.palmares:
                if self.palmares[personne] == valeurmax:
                    print(f"{personne} : {self.palmares[personne]}")
            valeurmax -= 1
                

        
