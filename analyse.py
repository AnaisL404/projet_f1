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
    
        return liste_10_max, liste_nb_apparitions
        


    def meilleur_temps_circuit(gestion: Gestion_donnees):
        # boucle pour voir les afficher les nom de circuit et pouvoir choisir le circuit voulu
        liste_circuit = []
        for course in gestion.lst_courses:
            if course.nom_circuit not in liste_circuit:
                liste_circuit.append(course.nom_circuit)

        index = 0
        for course in liste_circuit:
            print(f"{index}. {course}")
            index += 1
        try:
            print()
            circuit_int = int(input("Entrez le numéro du circuit voulu :"))
            circuit_str = gestion.lst_courses[circuit_int]

        except:
            print("Choix du circuit out of range")

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
                        elif min == best_lap_min:
                            if sec < best_lap_sec:
                                best_lap_sec = sec
                                best_lap_milli = milli
                            elif sec == best_lap_sec:
                                if milli < best_lap_milli:
                                    best_lap_milli = milli

        meilleur_temps = (f"{best_lap_min}:{best_lap_sec}.{best_lap_milli}")
        return meilleur_temps



    