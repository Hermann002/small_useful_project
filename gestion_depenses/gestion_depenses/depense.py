class Depense():
    def __init__(self, date, montant, categorie, description):
        self.date = date
        self.montant = montant
        self.categorie = categorie
        self.description = description

    def __str__(self):
        return f"{self.date} - {self.montant} XAF - {self.categorie} - {self.description}"

    def __repr__(self):
        return self.__str__()