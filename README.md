# hr_management
 
template for writing tests for my usecase for Software engineering course

## Getting Started
Execute these commands in the root directory of the project.

#### Virtual env
Create a virtual environment using
```
python-m venv env
```
#### Activate Virtual Environment
```
env\Scripts\activate.bat
```
or(for linux systems)
```
source env/bin/activate
```
#### Install requirements

```
pip install -r requirements.txt
```
#### Make migrations
```
python manage.py makemigrations
python manage.py makemigrations hr

python manage.py migrate
```
#### Run server
```
python manage.py runserver
```

All done now you can go [here](http://127.0.0.1:8000/) to see the project.
