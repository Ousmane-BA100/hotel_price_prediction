import pandas as pd
import numpy as np

# Charger les données actuelles
file_path = "data/df_merged.csv"
df_synthetic = pd.read_csv(file_path)

# Fixer la graine aléatoire pour la reproductibilité
np.random.seed(42)

# Générer les prix en tenant compte des facteurs influents
df_synthetic["price"] = (
    150  # Prix de base
    + df_synthetic["pool"] * 50  # Piscine = +50€
    + df_synthetic["parking"] * 30  # Parking = +30€
    + df_synthetic["stock"].apply(lambda x: max(0, 200 - x * 10))  # Moins de stock = prix plus élevé
    + np.random.normal(0, 50, df_synthetic.shape[0])  # Ajout de variabilité (écart-type de 50€)
)

# Appliquer une **plage de valeurs réaliste** (éviter les prix aberrants)
df_synthetic["price"] = df_synthetic["price"].clip(lower=70, upper=500)

# Sauvegarder le fichier avec les prix corrigés
new_file_path = "data/synthetic_pricing_data_calibrated.csv"
df_synthetic.to_csv(new_file_path, index=False)

print(f"✅ Prix calibrés et sauvegardés sous : {new_file_path}")
