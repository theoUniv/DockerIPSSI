# Architecture d'Application Web à 3 Conteneurs

Ce projet implémente une architecture web à trois conteneurs utilisée pour déployer une application web simple reliée à une base de données MySQL et exposée via un proxy Nginx.

## Architecture

L'architecture se compose de trois conteneurs principaux :

- **Nginx** : Agit comme un proxy inverse et expose l'application sur le port 5423
- **Application Web** : Une application développée avec Flask qui implémente les routes /health et /data
- **MySQL** : Un serveur de base de données qui stocke les données utilisées par l'application

## Prérequis

- Docker
- Docker Compose

## Structure du projet

./
├── app/
│   ├── Dockerfile
│   ├── src/
│   │   └── app.py
├── mysql/
│   ├── Dockerfile
│   └── conf/
│       └── init.sql
├── nginx/
│   └── conf/
│       └── nginx.conf
├── compose.yaml
└── setup_manual.sh

## Démarrage

### Méthode 1 : Utilisation du script manuel

Pour démarrer l'application via le script manuel :

```bash
# S'assurer que le script a les permissions d'exécution
chmod +x setup_manual.sh

# Exécuter le script
./setup_manual.sh
```

### Accès à l'application
Une fois démarrée, l'application est accessible via les URLs suivantes :

Vérification de santé : http://localhost:5423/health
Données de la base de données : http://localhost:5423/data