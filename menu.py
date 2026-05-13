from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse

class Menu:

    ## input des écurie dans le genre de menu
    #Analyse.circuit_plus_longtemps(gestion)
    lst_ecurie = []
    liste_nom = []
    #choisir l'écurie
    for ecurie in gestion.lst_ecuries:
        if ecurie.nom not in liste_nom:
            lst_ecurie.append(ecurie)
            liste_nom.append(ecurie.nom)

    index = 0
    for team in lst_ecurie:
        print(f"{index}. {team.nom}")
        index += 1
    try:
        print()
        ecurie_int = int(input("Entrez le numéro de l'écurie voulu: "))
        ecurie_str = lst_ecurie[ecurie_int]

    except:
        print("Choix du circuit out of range")


            
    #input des pilotes
    #choisir le pilote
    lst_pilote = []
    liste_nom = []

    for pilote in gestion.lst_pilotes:
            
        if pilote.driver_id not in liste_nom:
            lst_pilote.append(pilote)
            liste_nom.append(pilote.driver_id)

    index = 0
    for driver in lst_pilote:
        print(f"{index}. {driver.prenom}  {driver.nom}")
        index += 1
    try:
        print()
        pilote_int = int(input("Entrez le numéro du pilote voulu: "))
        pilote_str = lst_pilote[pilote_int]

    except:
        print("Choix du circuit out of range")

    print(Analyse.plus_de_podium(gestion, pilote_str))

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
        print("1. Circtuits")
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
        print("2. Points")#?
        print("3. Podiums")
        print("4. Word champion")
        
    def menu_saisons():
        print("1. win")
        print("2. Points")
        print("3. Podiums")#?