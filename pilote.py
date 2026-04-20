class Pilote:
    """Represente un pilote de F1
    """
    def __init__(self, driver_id: str, prenom: str, nom: str, nationalite: str, date_naissance: str):
        self.driver_id = driver_id
        self.prenom = prenom
        self.nom = nom
        self.nationalite = nationalite
        self.date_naissance = date_naissance

    def to_dict(self) -> dict:
        """permet de transformer le pilote en dictionnaire

        Returns:
            dict: retourne le dictionnaire du pilote
        """
        return {
            "driver_id": self.driver_id,
            "prenom": self.prenom,
            "nom": self.nom,
            "nationalite": self.nationalite,
            "date_naissance": self.date_naissance
        }
    
    def age(self) -> int:
        annee = int(self.date_naissance[0:4])

        age = 2025 - annee

        return age