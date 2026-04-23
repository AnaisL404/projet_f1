from pilote import Pilote
from ecurie import Ecurie

class Resultats:
    """Represente les résultats compris dans une course
    """


    def __init__(self, Pilote : Pilote, Ecurie : Ecurie, position : int, points : float, tours : int, statut : str, meilleur_tour : str):
        self.pilote = Pilote
        self.ecurie = Ecurie
        self._position = position
        self._points = points
        self._tours = tours
        self.statut = statut
        self.meilleur_tour = meilleur_tour

        self.position = position
        self.points = points
        self.tours = tours

    #setters getters pour les attributs protégés
    @property
    def position(self):
        return self._position
    
    @position.setter 
    def position(self, nouvelle_position : int):
        if nouvelle_position > 0:
            self._position = nouvelle_position
        elif nouvelle_position <= 0 :
            self._position = 1

    @property
    def points(self):
        return self._points
    
    @points.setter 
    def points(self, nouveau_points : float):
        if nouveau_points >= 0:
            self._points = nouveau_points
        elif nouveau_points < 0 :
            self._position = 0

    @property
    def tours(self):
        return self._tours
    
    @tours.setter 
    def tours(self, nouveau_tour : int):
        if nouveau_tour >= 0:
            self._tours = nouveau_tour
        elif nouveau_tour < 0 :
            self._tours = 0


    def a_fini(self) -> bool:
        """Permet de determiner si le pilote a terminer la course ou non

        Returns:
            bool: si oui ou non a fini
        """
        if self.statut == "Finished":
            return True
        else:
            return False
        
    def to_dict(self) -> dict:
        """Permet de convertir l'objet resultat sous forme de dictionnaire

        Returns:
            dict: le dictionnaire créé
        """
        return {
            "pilote" : self.pilote.to_dict(),
            "ecurie": self.ecurie.to_dict(),
            "position": self.position,
            "points": self.points,
            "tours" : self.tours,
            "statut" : self.statut,
            "meilleur_tour" : self.meilleur_tour
            }
