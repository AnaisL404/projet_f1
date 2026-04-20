class Ecurie:
    def __init__(self, nom: str, nationalite: str):
        self.nom = nom
        self.nationalite = nationalite

    def to_dict(self) -> dict:
        """permet de transformer l'écurie en dictionnaire

        Returns:
            dict: retourne le dictionnaire de l'écurie
        """
        return {
            "nom": self.nom,
            "nationalite": self.nationalite
        }
    
    def __str__(self) -> str:
        """permet d'imprimer l'écurie

        Returns:
            str: l'écurie imprimer
        """
        return(f"Le nom de l'écurie est {self.nom} et sa nationalité est {self.nationalite}")
        