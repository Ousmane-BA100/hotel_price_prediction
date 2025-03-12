from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Initialiser l'application Flask
app = Flask(__name__)

# Charger le modèle sauvegardé
model_path = "model/random_forest_model.pkl"  # Mets le bon nom de ton fichier modèle
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("✅ Modèle chargé avec succès !")
else:
    print("❌ Erreur : Modèle introuvable ! Vérifie le chemin.")

# Définition de la route de test
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API de prédiction des prix d'hôtels est en ligne 🚀"})

# Route pour faire des prédictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Récupérer les données JSON
        print("📥 Données reçues :", data)  # DEBUG : Afficher les données reçues dans le terminal
        
        df_input = pd.DataFrame([data])  # Convertir en DataFrame
        
        # Supprimer les colonnes inutiles si elles sont présentes
        columns_to_remove = ["hotel_id", "avatar_id", "price"]
        df_input = df_input.drop(columns=[col for col in columns_to_remove if col in df_input], errors='ignore')

        print("📊 Données transformées :", df_input)  # DEBUG : Afficher le DataFrame après transformation

        # Encodage de la colonne city_x
        cities = ["amsterdam", "copenhagen", "madrid", "paris", "rome", "sofia", "valletta", "vienna", "vilnius"]
        df_input["city_x"] = df_input["city_x"].apply(lambda x: cities.index(x) if x in cities else -1)

        print("📊 Données encodées pour la prédiction :", df_input)  # DEBUG

        # Faire la prédiction
        prediction = model.predict(df_input)
        
        # Retourner le résultat
        return jsonify({"predicted_price": round(prediction[0], 2)})

    except Exception as e:
        print("❌ Erreur :", str(e))  # DEBUG : Afficher l'erreur détaillée
        return jsonify({"error": str(e)}), 400

# Lancer l'application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
