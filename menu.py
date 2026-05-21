from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse

class Menu:

    ### Les menus

    def menu_principal():
        print("-----------------------")
        print("       Projet F1")
        print("-----------------------")
        print("0. Quitter le programme")
        print("1. Statistiques")
        print("2. Quiz")


    def menu_stat():
        print("-----------------------")
        print(" Menu des statistiques")
        print("-----------------------")
        print("1. Circuits")
        print("2. Écuries")
        print("3. Pilotes")
        print("4. Saisons")

    def menu_quiz():
        print("-----------------------")
        print("         Quiz")
        print("-----------------------")
        print("1. Palmarès")
        print("2. jouer au quiz")
        
    def menu_ecuries():
        print("-----------------------")
        print("   Stats par écurie")
        print("-----------------------")
        print("1. win")
        print("2. Points")
        print("3. Podiums")
        
    def menu_pilotes():
        print("------------------------")
        print("    Stats par pilote")
        print("------------------------")
        print("1. win")
        print("2. Points")
        print("3. Podiums")
        print("4. World champion")
        
    def menu_saisons():
        print("------------------------")
        print("    Stats par saison")
        print("------------------------")
        print("1. win")
        print("2. Points")
        print("3. Podiums")
        
    def menu_circuit():
        print("------------------------")
        print("   Stats des circuits")
        print("------------------------")
        print("1. Circuit les plus vieux")
        print("2. Meilleur temps d'un circuit")
        
        
    #choix de l'utilisateur
    
    def choix_pilote(gestion : Gestion_donnees) -> Pilote:
        """Permet de choisir un pilote pour l'utiliser dans les fonctions de statistiques

        Args:
            gestion (Gestion_donnees): L'object contenant la liste de pilotes

        Returns:
            Pilote: l'objet pilote choisi
        """
        
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
        """Permet de choisir une ecurie pour l,utiliser dans les fonctions de statistiques

        Args:
            gestion (Gestion_donnees): L'objet contenant la liste d'ecuries

        Returns:
            Ecurie: L'objet écurie choisi
        """
        
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
        """Permet de choisir une saison de f1 entre 1950 et 2025

        Returns:
            int: la saison voulue
        """
        
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