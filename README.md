## Project Name
​
- Award
## Author 
​
- Gitonga Miriam Njeri
​
## Project Description
- The website basically works in away that you can post your projects that you have       done with their descriptions and also the live link to the projects that you have       done throughout.
​
## Technologies Used
​
- PYTHON
- DJANGO
- POSTMAN API TESTING
- POSTGRES DATABASE
- BOOTSTRAP AND CSS
- HTML MARKDOWN
​
## BDD 
​
​
### Installing
​
A step by step series of examples that tell you how to get a development env running
​
1. set up a virtual environment using the following command
​
```
python3.6 -m venv --without-pip virtual
```
​
And activate it
​
```
source virtual/bin/activate
```
1. install the latest version of pip
​
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
​
1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3. manage.py makemigrations
```
​
and migrate
```
python3.6 manage.py migrate
```
1. create a admin account
```
python 3.6 manage.py createsuperuser
```
and add your credentials
​
1. run the application using 
```
python3.6 manage.py runserver
```
1. navigate to the admin panel by typing 
```
localhost:8000/admin
```
## BUgs
-
## Project live-link



