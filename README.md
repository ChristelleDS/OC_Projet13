## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Variables

- Créer un fichier d'environnement .env à la racine du projet et y définir les variables d'environnement (sans espace ni guillements)
    SECRET_KEY et SENTRY_DSN
- ajouter ce fichier .env dans le fichier .gitignore


### Déploiement en intégration continue

Le déploiement se fait via circleCI (config.yml) à chaque déploiement du projet sur la branche master de GITHUB. 
1) L'exécution du linting et des tests
2) La conteneurisation du site en une image Docker (si étape 1 OK)
3) La mise en production sous Heroku ( si étape 2 OK)

### Configuration de circleCI

- créer un compte sur https://circleci.com/ et lier votre compte github: https://circleci.com/signup/
- Aller dans les settings du projet concerné, puis créer vos variables d'environnement dans le menu du même nom:
DOCKER_PASSWORD, DOCKER_USERNAME, HEROKU_API_KEY, SECRET_KEY et SENTRY_DSN


### Containerisation avec Docker

- https://hub.docker.com/
- S'inscrire et s'identifier
- Installer Docker desktop en local
- alimenter les variables d'authentification DOCKER dans CircleCI

Le fichier Dockerfile décrit les instructions à éxécuter pour construire l'image docker.

### Hébergement Heroku

- S'incrire sur Heroku: https://signup.heroku.com/ et se connecter
- Au niveau du tableau de bord, cliquer sur "New" puis "Create new app"
- Donner un nom à l'application (oc-lettings-1222 dans notre cas) puis cliquer sur "Create app"
- Aller dans les settings de l'application crée, ajouter les variables d'environnement (Config vars/Reveal config vars):
SECRET_KEY, SENTRY_DSN, HEROKU_API_KEY
- alimenter la variable HEROKU_API_KEY dans circleCI

### Monitoring Sentry

- Lier votre compte github à Sentry à partir du lien: https://sentry.io/signup/
- Créer un projet et récupérer son DSN dans les settings
- alimenter la variable SENTRY_DSN dans heroku et circleCI
