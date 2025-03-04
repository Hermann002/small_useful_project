import argparse
from gestion_depenses.gestionnaireDepenses import GestionnaireDepenses
import os
from .utils import get_user_dir

DATA_DIR = get_user_dir()

def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de depenses personnelles")
    parser.add_argument('action', choices=['ajouter', 'afficher', 'filtrer', 'tous'], help="Action à effectuer")
    parser.add_argument('--montant', type=float, help="Montant de la depense")
    parser.add_argument('--categorie', help="Categorie de la depense")
    parser.add_argument('--description', help="Description de la depense")
    parser.add_argument('--mois', help="Mois pour filtrer les depenses")

    args = parser.parse_args()

    gestionnaire = GestionnaireDepenses(f"{DATA_DIR}/depenses.csv")

    if args.action == 'ajouter':
        if not args.montant or not args.categorie:
            parser.error("L'argument --montant et --categorie sont requis pour ajouter une depense")
        gestionnaire.ajouter_depense(args.montant, args.categorie, args.description)
    elif args.action == 'afficher':
        gestionnaire.affiche_depenses()
    elif args.action == 'filtrer':
        if not args.categorie and not args.mois:
            parser.error("L'argument --categorie ou --mois est requis pour filtrer les depenses")
        gestionnaire.filtrer_depenses(args.categorie, args.mois)
    elif args.action == 'tous':
        gestionnaire.tous_afficher()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()