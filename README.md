# Django REST – Todolist & Notes

API REST développée avec **Django** et **Django REST Framework**.

---

## Prérequis

- Python 3.10+
- pip
- Git
- Windows

---

## Installation

Cloner le projet :

```powershell
git clone https://github.com/jaykkoo/ootis-test.git
cd ootis_test
```

---

## Environnement virtuel

Créer un environnement virtuel :

```powershell
python -m venv venv
```

Activer l’environnement :

```powershell
venv\Scripts\activate
```

---

## Dépendances

Installer les dépendances :

```powershell
pip install -r requirements.txt
```

---

## Lancer le projet

Appliquer les migrations :

```powershell
python manage.py migrate
```

Démarrer le serveur de développement :

```powershell
python manage.py runserver
```

---

## Accès local

L’API est accessible à l’adresse :

```
http://127.0.0.1:8000/
```

---

## Remarques

- Projet API REST uniquement (pas de templates HTML)
- Base de données SQLite utilisée pour le développement
- Les environnements virtuels et la base locale ne sont pas versionnés
