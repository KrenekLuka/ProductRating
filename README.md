 docker-compose up -d
 
 docker-compose run web bash

 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser

docker-compose down
docker-compose logs -f

docker-compose build