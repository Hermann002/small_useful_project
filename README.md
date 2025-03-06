# petit projets cools et utiles
## password generator
Ce programme te permet de générer tes mots de passes et les stokers dans un fichier markdown <br>
**prerequis**
- `python`
- `pip`

**Comment utiliser**:
- `cd password_generator` --> `python main.py`<br>
ou
- `pip install -e .` --> `genetor-password`

## gestion des dépenses
Ce programme vous permet de suivre en temps réel vos dépenses journalière.
si vous trouvez les interfaces chiantes et peu fiables, ceci est pour vous.
**prerequis**
- `python`
- `pip`

**intallation**
- `git clone <lien de la repo>`
- `cd gestion_depenses` --> `pip install -e .`

**utilisation**
depense [-h] [--amount AMOUNT] [--cat CAT] [--desc DESC] [--mounth MOUNTH] {add,print,filter,all}

Personal expense manager

positional arguments:<br>
  - {add,print,filter,all} *Action to be taken*

options:<br>
| commande | function | description |
|-----|-------------|---------------|
  |-h, --help |HELP            |show this help message and exit|
  |--amount| AMOUNT       |Expense amount|
  |--cat |CAT           |Expense category|
  |--desc |DESC           |Expense description
  |--mounth |MOUNTH       |Months to filter expenses

*example*: <br>
- ajouter une depense: `expense add --amount 2000 --cat repas --desc "un bon plat d'okok sans pipi à l'intérieur"`

- afficher tous: `expense all`