import joblib
import os
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# 📌 Définir le chemin du modèle
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model", "random_forest_model.pkl")

# 📌 Charger le modèle
try:
    print(f"🔍 Tentative de chargement du modèle depuis : {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)  # Utilisation du chemin absolu
    expected_features = model.feature_names_in_  # Vérifie les features attendues
    print(f"✅ Modèle chargé avec succès ! Features attendues : {expected_features}")
except Exception as e:
    print(f"❌ Erreur lors du chargement du modèle : {e}")
    model = None

# 📌 Encodage des variables catégoriques
city_encoding = {
    "amsterdam": 0,
    "paris": 1,
    "london": 2,
    "berlin": 3,
    "madrid": 4
}

def preprocess_input(data):
    """Transforme les données d'entrée pour correspondre au modèle."""
    df = pd.DataFrame([data])

    # 📌 Encodage des variables catégoriques
    city_encoding = {
        "amsterdam": 0,
        "copenhagen": 1,
        "madrid": 2,
        "paris": 3,
        "rome": 4,
        "sofia": 5,
        "valletta": 6,
        "vienna": 7,
        "vilnius": 8
    }

    language_encoding = {
        "Français (fr, lux, be)": 1,
        "Anglais (en, ir)": 2,
        "Espagnol/Portugais (es, pt)": 3,
        "Italien/Maltais (it, mt)": 4,
        "Allemand/Austro (de, at)": 5,
        "Europe de l'Est (ro, sk, hu, bg)": 6,
        "Pays Nordiques (da, sv, fi, no)": 7,
        "Grec (el, cy)": 8,
        "Balkans (hr, sl, sr, bs)": 9,
        "Europe Centrale (pl, cz)": 10,
        "Pays Baltes (et, lv, lt)": 11
    }

    brand_encoding = {
        "Sans marque": 0,
        "Marque économique": 1,
        "Marque intermédiaire": 2,
        "Marque haut de gamme": 3
    }

    group_encoding = {
        "Indépendant": 0,
        "Groupe International": 1,
        "Luxe": 2,
        "Économique": 3
    }

    # 📌 Vérifier si la ville est connue dans l'encodage
    if df["city_x"].iloc[0] in city_encoding:
        df["city_x"] = city_encoding[df["city_x"].iloc[0]]
    else:
        return None, f"❌ Ville inconnue : {df['city_x'].iloc[0]}"

    # 📌 Vérifier si la langue est connue dans l'encodage
    if df["language"].iloc[0] in language_encoding:
        df["language"] = language_encoding[df["language"].iloc[0]]
    else:
        return None, f"❌ Langue inconnue : {df['language'].iloc[0]}"

    # 📌 Vérifier si la marque d'hôtel est connue dans l'encodage
    if df["brand"].iloc[0] in brand_encoding:
        df["brand"] = brand_encoding[df["brand"].iloc[0]]
    else:
        return None, f"❌ Marque inconnue : {df['brand'].iloc[0]}"

    # 📌 Vérifier si le groupe d'hôtel est connu dans l'encodage
    if df["group"].iloc[0] in group_encoding:
        df["group"] = group_encoding[df["group"].iloc[0]]
    else:
        return None, f"❌ Groupe inconnu : {df['group'].iloc[0]}"

    # 📌 Vérifier les colonnes manquantes
    missing_cols = set(expected_features) - set(df.columns)
    if missing_cols:
        return None, f"❌ Colonnes manquantes après filtrage : {missing_cols}"

    # 📌 Réorganiser les colonnes pour correspondre au modèle
    df = df[expected_features]

    return df, None



@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "API is running"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        print("❌ Modèle non disponible")
        return jsonify({"error": "Modèle non disponible"}), 500

    data = request.get_json()
    print(f"📥 Données reçues : {data}")

    df_transformed, error = preprocess_input(data)

    if error:
        print(error)
        return jsonify({"error": error}), 400  # Mauvaise requête si la ville est inconnue ou colonnes manquantes

    print(f"📊 Données encodées pour la prédiction :\n{df_transformed}")

    try:
        # 📌 Faire la prédiction
        prediction = model.predict(df_transformed)[0]
        print(f"✅ Prédiction réussie : {prediction}")
        return jsonify({"predicted_price": prediction})
    except Exception as e:
        print(f"❌ Erreur interne : {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
