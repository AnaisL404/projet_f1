class Saison:
    def __init__(self, annee: int, nb_courses: int, nb_pilotes: int):
        self._annee = 0
        self._nb_courses = 0
        self._nb_pilotes = 0

        #innitialisation des données
        self.annee = annee
        self.nb_courses = nb_courses
        self.nb_pilotes = nb_pilotes

    @property
    def annee(self) -> int:
        return self._annee
    
    @annee.setter
    def annee(self, annee: int) -> None:
        # le annee ne peut pas être plus petit que 1950 ni plus grand que 2025
        if annee <= 1950:
            self._annee = 1950
        elif annee > 2025:
            self.annee = 2025
        else:
            self._annee = annee

    @property
    def nb_courses(self) -> int:
        return self._nb_courses
    
    @nb_courses.setter
    def nb_courses(self, nb_courses: int) -> None:
        # le nb_courses ne peut pas être plus petit que 0
        if nb_courses <= 0:
            self._nb_courses = 0
        else:
            self._nb_courses = nb_courses

    @property
    def nb_pilotes(self) -> int:
        return self._nb_pilotes
    
    @nb_pilotes.setter
    def nb_pilotes(self, nb_pilotes: int) -> None:
        # le nb_pilotes ne peut pas être plus petit que 0
        if nb_pilotes <= 0:
            self._nb_pilotes = 0
        else:
            self._nb_pilotes = nb_pilotes