# 📌 Projet : Prédiction des Prix d'une nuit des Hôtels 🏨

## 🏆 Défi IA : 1001 Nights  

### 📖 Un peu de contexte…  

La **DGCCRF** (équivalent de la répression des fraudes) d'un **pays imaginaire** vient de recevoir des **plaintes** concernant une **agence de voyage en ligne** (*1001NightsHotels.com*). Cette agence est suspectée de **pratiquer des prix à la tête du client**, ce qui pourrait **tromper les consommateurs**. Cependant, les faits dénoncés restent **flous**, nécessitant une **enquête approfondie** avant toute action en justice.  

L’agence propose divers services (**réservations d'hôtels, vols, packages vacances, activités de loisirs**), mais l’enquête concerne **exclusivement la partie hôtellerie**.  

### 🔍 Enquête ciblée sur l'hôtellerie en Europe  

Les plaintes reçues concernent uniquement des **consommateurs européens** ayant réservé des hôtels dans des **villes européennes**. La **DGCCRF** a identifié **9 villes clés** comme représentatives du marché hôtelier en Europe et souhaite concentrer son **investigation sur ces villes**.  

### 👨‍💻 Votre mission en tant que Data Scientist  

Votre réputation de **Data Scientist talentueux** vous a permis d'obtenir un **stage** dans l’équipe en charge de la **pré-enquête**.  

🛠️ **Moyens mis à votre disposition :**  
- **Des puissants moyens de calcul** pour analyser les données.  
- **Un scraper** permettant de collecter les données des prix affichés par l'agence.  

Cependant, pour ne pas éveiller les soupçons de **1001NightsHotels.com**, **le nombre de requêtes que vous pouvez envoyer est limité**.  

### 🎯 Objectif  

Votre objectif est de **décortiquer l'algorithme de pricing de l’agence** et de comprendre **les facteurs qui influencent les prix**.  

🔹 **Serez-vous capable de prédire avec précision les prix fixés par l’algorithme de l’agence ?**  
🔹 **Détecterez-vous des biais dans la tarification pratiquée ?**  

Le **temps presse** car la **CMA** (l’autorité de la concurrence britannique) est **également sur le coup** et souhaite frapper **fort** contre **les pratiques abusives dans le secteur du tourisme**.  

⚠️ **L’équipe compte sur vous pour lever le voile sur l’algorithme et ses potentielles irrégularités !**  

Cependant, comme les prix réels ne sont pas disponibles, j'ai choisi de **les générer artificiellement** en nous basant sur des tendances observées dans le secteur hôtelier.  

---

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

## 🎯 Objectif du projet  
L'objectif est de :  

✅ **Analyser les facteurs influençant les prix** des hôtels.  
✅ **Générer des prix artificiels** pour entraîner un modèle de prédiction.  
✅ **Développer un modèle de Machine Learning** capable d'estimer les prix des hôtels avec précision.  
✅ **Déployer une API Flask et une interface utilisateur** avec Streamlit pour des prédictions en temps réel.  
✅ **Automatiser le déploiement sur une instance AWS EC2 Ubuntu** via **GitHub Actions** et **Docker Compose**, permettant une mise à jour continue et un accès distant aux services. 🚀   

---

## 📌 Table des matières
- [🔧 Prérequis](#prérequis)
- [📂 Structure du projet](#structure-du-projet)
- [📥 Installation](#installation)
- [🚀 Exécution](#exécution)
- [🖱️ Utilisation](#utilisation)
- [🛠️ Technologies utilisées](#technologies-utilisées)
- [📦 Backend (API Flask)](#backend-api-flask)
- [🎨 Frontend (Streamlit)](#frontend-streamlit)
- [✅ Tests Automatisés](#tests-automatisés)
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
│── modelisation/                   # Preprocessing & Modélisation
│   ├── model.ipynb                # Script d'entraînement et d'évaluation du modèle
│   ├── preprocess.ipynb            # Prétraitement des données
│   ├── generate_data.py        # Génération des données artificielles
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
### 🌍 Accès aux services :
- 📌 **API Flask (Local)** : [http://localhost:5000](http://localhost:5000)
- 📌 **API Flask (Déployé sur AWS)** : [http://EC2_PUBLIC_IP:5000](http://EC2_PUBLIC_IP:5000)
---
### 📌 Tester la prédiction des prix avec une requête **POST** 

Utilisez **Postman** pour envoyer une requête `POST` à l'endpoint `/predict` avec les données suivantes :

- **URL (Local) :** `http://localhost:5000/predict`
- **URL (Déployé sur AWS) :** `http://EC2_PUBLIC_IP:5000/predict`
- **Méthode :** `POST`
- **Headers :** `Content-Type: application/json`
- **Body (JSON) :** 

```json
{
  "order_requests": 10,
  "city_x": "amsterdam",
  "date": 10,
  "language": 1,
  "mobile": 0,
  "stock": 10,
  "group": 1,
  "brand": 1,
  "parking": 0,
  "pool": 0,
  "children_policy": 0
}
```
 ### 📌 Réponse attendue :
```json
{
  "predicted_price": 245.75
}
``` 
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

## 🚀 Déploiement Automatisé avec GitHub Actions

Le projet est configuré pour être **déployé automatiquement sur un serveur AWS** via **GitHub Actions**. 

### 📌 Étapes du déploiement :
1. **Push du code sur la branche `main`** déclenche la pipeline CI/CD.
2. **GitHub Actions établit une connexion SSH** avec l'instance EC2.
3. **Le code est synchronisé sur le serveur AWS** via `rsync`.
4. **Docker Compose est exécuté pour redémarrer les services**.

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

