# api-auth
api rest for registration and login 


After cloning the repo:
## create a virtual environment
$ virtualenv env
$ . env/bin/activate

## Install dependencies
$ pip install -r requirements.txt

## Initialize the DB
$ cd api
$ python manage.py makemigrations
$ python manage.py migrate

## Start the server
$ python manage.py runserver

The site will be accessible at http://localhost:8000/.

## API endpoints

### Register:
curl -X POST http://127.0.0.1:8000/auth/users/ --data "username=Amine&email=Amine@gmail.com&password=test1234&re_password=test1234"

### user's detail 
curl -LX GET http://127.0.0.1:8000/auth/users/me/

### login 
curl -X POST http://127.0.0.1:8000/auth/token/login/ --data "email=Amine@gmail.com&password=test1234"

### user's detail 
curl -LX GET http://127.0.0.1:8000/auth/users/me/ -H "Authorization: Token f6a28dbe42aaebdb0794b6e4dc5deed7cda2997f"

#### logout
curl -X POST http://127.0.0.1:8000/auth/token/logout/ -H "Authorization: Token f6a28dbe42aaebdb0794b6e4dc5deed7cda2997f"

