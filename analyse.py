import matplotlib.pyplot as plt
from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie

class Analyse:
    """permet de faire toutes les fonctions d'analyse
    """
    

    def circuit_plus_longtemps(gestion : Gestion_donnees) -> None:
        """permet de faire la diagramme des circuits qui sont la depuis le plus longtemps

        Args:
            gestion (Gestion_donnees): classe gestion de données (API)
        """
        
        dico_courses = {}

        for course in gestion.lst_courses:

            if course.nom_circuit in dico_courses:
                dico_courses[course.nom_circuit] += 1
                
            else:
                dico_courses[course.nom_circuit] = 1
        
        liste_nb_apparitions = []
        valeurmax = 0
        circuit_max = ""
        liste_10_max = []

        #boucle pour trouver les 10 courses
        for _ in range(10):
            valeurmax = 0
            circuit_max = ""

            #boucle pour trouver chaque circuit max
            for circuit in dico_courses:

                if dico_courses[circuit] > valeurmax:
                    valeurmax = dico_courses[circuit]
                    circuit_max = circuit
            
            #ajout a liste 10 circuits et supprime du dictionnaire
            liste_10_max.append(circuit_max)
            liste_nb_apparitions.append(valeurmax)
            dico_courses.pop(circuit_max)

        #graphique a bandes
        plt.bar(liste_10_max, liste_nb_apparitions)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout() # Ensures labels fit within the image


        plt.xlabel("Nom des circuits")
        plt.ylabel("Nombre de grand prix")
        plt.title("Top 10 des grands prix qui ont été présents lors du plus grand nombre de saisons ")
        plt.show()
    
        


    def meilleur_temps_circuit(gestion: Gestion_donnees) -> str:
        """donne le temps le plus rapide du circuit choisi

        Args:
            gestion (Gestion_donnees): gestion (Gestion_donnees): classe gestion de données (API)

        Returns:
            str: retourne le temps le plus rapide ainsi que le pilote qui la effectuer et l'année
        """
        
        # boucle pour voir les afficher les nom de circuit et pouvoir choisir le circuit voulu
        liste_circuit : list[Course] = []
        liste_nom = []

        for course in gestion.lst_courses:

            if course.saison >= 2004:

                if course.nom_circuit not in liste_nom:
                    liste_circuit.append(course)
                    liste_nom.append(course.nom_circuit)

        index = 0

        for course in liste_circuit:
            print(f"{index}. {course.nom_circuit} - {course.nom_gp}")
            index += 1

        try:
            print()
            circuit_int = int(input("Entrez le numéro du circuit voulu: "))
            circuit_str = liste_circuit[circuit_int]

        except:
            print("Choix du circuit out of range")

        #initiallisation des valeurs
        best_lap_min = 10000
        best_lap_sec = 10000
        best_lap_milli = 10000

        for course in gestion.lst_courses:

            if course.nom_circuit == circuit_str.nom_circuit:

                for resultat in course.lst_resultats:

                    if resultat.meilleur_tour != 0:
                        minutes_str, reste = resultat.meilleur_tour.split(":")
                        secondes_str, millisecondes_str = reste.split(".")

                        #valeurs du temps à comparer
                        min= int(minutes_str)
                        sec = int(secondes_str)
                        milli = int(millisecondes_str)
                        
                    #comparer les le temps avec les variable initialiser
                        if min < best_lap_min:
                            best_lap_min = min
                            best_lap_sec = sec
                            best_lap_milli = milli
                            pilote = resultat.pilote.nom
                            annee = course.saison

                        elif min == best_lap_min:

                            if sec < best_lap_sec:
                                best_lap_sec = sec
                                best_lap_milli = milli
                                pilote = resultat.pilote.nom
                                annee = course.saison 

                            elif sec == best_lap_sec:

                                if milli < best_lap_milli:
                                    best_lap_milli = milli
                                    pilote = resultat.pilote.nom
                                    annee = course.saison  
 
    #rajouter des zéros pour être comme dans le json
        if len(str(best_lap_milli)) == 2:
            best_lap_milli = f"0{best_lap_milli}"

        if len(str(best_lap_milli)) == 1:
            best_lap_milli = f"00{best_lap_milli}"

        meilleur_temps = (f"{best_lap_min}:{best_lap_sec}.{best_lap_milli}")

        
        return (f"Le meilleur temps à été réaliser par {pilote} en {annee} et est de {meilleur_temps}")


    def plus_de_podium(gestion : Gestion_donnees, pilote_choisi: Pilote) -> str:
        """permet de donner le nombre de podium effectuer par un pilote choisi

        Args:
            gestion (Gestion_donnees): gestion (Gestion_donnees): classe gestion de données (API)
            pilote_choisi (Pilote): pilote choisi par l'utilisateur

        Returns:
            str: retourne le nombre de podium effectuer par le pilote en phrase
        """

        #initialisation
        nb_podium = 0

        for course in gestion.lst_courses:

            podium = course.podium()
            podium_nom = [podium[0].driver_id, podium[1].driver_id, podium[2].driver_id]

            if pilote_choisi.driver_id in podium_nom:
                nb_podium += 1
                
        return f"Le pilote {pilote_choisi} à fait {nb_podium} podiums dans sa carrière"
    
    
    def plus_de_points(gestion : Gestion_donnees, pilote_choisi: Pilote) -> str:
    
    
        #initialisation
        nb_points = 0

        for course in gestion.lst_courses:
            
            for results in course.lst_resultats:
                
                if results.pilote.driver_id == pilote_choisi.driver_id:
                    nb_points += results.points     
                
        return f"Le pilote {pilote_choisi} à fait {nb_points} points dans sa carrière"

    
    
    
    
        
    def plus_de_win(gestion : Gestion_donnees, pilote_choisi: Pilote) -> str:
        """permet de donner le nombre de victoire d'un pilote choisi

        Args:
            gestion (Gestion_donnees): gestion (Gestion_donnees): classe gestion de données (API)
            pilote_choisi (Pilote): pilote choisi par l'utilisateur

        Returns:
            str: retourne le nombre de victoire effectuer par le pilote en phrase
        """

        #initialisation
        nb_win = 0
        
        for course in gestion.lst_courses:

            if pilote_choisi.driver_id == course.vainqueur().driver_id:
                nb_win += 1

        return f"Le pilote {pilote_choisi} à fait {nb_win} podiums dans sa carrière"

    

    def pourcentage_win_saison(gestion : Gestion_donnees, saison_voulue : int) -> None:
        """permet de faire le diagramme de la répartition des points de la saison par pilote

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            saison_voulue (int): saison choisi par l'utilisateur
        """
        
        courses_saison : list[Course] = []

        for course in gestion.lst_courses:

            if course.saison == saison_voulue:
                courses_saison.append(course)

        #initialisation
        winners = []
        nb_wins = []

        for course in courses_saison:

            for resultat in course.lst_resultats:

                if resultat.pilote.driver_id == course.vainqueur().driver_id:

                    if resultat.pilote.driver_id in winners:

                        for x in range(len(winners)):

                            if resultat.pilote.driver_id == winners[x]:
                                nb_wins[x] += 1

                    else:
                        winners.append(resultat.pilote.driver_id)
                        nb_wins.append(1)
        
        labels = winners
        parts = nb_wins

        plt.pie(parts)

        plt.legend(labels)
        plt.title(f"Repartition des wins de la saison {saison_voulue} ")

        plt.show()

    def points_saison(gestion : Gestion_donnees, saison_voulue : int) -> list:
        """fait un dictionnaire des pilote avec leur points gagner durant la saison

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            saison_voulue (int): saison choisi par l'utilisateur

        Returns:
            list: retourne une liste de liste contenant le pilote et leurs points
        """
        
        courses_saison : list[Course]= []

        for course in gestion.lst_courses:

            if course.saison == saison_voulue:
                courses_saison.append(course)

        results = {}

        for course in courses_saison:

            for resultat in course.lst_resultats:

                if resultat.pilote.driver_id in results:
                    results[resultat.pilote.driver_id] += resultat.points

                else:
                    results[resultat.pilote.driver_id] = resultat.points
        
            lst_lst : list[list] = list(results.items())

        return lst_lst
    
    def podiums_saison(gestion : Gestion_donnees, saison_voulue : int) -> list:
        
        courses_saison : list[Course]= []

        for course in gestion.lst_courses:

            if course.saison == saison_voulue:
                courses_saison.append(course)

        results = {}

        for course in courses_saison:
            
            podium = course.podium()
            podium_nom = [podium[0].driver_id, podium[1].driver_id, podium[2].driver_id]

            for resultat in course.lst_resultats:
                
                if resultat.pilote.driver_id in podium_nom:

                    if resultat.pilote.driver_id in results:
                        results[resultat.pilote.driver_id] += 1

                    else:
                        results[resultat.pilote.driver_id] = 1
        
            lst_lst : list[list] = list(results.items())

        return lst_lst
        



    def tri(lst_lst : list) -> list[list]:
        """permet de trié les points de la liste de liste pilote:points

        Args:
            lst_lst (list): liste de liste pilote:points

        Returns:
            list[list]: liste de loiste pilote:points trié
        """
        
        liste_a_trier : list[list] = lst_lst.copy()

        #si la liste est vide ou ne contient qu'un élément
        #elle est triée, on renvoie directement la liste + sortir de la boucle infini
        if len(liste_a_trier) <= 1:
            return liste_a_trier
        
        pivot = liste_a_trier[len(liste_a_trier) -1] #pivot est le dernier élément de la liste

        petits = []
        grands = []


        for x in range(len(liste_a_trier) -1): #parcourt tous les éléments suf le pivot
            if liste_a_trier[x][1] < pivot[1]:
                petits.append(liste_a_trier[x]) #ajoute les éléments plus petits que le pivot
            else:
                grands.append(liste_a_trier[x]) #ajoute les éléments plus grands que le pivot

        #combine les résultats pour obtenir la liste trier finale
        return Analyse.tri(petits) + [pivot] + Analyse.tri(grands)

    
    def pilotes_ecurie(gestion : Gestion_donnees, ecurie_choisi: Ecurie) -> dict:
        """fait le trie de chaque pilotes qui on fait parti de l'écurie choisi

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            ecurie_choisi (Ecurie): écurie choisi par l'utilisateur

        Returns:
            dict: retounre le dictionnaire des pilotes de l'écurie 
        """
        #initialisation
        liste_nom = []
        pilotes = {}

        for course in gestion.lst_courses:

            for resultat in course.lst_resultats:

                if resultat.ecurie.nom == ecurie_choisi.nom:

                    if resultat.pilote.driver_id not in liste_nom:
                       liste_nom.append(resultat.pilote.driver_id)
                       pilotes[resultat.pilote.driver_id] = 0

                    else:
                        pilotes[resultat.pilote.driver_id] = 0

        return pilotes
    

    def afficher_top3(results: dict) -> None:
        """permet d'afficher les 3 meilleurs pilotes de l'écurie

        Args:
            results (dict): dictionnaire des pilotes et de leurs valeurs de points/podiums/wins
        """
        
        results_copy = results.copy()

        liste_top_3 = []

        try:

            for _ in range(3):

                valeurmax = -1
                pilote_max = ""

                for pilote in results_copy:

                    if results_copy[pilote] > valeurmax:

                        valeurmax = results_copy[pilote]
                        pilote_max = pilote

                liste_top_3.append((pilote_max, valeurmax))

                results_copy.pop(pilote_max)

            for pilote, valeur in liste_top_3:

                print(f"{pilote} : {valeur}")

        except Exception as e:
            print(e)


    def podiums_ecurie(gestion : Gestion_donnees, ecurie_choisi: Ecurie) -> dict:
        """permet de comptabiliser les podiums des pilotes de l'écurie

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            ecurie_choisi (Ecurie): écurie choisi par l'utilisateur

        Returns:
            dict: dictionnaire des pilotes et de leurs valeurs de podiums
        """

        results : dict = Analyse.pilotes_ecurie(gestion, ecurie_choisi)

        for course in gestion.lst_courses:

            podium = course.podium()

            for pilote in podium:

                if pilote.driver_id in results:

                    # vérifier l'écurie du pilote dans cette course
                    for resultat in course.lst_resultats:

                        if resultat.pilote.driver_id == pilote.driver_id and resultat.ecurie.nom == ecurie_choisi.nom:
                            results[pilote.driver_id] += 1

        return results
    

    def points_ecurie(gestion: Gestion_donnees, ecurie_choisi: Ecurie) -> dict:
        """permet de comptabiliser les points des pilotes de l'écurie

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            ecurie_choisi (Ecurie): écurie choisi par l'utilisateur

        Returns:
            dict: dictionnaire des pilotes et de leurs valeurs de points
        """
    

        results : dict = Analyse.pilotes_ecurie(gestion, ecurie_choisi)

        for course in gestion.lst_courses:

            for resultat in course.lst_resultats:

                pilote = resultat.pilote.driver_id

                if pilote in results and resultat.ecurie.nom == ecurie_choisi.nom:
                    results[pilote] += resultat.points

        return results
    

    def win_ecurie(gestion : Gestion_donnees, ecurie_choisi: Ecurie) -> dict:
        """permet de comptabiliser les wins des pilotes de l'écurie

        Args:
            gestion (Gestion_donnees): retourne le nombre de podium effectuer par le pilote en phrase
            ecurie_choisi (Ecurie): écurie choisi par l'utilisateur

        Returns:
            dict: dictionnaire des pilotes et de leurs valeurs de wins
        """

        results : dict = Analyse.pilotes_ecurie(gestion, ecurie_choisi)

        for course in gestion.lst_courses:

            pilote = course.vainqueur()

            if pilote.driver_id in results:

                # vérifier l'écurie du pilote dans cette course
                for resultat in course.lst_resultats:

                    if resultat.pilote.driver_id == pilote.driver_id and resultat.ecurie.nom == ecurie_choisi.nom:
                        results[pilote.driver_id] += 1

        return results
    
    def wc(gestion: Gestion_donnees) -> None:
        
        #initialisation
        dico_wc = {}
        lst_wc: list[list] = []
        
        #boucle pour faire toutes les saions
        for x in range(1950,2026):
            
            lst_lst = Analyse.points_saison(gestion, x)
            
            
            liste_trier = Analyse.tri(lst_lst)
            
            world_champion = liste_trier.pop()
                 
            lst_wc.append(world_champion)
            
        for pilote in lst_wc:

            nom = pilote[0]

            if nom in dico_wc:
                dico_wc[nom] += 1
                
            else:
                dico_wc[nom] = 1
                
        lst_de_lst : list[list] = list(dico_wc.items()) 
        
        liste_trier_wc = Analyse.tri(lst_de_lst)
        
        for driver in liste_trier_wc:
            
            print(driver)
            
    