from resultats import Resultats

class Course:
    def __init__(self, saison: int, date: str, nom_circuit: str, pays: str):
        self._saison = 0
        self.date = date
        self.nom_circuit = nom_circuit
        self.pays = pays
        self.lst_resultas : list[Resultats] = []

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
