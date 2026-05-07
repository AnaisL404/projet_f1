from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse



gestion = Gestion_donnees()

gestion.collecter_donnee()

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

Analyse.top3_points_ecurie(gestion, ecurie_str)


# 1. calcul des points (filtrage + somme)
#results = Analyse.points_ecurie(gestion, ecurie_str)

# 2. tri + affichage top 3
#Analyse.afficher_top3(results)
    """j'ai essayer de faire les truc d'écurie en def séparer mais pour l'instant j'ai juste tous les points que les pilotes ont fait dans
        leur carrière
    """
    





