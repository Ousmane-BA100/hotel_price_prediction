# 📌 Projet : Prédiction des Prix des Hôtels 🏨

Bienvenue dans ce projet de **prédiction des prix des hôtels** ! Ce projet utilise **l'apprentissage automatique** pour estimer les prix des chambres en fonction de plusieurs caractéristiques des hôtels et des réservations.

---

## 📂 Structure du Projet

```
📂 hotel_price_prediction/
│── data/                   # Données du projet
│   ├── features_hotels.csv       # Caractéristiques des hôtels
│   ├── synthetic_data.csv        # Données de prix simulées
│   ├── test_set.csv              # Données de test
│── model.py                # Script d'entraînement et d'évaluation du modèle
│── preprocess.py            # Prétraitement des données
│── generate_data.py         # Génération des données artificielles
│── predict.py               # Faire des prédictions
│── requirements.txt         # Dépendances du projet
│── README.md                # Explication du projet
```

---

## 🛠️ Installation

1️⃣ **Cloner le projet**
```bash
git clone https://github.com/votre-repo/hotel_price_prediction.git
cd hotel_price_prediction
```

2️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

---

## 📊 Données

Les données utilisées comprennent :
✅ `features_hotels.csv` : Informations sur les hôtels (groupe, marque, ville, équipements, etc.)
✅ `synthetic_data.csv` : Données de prix générées si l'API n'est pas accessible
✅ `test_set.csv` : Données de test à prédire

---

## 🚀 Utilisation

### 🔹 **1. Générer des données artificielles (si besoin)**
```bash
python generate_data.py
```

### 🔹 **2. Prétraiter les données**
```bash
python preprocess.py
```

### 🔹 **3. Entraîner le modèle**
```bash
python model.py
```

### 🔹 **4. Faire des prédictions**
```bash
python predict.py
```

Les prédictions sont enregistrées dans `predictions.csv`.

---

## 🎯 Objectif

L'objectif du projet est de **prédire les prix des hôtels** à partir de leurs caractéristiques et des informations de réservation. Le modèle de machine learning est évalué à l'aide de **l'erreur quadratique moyenne (RMSE)**.

---

## 📌 Modèles utilisés

- Régression Linéaire 🤖
- Random Forest 🌲
- XGBoost ⚡

Le modèle avec la **meilleure RMSE** sera sélectionné pour la soumission finale.

---

## 🏆 Améliorations possibles

🔹 Collecte de plus de données réelles 📡  
🔹 Test de modèles avancés comme LightGBM 🔥  
🔹 Optimisation des hyperparamètres avec GridSearchCV 🔍  

---

## 🤝 Contributions

Les contributions sont les bienvenues ! Merci de proposer des améliorations via des **issues** ou **pull requests** sur GitHub.

📩 **Contact :** Si vous avez des questions, n'hésitez pas à me contacter ! 😊

