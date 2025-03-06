import argparse
from gestion_depenses.gestionnaireDepenses import GestionnaireDepenses
import os
from .utils import get_user_dir

DATA_DIR = get_user_dir()

def main():
    parser = argparse.ArgumentParser(description="Personal expense manager")
    parser.add_argument('actions', choices=['add', 'print', 'filter', 'all'], help="Action to be taken")
    parser.add_argument('--amount', type=float, help="Expense amount")
    parser.add_argument('--cat', help="Expense category")
    parser.add_argument('--desc', help="Expense description")
    parser.add_argument('--mounth', help="Months to filter expenses")

    args = parser.parse_args()

    gestionnaire = GestionnaireDepenses(f"{DATA_DIR}/depenses.csv")

    if args.action == 'add':
        if not args.montant or not args.categorie:
            parser.error("L'argument --montant et --categorie sont requis pour ajouter une depense")
        gestionnaire.ajouter_depense(args.montant, args.categorie, args.description)
    elif args.action == 'print':
        gestionnaire.affiche_depenses()
    elif args.action == 'filter':
        if not args.categorie and not args.mois:
            parser.error("The --cat or --month argument is required to filter expenses.")
        gestionnaire.filtrer_depenses(args.categorie, args.mois)
    elif args.action == 'all':
        gestionnaire.tous_afficher()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()