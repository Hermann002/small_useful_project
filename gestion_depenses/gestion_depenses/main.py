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
    parser.add_argument('--month', help="Months to filter expenses")

    args = parser.parse_args()

    gestionnaire = GestionnaireDepenses(f"{DATA_DIR}/depenses.csv")

    if args.actions == 'add':
        if not args.amount or not args.cat:
            parser.error("L'argument --montant et --categorie sont requis pour ajouter une depense")
        gestionnaire.ajouter_depense(args.amount, args.cat, args.desc)
    elif args.actions == 'print':
        gestionnaire.affiche_depenses()
    elif args.actions == 'filter':
        if not args.cat and not args.month:
            parser.error("The --cat or --month argument is required to filter expenses.")
        gestionnaire.filtrer_depenses(args.cat, args.month)
    elif args.actions == 'all':
        gestionnaire.tous_afficher()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()