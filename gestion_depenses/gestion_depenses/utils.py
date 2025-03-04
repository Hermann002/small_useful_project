from appdirs import user_data_dir
import os
import pandas as pd

def get_user_dir():
    data_dir = user_data_dir("depenses")
    try:
        os.makedirs(data_dir, exist_ok=True)
    except PermissionError:
        raise PermissionError(f"Impossible de créer le dossier {data_dir}. Vérifiez les permissions.")
    return data_dir