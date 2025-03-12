import streamlit as st
import requests

# URL de l'API Flask
API_URL = "http://localhost:5000/predict"  # Change l'URL si nécessaire

# Configuration de la page
st.set_page_config(page_title="🏨 Prédiction du Prix d'une nuit des Hôtels", layout="centered")

st.title("🏨 Prédiction du Prix des Hôtels")
st.markdown("Saisissez les informations ci-dessous pour obtenir une estimation du prix d'une nuit.")

# 📍 **Ville (Affichage avec noms clairs)**
city_mapping = {
    "Amsterdam": "amsterdam",
    "Copenhague": "copenhagen",
    "Madrid": "madrid",
    "Paris": "paris",
    "Rome": "rome",
    "Sofia": "sofia",
    "La Valette": "valletta",
    "Vienne": "vienna",
    "Vilnius": "vilnius"
}
city_label = st.selectbox("📍 Ville", list(city_mapping.keys()))
city_x = city_mapping[city_label]  # Convertir en code attendu par l'API

# 📅 **Jour de réservation**
date = st.slider("📅 Jour de réservation (ex: J-10 avant la date souhaitée)", min_value=0, max_value=40, value=10)

# 🌐 **Langue**
language_mapping = {
    "Français": 1,
    "Anglais": 2,
    "Espagnol": 3,
    "Italien": 4,
    "Allemand": 5
}
language_label = st.selectbox("🌐 Langue du client", list(language_mapping.keys()))
language = language_mapping[language_label]  # Convertir en code

# 📲 **Réservation via mobile ou ordinateur**
mobile_mapping = {
    "📱 Mobile": 1,
    "💻 Ordinateur": 0
}
mobile_label = st.radio("📲 Réservé via", list(mobile_mapping.keys()))
mobile = mobile_mapping[mobile_label]

# 🏨 **Stock de chambres disponibles**
stock = st.number_input("🏨 Nombre de chambres disponibles", min_value=0, value=10)

# 🏢 **Groupe d'hôtel**
group_mapping = {
    "Indépendant": 0,
    "Groupe International": 1,
    "Luxe": 2,
    "Économique": 3
}
group_label = st.selectbox("🏢 Groupe d'hôtel", list(group_mapping.keys()))
group = group_mapping[group_label]

# 🏷 **Marque d'hôtel**
brand_mapping = {
    "Sans marque": 0,
    "Marque économique": 1,
    "Marque intermédiaire": 2,
    "Marque haut de gamme": 3
}
brand_label = st.selectbox("🏷 Marque d'hôtel", list(brand_mapping.keys()))
brand = brand_mapping[brand_label]

# Ajout de styles CSS pour forcer les labels à rester sur une seule ligne
st.markdown(
    """
    <style>
    .stRadio div[role="radiogroup"] label {
        display: inline-flex;
        align-items: center;
        gap: 5px; /* Espacement entre le bouton et le texte */
        white-space: nowrap; /* Empêcher le retour à la ligne */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🔹 Créer trois colonnes pour aligner les options
col1, col2, col3 = st.columns([1, 1, 1.5])  # Ajustement des largeurs

# 🚗 Parking disponible
with col1:
    parking_mapping = {"❌ Non": 0, "✅ Oui": 1}
    parking_label = st.radio("🚗 Parking disponible ?", list(parking_mapping.keys()), horizontal=True)
    parking = parking_mapping[parking_label]

# 🏊 Piscine disponible
with col2:
    pool_mapping = {"❌ Non": 0, "✅ Oui": 1}
    pool_label = st.radio("🏊 Piscine disponible ?", list(pool_mapping.keys()), horizontal=True)
    pool = pool_mapping[pool_label]

# 👶 Politique enfants
with col3:
    children_policy_mapping = {
        "👶 Non accepté": 0,
        "👦 Accepté avec restrictions": 1,
        "👨‍👩‍👧 Accepté sans restrictions": 2
    }
    children_policy_label = st.radio("👶 Politique enfants", list(children_policy_mapping.keys()), horizontal=True)
    children_policy = children_policy_mapping[children_policy_label]

# 🔥 **Envoyer les données à l'API Flask**
if st.button("🚀 Prédire le prix"):
    input_data = {
        "order_requests": 10,  # Valeur par défaut pour l'instant
        "city_x": city_x,
        "date": date,
        "language": language,
        "mobile": mobile,
        "stock": stock,
        "group": group,
        "brand": brand,
        "parking": parking,
        "pool": pool,
        "children_policy": children_policy
    }

    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        predicted_price = response.json()["predicted_price"]
        st.success(f"💰 Prix estimé : **{predicted_price} €**")
    else:
        st.error(f"❌ Erreur dans la prédiction. Message : {response.json()}")
