from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse

class Menu:

    #print(f"Le podium est:")
    #       print(f"{premier}🥇")
    #      print(f"{deuxieme}🥈")
    #     print(f"{troisieme}🥉")
    
    
    #lst_lst = Analyse.points_saison(gestion, 2025)

    #info = Analyse.tri_points(lst_lst)

    #for x in info:
        #print(f"{x[0]} : {x[1]} points")


    ### Les menus

    def menu_principal():
        print("0. Quitter le programme")
        print("1. Statistiques")
        print("2. Quiz")


    def menu_stat():
        print("1. Circuits")
        print("2. Écuries")
        print("3. Pilotes")
        print("4. Saisons")

    def menu_quiz():
        print("1. Palmarès")
        print("2. jouer au quiz")
        
    def menu_ecuries():
        print("1. win")
        print("2. Points")
        print("3. Podiums")
        
    def menu_pilotes():
        print("1. win")
        print("2. Points")
        print("3. Podiums")
        print("4. World champion")
        
    def menu_saisons():
        print("1. win")
        print("2. Points")
        print("3. Podiums")#?