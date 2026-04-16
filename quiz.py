from question import Question

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
        
            if "album" in dico:
                objet = Chanson(dico["id_media"], dico["titre"], dico["artiste"], dico["duree"], dico["nb_ecoutes"], dico["est_favori"], dico["album"])

            elif "numero_episode" in dico:
                objet = Podcast(dico["id_media"], dico["titre"], dico["artiste"], dico["duree"], dico["nb_ecoutes"], dico["est_favori"], dico["numero_episode"])

            else:
                objet = Media(dico["id_media"], dico["titre"], dico["artiste"], dico["duree"], dico["nb_ecoutes"], dico["est_favori"])

            self.liste_medias.append(objet)


    def sauvegarder_json(self, source : str) -> None:
        """Permet de sauvegarder les médias modifier lors du programme dasn le ficher json

        Args:
            source (str): le ficher json
        """

        liste_dictionnaires = []
        for media in self.liste_medias:
            # 2. On appelle notre méthode pour obtenir la version dictionnaire
            dico_media = media.conversion_dict()
	        # On ajoute à la liste de dictionnaires
            liste_dictionnaires.append(dico_media)
            
        # 3. On sauvegarde la liste complète d'un seul coup !
        with open("source.json", "w", encoding="utf-8") as fichier:
            # json.dump ajoute la liste de dictio dans le fichier
            json.dump(liste_dictionnaires, fichier, indent=4)
        