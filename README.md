# 📌 Projet : Prédiction des Prix des Hôtels 🏨

## 📊 Présentation du Dataset  
Le dataset utilisé dans ce projet combine des données réelles et des données simulées :  

📍 **Caractéristiques des hôtels** (`features_hotels.csv`) : localisation, marque, parking, piscine, politique enfants.  
🏨 **Informations sur les réservations** (`test_set.csv`) : ville, date, langue du client, mobile ou non, stock de chambres.  
💰 **Prix des hôtels** (`synthetic_data.csv`) : valeur cible à prédire, générée artificiellement.  

Les caractéristiques des hôtels et les informations sur les réservations proviennent de **données fournies**, tandis que les **prix sont générés artificiellement** afin de simuler un scénario réaliste et entraîner un modèle de Machine Learning.  

---
## 🎯 Stratégie pour générer des prix réalistes

### 📌 Objectif :
- Prix moyen autour de **200-300 €**.
- Minimum autour de **70 €**, maximum autour de **500 €** (éviter les valeurs extrêmes).

### 🔍 Facteurs influençant le prix :
- **Stock bas** → Prix plus élevés.
- **Piscine, parking, marque d'hôtel** → Ajoutent une valeur au prix.
- **Variabilité aléatoire contrôlée** pour éviter les valeurs trop extrêmes.

---

## 🏥 Contexte  
La **DGCCRF** d’un pays imaginaire a reçu des plaintes sur l’agence en ligne **1001NightsHotels.com**, suspectée de pratiquer des **prix à la tête du client**.  
L’objectif est d’analyser le système de tarification de cette agence et de vérifier s’il existe des **irrégularités**.  

Cependant, comme les prix réels ne sont pas disponibles, nous avons choisi de **les générer artificiellement** en nous basant sur des tendances observées dans le secteur hôtelier.  

---

## 🎯 Objectif du projet  
L'objectif est de :  

✅ **Analyser les facteurs influençant les prix** des hôtels.  
✅ **Générer des prix artificiels** pour entraîner un modèle de prédiction.  
✅ **Développer un modèle de Machine Learning** capable d'estimer les prix des hôtels avec précision.  
✅ **Déployer une API Flask et une interface utilisateur** avec Streamlit pour des prédictions en temps réel.    

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
│── model.ipynb                # Script d'entraînement et d'évaluation du modèle
│── preprocess.ipynb            # Prétraitement des données
│── generate_data.py        # Génération des données artificielles
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
## 📦 Backend (API Flask)

Le **backend** est développé en **Flask** et expose une API permettant de faire des prédictions de prix d’hôtels à partir de caractéristiques fournies en entrée.

### 📌 Fonctionnalités :
- Une **route `/predict`** qui prend un JSON en entrée et retourne une prédiction.
- Chargement du modèle de **Machine Learning** entraîné.
- Prétraitement des données avant la prédiction.

### 🚀 Exécuter le backend avec Docker :

```bash
cd backend
docker build -t hotel_price_backend .
docker run -p 5000:5000 hotel_price_backend
```

## 🚀 Exécuter avec Docker Compose

### 📌 Commande pour démarrer les services :
```bash
docker-compose up --build
```
 🌍 Accès aux services :
📌 API Flask (Local) : http://localhost:5000
📌 API Flask (Déployé sur AWS) : http://EC2_PUBLIC_IP:5000

---

## 🎨 Frontend (Streamlit)

Le **frontend** est développé avec **Streamlit** pour fournir une interface utilisateur simple et interactive permettant d’interagir avec l’API.

### 📌 Fonctionnalités :
- Interface permettant aux utilisateurs d’entrer des caractéristiques d’un hôtel.
- Envoi de ces caractéristiques à l’API Flask pour obtenir une prédiction.
- Affichage des prix estimés.

---
## ✅ Tests Automatisés

Le projet inclut des tests unitaires et d’intégration pour assurer la fiabilité du backend.

### 🔍 Exécuter les tests avec pytest :
```bash
cd backend
pytest
```
---
### 🔍 Exécuter les tests avec Docker :
```bash
docker-compose run backend pytest
```
### 🛠️ Les tests couvrent :
- La disponibilité de l’API.
- La validité des réponses de `/predict`.
- La gestion des erreurs.

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

