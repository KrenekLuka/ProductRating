### Install docker locally and run this command to build containers and run then:
`docker-compose up -d`
 
### Run this command to attach a shell to our django web docker container:
`docker-compose run web bash`

### Inside bash docker container run these commands to migrate database and to create initial user(if you use register.py script you can input username and password for user)
```
 python manage.py makemigrations
 python manage.py migrate
 python manage.py createsuperuser, can be replaced with "python py_client/register.py" 
```
 
### To kill running web django container and postgresql database, run this command:
`docker-compose down`

### To tail live logs from web container, run this command:
`docker-compose logs -f`

### In case you want to modify Dockerfile and anything Dockerfile uses, run this command before docker-compose up:
`docker-compose build`

### To run tests in docker container run these commands:
```
docker-compose run web bash
python manage.py test
```

### explaining py_client folder:
It contains scripts for basic CRUD operations and AUTH/register user. You can use postman or similar applications to run all requests, if you do not wish to use these scripts.

### Authentication
Inside `py_client` folder create `token_path.py` and add the following variable `token_path = 'path/to/your/token/'` where token will be stored and used in other py_client scripts.
After the token_path has been set you can run `python py_client/auth.py` to generate an auth token which will be stored in your designated `token_path`

### py_client scripts:
1. `register.py` - it will create new superuser in our database with provided username and password as inputs.
2. `auth.py` - will create token in the token_path for the user that you have provided username and password inputs.
3. `create.py` - will create product in database(you can modify name and price of the product)
4. `delete.py` - will delete product whose id you have input
5. `detail.py` - will show detail of a single product whose id you have input
6. `list.py` - will show paginated products from our database
7. `list_all.py` - will list all the products from our database
8. `create_rating.py` - you can modify product id and rating in the script to select which product you want to rate(it will rate it for the last authenticated user, which you called with auth.py script)
9. `load_dummy_product_data.py` - this will create 20 products in database.
