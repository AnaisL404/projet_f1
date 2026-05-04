from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse



gestion = Gestion_donnees()
#1,2,7,26,29,33

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



Analyse.pilotes_ecurie(gestion, ecurie_str)


        
    




