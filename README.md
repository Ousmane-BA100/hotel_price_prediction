# 📌 Projet : Prédiction des Prix des Hôtels 🏨

Bienvenue dans ce projet de **prédiction des prix des hôtels** ! Ce projet utilise **l'apprentissage automatique** pour estimer les prix des chambres en fonction de plusieurs caractéristiques des hôtels et des réservations.

Nous avons également ajouté une **API Flask** et une **interface Streamlit** pour permettre aux utilisateurs d'effectuer des prédictions en temps réel. Le projet est déployable avec **Docker** et **Docker Compose** pour faciliter son utilisation et sa mise en production.

---

## 📌 Table des matières
- [🔧 Prérequis](#prérequis)
- [📂 Structure du projet](#structure-du-projet)
- [📥 Installation](#installation)
- [🚀 Exécution](#exécution)
- [🖱️ Utilisation](#utilisation)
- [🛠️ Technologies utilisées](#technologies-utilisées)
- [👨‍💻 Auteurs](#auteurs)
- [📜 Licence](#licence)
- [🤝 Contribuer](#contribuer)
- [❓ Questions ou problèmes](#questions-ou-problèmes)

---

## 🔧 Prérequis
Avant de commencer, assurez-vous d'avoir installé :
- Python 3.x 🐍
- Docker 🐳 (optionnel pour le déploiement)
- Git 🛠️

---

## 📂 Structure du Projet

```
📂 hotel_price_prediction/
│── data/                   # Données du projet
│   ├── features_hotels.csv       # Caractéristiques des hôtels
│   ├── synthetic_data.csv        # Données de prix simulées
│   ├── test_set.csv              # Données de test
│── model.py                # Script d'entraînement et d'évaluation du modèle
│── preprocess.ipynb            # Prétraitement des données
│── generate_data.py        # Génération des données artificielles
│── predict.ipynb               # Faire des prédictions
│── backend/                 # Dossier du backend (API Flask)
│   ├── Dockerfile 📄         # Dockerfile pour l'API
│   ├── backend_api.py 🖥️      # Code source de l'API
│   ├── requirements.txt 📜   # Dépendances Python
│   └── model/ 📁  # Modèle de prédiction
│── frontend/                # Dossier du frontend (Streamlit)
│   ├── Dockerfile 📄         # Dockerfile pour le frontend
│   ├── frontend.py 🎨        # Interface utilisateur
│   └── requirements.txt 📜   # Dépendances Streamlit
│── docker-compose.yml ⚙️     # Configuration Docker Compose
│── requirements.txt         # Dépendances du projet
│── README.md                # Explication du projet
```

---

## 📥 Installation

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

## 🚀 Exécution

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

## 🖱️ Utilisation

Ce projet permet de **prédire les prix des hôtels** en fonction des caractéristiques de l'hôtel et des conditions de réservation.

1. **Chargez les données**.
2. **Entraînez le modèle**.
3. **Générez des prédictions** pour de nouveaux hôtels.
4. **Déployez l'API et l'interface utilisateur**.

---

## 🛠️ Technologies utilisées

Ce projet utilise les technologies suivantes :

- **Python** 🐍 (scikit-learn, pandas, numpy)
- **Flask** 🔥 (pour le backend API)
- **Streamlit** 🎨 (pour le frontend interactif)
- **Docker & Docker Compose** 🐳 (pour le déploiement)
- **Git & GitHub** 🛠️ (pour la gestion du projet)

---

## 👨‍💻 Auteurs
 
👨‍💻 **Ousmane BA** : Développeur principal  

---

## 📜 Licence

Ce projet est sous licence **MIT**. Voir le fichier `LICENSE` pour plus de détails.

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! 🚀 Pour contribuer :

1. **Forkez le projet** 🍴.
2. **Créez une branche** :
   ```bash
   git checkout -b feature/NouvelleFonctionnalité
   ```
3. **Committez vos modifications** :
   ```bash
   git commit -m "Ajout d'une nouvelle fonctionnalité"
   ```
4. **Poussez vers la branche** :
   ```bash
   git push origin feature/NouvelleFonctionnalité
   ```
5. **Ouvrez une Pull Request** 📬.

---

## ❓ Questions ou problèmes ?

Si vous avez des questions, ouvrez une **issue** sur GitHub ou contactez-moi 📩 à **bousmane733@gmail.com**.

🚀 **Bon travail et bon entraînement !** 😊

