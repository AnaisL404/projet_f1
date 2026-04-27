from gestion_donnees import Gestion_donnees
from resultats import Resultats
from course import Course
from pilote import Pilote
from ecurie import Ecurie
from analyse import Analyse



gestion = Gestion_donnees()


gestion.collecter_donnee()


meilleur_temps =Analyse.meilleur_temps_circuit(gestion)
print(meilleur_temps)
Analyse.circuit_plus_longtemps(gestion)


#print(f"Le podium est:")
 #       print(f"{premier}🥇")
  #      print(f"{deuxieme}🥈")
   #     print(f"{troisieme}🥉")