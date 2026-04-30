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
for x in range(37): 
    meilleur_temps =Analyse.meilleur_temps_circuit(gestion)
    print()
    print(meilleur_temps)



#print(f"Le podium est:")
 #       print(f"{premier}🥇")
  #      print(f"{deuxieme}🥈")
   #     print(f"{troisieme}🥉")