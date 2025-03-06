from gestion_depenses.depense import Depense
import os
import csv
from datetime import datetime
import pandas as pd

class GestionnaireDepenses():
    
    def __init__(self, file:str):
        self.file = file
        self.depenses = self.charger_depenses()

    def charger_depenses(self):
        print("loading of expenses...")
        if not os.path.exists(self.file):
            return []
        
        with open(self.file, 'r') as f:
            reader = csv.DictReader(f)
            depenses = [Depense(d["date"], float(d["montant"]), d["categorie"], d["description"]) for d in reader]
            return depenses
        
    def sauvegarder_depenses(self):
        """Sauvegarde les dépenses dans le fichier CSV en mode ajout."""
        file_exists = os.path.exists(self.file)
        print(f"file exist ? {file_exists}")
        depense = self.depenses

        if not file_exists:
            with open(self.file, 'w', newline='') as f: 
                fieldnames = ['date', 'montant', 'categorie', 'description']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({
                    'date': depense.date,
                    'montant': depense.montant,
                    'categorie': depense.categorie,
                    'description': depense.description
                })
        else:
            with open(self.file, 'a', newline='') as f: 
                fieldnames = ['date', 'montant', 'categorie', 'description']
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writerow({
                    'date': depense.date,
                    'montant': depense.montant,
                    'categorie': depense.categorie,
                    'description': depense.description
                })

    def ajouter_depense(self, montant:float, categorie:str, description:str):
        depense = Depense(date=datetime.now().strftime('%Y-%m-%d'), montant=montant, categorie=categorie, description=description)
        self.depenses = depense
        self.sauvegarder_depenses()
        print(f"new expense added")

    def affiche_depenses(self):
        if not self.depenses:
            print("No expenses recorded")
            return
        
        total = sum(depense.montant for depense in self.depenses)
        print(f"total expenses: {total} XAF")

        categories = {}
        for depense in self.depenses:
            if depense.categorie not in categories:
                categories[depense.categorie] = 0
            categories[depense.categorie] += depense.montant

        for categorie, total in categories.items():
            print(f"{categorie}: {total} XAF")

    def filtrer_depenses(self, categorie:str, mois=None):
        depenses_filtrees = self.depenses
        if categorie:
            depenses_filtrees = [depense for depense in depenses_filtrees if depense.categorie == categorie]
        if mois:
            depenses_filtrees = [depense for depense in depenses_filtrees if datetime.strptime(depense.date, "%Y-%m-%d").strftime("%Y-%m") == mois]
        
        if not depenses_filtrees:
            print("No expenses found")
        else: 
            print(f"expenses for category {categorie} in the month of {mois}")
            for depense in depenses_filtrees:
                print(depense)

    def tous_afficher(self):
        depense = pd.read_csv(self.file, encoding="ISO-8859-1")
        print(depense)