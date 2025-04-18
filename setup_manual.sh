    #!/bin/bash

    # Arrêt et suppression des conteneurs s'ils existent
    docker stop mysql_container app_container nginx_container 2>/dev/null
    docker rm mysql_container app_container nginx_container 2>/dev/null

    # Suppression des volumes et réseaux
    docker volume rm db_volume 2>/dev/null
    docker network rm db_network site_network 2>/dev/null

    # Création des réseaux
    docker network create db_network
    docker network create site_network

    # Création du volume pour MySQL
    docker volume create db_volume

    # Construction des images
    docker build -t mysql ./mysql
    docker build -t app ./app
    docker build -t nginx ./nginx

    # Lancement du conteneur MySQL
    docker run -d \
    --name mysql_container \
    --network db_network \
    -v db_volume:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=rootpassword \
    -e MYSQL_DATABASE=test_db \
    -e MYSQL_USER=myuser \
    -e MYSQL_PASSWORD=mypassword \
    mysql:8.0


    # Connexion du conteneur MySQL au réseau de l'app
    docker network connect site_network mysql_container

    # 💤 Attente que MySQL soit prêt (max 30s)
    echo "⏳ En attente de MySQL (ça peut prendre un shot)..."
    for i in {1..30}; do
        health=$(docker inspect --format='{{.State.Health.Status}}' mysql_container 2>/dev/null)
        if [ "$health" == "healthy" ]; then
            echo "✅ MySQL est prêt !"
            break
        fi
        sleep 1
    done

    # Lancement du conteneur de l'app
    docker run -d \
    --name app_container \
    --network site_network \
    --network-alias app \
    -p 4743:4743 \
    app

    # Connexion de l'app au réseau DB (si besoin de requêtes SQL)
    docker network connect db_network app_container

    # Lancement du conteneur Nginx
    docker run -d \
    --name nginx_container \
    --network site_network \
    -p 5423:824 \
    -v $(pwd)/nginx/conf/nginx.conf:/etc/nginx/nginx.conf:ro \
    nginx


    docker ps

