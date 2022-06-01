Install docker locally and run this command to build containers and run then:
docker-compose up -d
 
Run this command to attach a shell to our django web docker container:
docker-compose run web bash

Inside bash docker container run these commands to migrate database and to create initial user(if you use register.py script you can input username and password for user)
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser, can be replaced with "python py_client/register.py" 

 
To kill running web django container and postgresql database, run this command:
docker-compose down

To tail live logs from web container, run this command:
docker-compose logs -f

In case you want to modify Dockerfile and anything Dockerfile uses, run this command before docker-compose up:
docker-compose build

To run tests in docker container run these commands:
docker-compose run web bash
python manage.py test     