import streamlit as st

st.set_page_config(page_title="ℹ️ Description de l'Application", layout="centered")

st.title("ℹ️ Description de l'Application")
st.markdown("""
Bienvenue dans l'application de prédiction des prix d'une nuit des hôtels ! 🏨✨

### **📌 Objectif**
Cette application utilise un modèle de **Machine Learning** pour prédire le prix d'une nuit d'hôtel en fonction de divers facteurs :
- 📍 **Ville** de réservation
- 📅 **Jour de la réservation**
- 🌐 **Langue du client**
- 📲 **Réservation sur mobile ou non**
- 🏢 **Groupe et marque de l'hôtel**
- 🚗 **Parking disponible**
- 🏊 **Piscine disponible**
- 👶 **Politique enfants**
- 📈 **Nombre de demandes et stock de chambres disponibles**

### **⚙️ Comment ça fonctionne ?**
1. **Saisissez vos informations** sur la page principale.
2. **L'API Flask** envoie ces données à un modèle de Machine Learning.
3. **Le modèle prédit le prix** en fonction des caractéristiques de l'hôtel et du marché.
4. **Le prix estimé s'affiche** directement sur votre écran !

🎯 *Prêt à tester ? Rendez-vous sur la page principale !*
""")
