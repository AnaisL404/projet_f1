from matplotlib import image


class Question:

    def __init__(self, question : str, choix_rep : str, reponse : str, fichier_image  ):
        self.question = question
        self.choix_rep = choix_rep
        self.reponse = reponse

        