from resultats import Resultats
from pilote import Pilote

class Course:
    """represente les course d'une saison
    """
    def __init__(self, saison: int, date: str, nom_circuit: str, pays: str):
        self._saison = 0
        self.date = date
        self.nom_circuit = nom_circuit
        self.pays = pays
        self.lst_resultats : list[Resultats] = []

        self.saison = saison

    @property
    def saison(self) -> int:
        return self._saison
    
    @saison.setter
    def saison(self, saison: int) -> None:
        # une saison ne peut pas être négative
        if saison < 0:
            self._saison = 1
        else:
            self._saison = saison

    def ajouter_resultat(self, new_resultat:Resultats):
        self.lst_resultats.append(new_resultat)

    
    def __str__(self) -> str:
        """permet d'imprimer la course

        Returns:
            str: la course imprimer
        """
        return (f"{self.nom_circuit} - {self.pays} - {self.date} - Saison : {self.saison} - Nombre de résultats : {len(self.lst_resultats)}")

    
    def to_dict(self) -> dict:
        """permet de transformer la course en dictionnaire

        Returns:
            dict: retourne le dictionnaire de la course
        """
        lst_res_dico = []

        for res in self.lst_resultats:
            res_dico = res.to_dict()
            lst_res_dico.append(res_dico)

        return {
            "saison": self.saison,
            "date": self.date,
            "nom_circuit": self.nom_circuit,
            "pays": self.pays,
            "lst_resultats": lst_res_dico
        }
    
    def def_vainqueur(self) -> Pilote:
        for resultat in self.lst_resultats:
            if resultat.position == 1:
                vainqueur = resultat.pilote

        return vainqueur
    
    def podium(self) -> list:
        for resultat in self.lst_resultats:
            if resultat.position == 1:
                premier = resultat.pilote
            if resultat.position == 2:
                deuxieme = resultat.pilote
            if resultat.position == 3:
                troisieme = resultat.pilote
        lst_podium = [premier, deuxieme, troisieme]
        return lst_podium
