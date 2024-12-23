# Bibliothèque Numérique 📚

Bienvenue dans **Bibliothèque Numérique**, un système de gestion de bibliothèque en ligne, développé avec Django. Ce projet vous permet de gérer les livres, les auteurs, et les emprunts, tout en offrant une interface utilisateur moderne et intuitive.

---

## 🚀 Fonctionnalités

### 🔖 Gestion des Livres
- Ajouter, modifier et supprimer des livres.
- Rechercher des livres par titre ou genre.

### ✍️ Gestion des Auteurs
- Ajouter, modifier et supprimer des auteurs.
- Rechercher des auteurs par nom ou nationalité.

### 📋 Gestion des Emprunts
- Suivre les emprunts et gérer les retours.
- Empêcher les emprunts si le livre n'a plus d'exemplaires disponibles.

### 🛠️ Pages Utilisateur
- Page d'accueil avec un slider dynamique.
- Formulaires d'inscription et de connexion.
- Interface utilisateur conçue avec Bootstrap 5.

---

## 🖼️ Captures d'Écran

### **Page d'Accueil**
![Accueil](screenshots/homepage.png)

### **Gestion des Livres**
![Livres](screenshots/books_management.png)

### **Gestion des Auteurs**
![Auteurs](screenshots/authors_management.png)

### **Gestion des Emprunts**
![Emprunts](screenshots/loans_management.png)

### **Formulaire d'Inscription**
![Inscription](screenshots/register.png)

---

## 🛠️ Technologies Utilisées

- **Backend :** Django 5.1.4
- **Frontend :** HTML5, CSS3, Bootstrap 5
- **Base de Données :** SQLite
- **Outils :** Python 3.13, Django Admin

---

## 🛠️ Étapes pour Configurer le Projet

Suivez ces étapes pour installer et configurer ce projet Django sur votre machine locale :

### **1. Cloner le Dépôt**
Clonez le dépôt GitHub sur votre machine :
```bash
git clone https://github.com/Rochdi7/Django-Projects.git
cd Django-Projects

# 1. Installer Django (si ce n'est pas déjà fait)
pip install django

# 2. Créer un environnement virtuel
# Sur Windows
py -m venv venv

# Sur macOS/Linux
python3 -m venv venv

# 3. Activer l'environnement virtuel
# Sur Windows
venv\Scripts\activate

# Sur macOS/Linux
source venv/bin/activate

# 4. Naviguer vers le dossier principal du projet
cd /path/to/your/project

# 5. Appliquer les migrations pour initialiser la base de données
python manage.py makemigrations
python manage.py migrate

# 6. Lancer le serveur de développement
python manage.py runserver

# 7. Accéder à l'application dans le navigateur
# Ouvrez votre navigateur et rendez-vous sur :
# http://127.0.0.1:8000
