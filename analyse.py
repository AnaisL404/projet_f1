import matplotlib.pyplot as plt
from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie

class Analyse:
    

    def circuit_plus_longtemps(gestion : Gestion_donnees):
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
    
        
        


    def meilleur_temps_circuit(gestion: Gestion_donnees):
        # boucle pour voir les afficher les nom de circuit et pouvoir choisir le circuit voulu
        liste_circuit = []
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

        #comparer les temps
        best_lap_min = 10000
        best_lap_sec = 10000
        best_lap_milli = 10000
        for course in gestion.lst_courses:
            if course.nom_circuit == circuit_str.nom_circuit:
                for resultat in course.lst_resultats:
                    if resultat.meilleur_tour != 0:
                        minutes_str, reste = resultat.meilleur_tour.split(":")
                        secondes_str, millisecondes_str = reste.split(".")


                        min= int(minutes_str)
                        sec = int(secondes_str)
                        milli = int(millisecondes_str)
                        
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

        if len(str(best_lap_milli)) == 2:
            best_lap_milli = f"0{best_lap_milli}"
        if len(str(best_lap_milli)) == 1:
            best_lap_milli = f"00{best_lap_milli}"

        meilleur_temps = (f"{best_lap_min}:{best_lap_sec}.{best_lap_milli}")

        
        return (f"Le meilleur temps à été réaliser par {pilote} en {annee} et est de {meilleur_temps}")


    def plus_de_podium(gestion : Gestion_donnees, pilote_choisi: Pilote):

        nb_podium = 0
        for course in gestion.lst_courses:
            podium = course.podium()
            podium_nom = [podium[0].driver_id, podium[1].driver_id, podium[2].driver_id,]
            if pilote_choisi.driver_id in podium_nom:
                nb_podium += 1
        return f"Le pilote {pilote_choisi} à fait {nb_podium} podiums dans sa carrière"
        
    def plus_de_win(gestion : Gestion_donnees, pilote_choisi: Pilote):

        nb_win = 0
        for course in gestion.lst_courses:
            if pilote_choisi.driver_id == course.vainqueur().driver_id:
                nb_win += 1
        return f"Le pilote {pilote_choisi} à fait {nb_win} podiums dans sa carrière"

    

    def pourcentage_win_saison(gestion : Gestion_donnees, saison_voulue : int):
        courses_saison = []
        for course in gestion.lst_courses:
            if course.saison == saison_voulue:
                courses_saison.append(course)

        winners = []
        nb_wins = []
        for course in courses_saison:
            for resultat in course.lst_resultats:
                if resultat.position == 1:
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

    ## les trier pour quil en ordre!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def points_saison(gestion : Gestion_donnees, saison_voulue : int):
        courses_saison = []
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
        
        for pilote in results:
            print(f"{pilote} : {results[pilote]} points")
        



                
    def points_pilotes_ecurie(gestion : Gestion_donnees, ecurie_choisi: Ecurie):
        #mettre tous les pilotes qui ont été dans l'écurie choisi
        lst_pilotes = []
        liste_nom = []
        for course in gestion.lst_courses:
           for resultat in course.lst_resultats:
               if resultat.ecurie.nom == ecurie_choisi.nom:
                    if resultat.pilote.driver_id not in liste_nom:
                       lst_pilotes.append(resultat)
                       liste_nom.append(resultat.pilote.driver_id)
                    else:
                        lst_pilotes.append(resultat)

        results = {}
        for resultat in lst_pilotes:
            if resultat.pilote.driver_id in results:
                results[resultat.pilote.driver_id] += resultat.points
            else:
                results[resultat.pilote.driver_id] = resultat.points
        
        for pilote in results:
            print(f"{pilote} : {results[pilote]} points")

        return lst_pilotes
        
