import matplotlib.pyplot as plt
from matplotlib import image


class Question:

    def __init__(self, question : str, choix_rep : str, reponse : str, fichier_image : str ):
        self.question = question
        self.choix_rep = choix_rep
        self.reponse = reponse
        self.fichier_image = fichier_image

        


    def afficher_image(self):
        img = image.imread(f"images/{self.fichier_image}")    
        plt.imshow(img)
        plt.axis('off')
        plt.show()