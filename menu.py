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
        print("3. Podiums")
        
    def menu_circuit():
        print("1. Circuit les plus vieux")
        print("2. Meilleur temps d'un circuit")
        
        
    #choix de l'utilisateur
    
    def choix_pilote(gestion : Gestion_donnees) -> Pilote:
        
        #input des pilotes
        #choisir le pilote
        
        lst_pilote : list[Pilote] = []
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
            
            return pilote_str 

        except:
            print()
            print("Choix out of range")
            print()
            
    def choix_ecurie(gestion : Gestion_donnees) -> Ecurie:
        
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
            
            return ecurie_str

        except:
            print()
            print("Choix du circuit out of range")
            print()
            
    def choix_saison() -> int:
        
        try:
            saison_voulue = int(input("Quelle saison voulez-vous: "))
            
            if 1950 <= saison_voulue <= 2025:
                return saison_voulue
            else:
                print("Votre choix doit être entre 1950 et 2025")
                return None
                
        except:
            print("Veuillez entrer un nombre valide")
            return None