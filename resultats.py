class Resultats:
    """Represente les résultats compris dans une course
    """


    def __init__(self, Pilote : object, Ecurie : object, position : int, points : float, tours : int, statut : str, temps : str, meilleur_tour : str, vitesse_moy : float):
        self.pilote = Pilote
        self.ecurie = Ecurie
        self._position = position
        self._points = points
        self._tours = tours
        self.statut = statut
        self.temps = temps
        self.meilleur_tour = meilleur_tour
        self._vitesse_moy = vitesse_moy

        self.position = position
        self.points = points
        self.tours = tours
        self.vitesse_moy = vitesse_moy

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

    @property
    def vitesse_moy(self):
        return self._vitesse_moy
    
    @vitesse_moy.setter 
    def vitesse_moy(self, nouvelle_vit : float):
        if nouvelle_vit >= 0:
            self._vitesse_moy = nouvelle_vit
        elif nouvelle_vit < 0 :
            self._vitesse_moy = 0


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
            "pilote" : self.pilote,
            "ecurie": self.ecurie,
            "position": self.position,
            "points": self.points,
            "tours" : self.tours,
            "statut" : self.statut,
            "temps" : self.temps,
            "meilleur_tour" : self.meilleur_tour,
            "vitesse_moy" : self.vitesse_moy
            }

    #def from_dict()