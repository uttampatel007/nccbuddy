# nccbuddies
Social Media Clone Developed In Django
## Getting Started
This project is basic social media clone with features like user authentication, image with description post, post like, post comment, user profile, user follow/unfollow, post search, user search and much more. Python, Django, HTML, CSS, Bootstrap, JavaScript, AJAX, is used in this project.
### Prerequisites
Things you need to install the project and how to install them
```
Python : https://www.python.org/
Virtual Environment : pip install virtualenv
Django : pip install django
```
### Installing and SetUp
1) Clone or download this project.
2) Set Up Virtual Environment and activate it
3) Install dependencies
```
pip install -r requirements.txt
```
4) Change database settings in case you dont want to use PostgreSQL to sqlite
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
5) Also comment out AWS and Email settings in case you dont required(They are only for production):
6) Migrate data using command 
```
python manage.py migrate
```
7) Create Superuser
```
python manage.py createsuperuser
```
8) Run project on localhost:
```
python manage.py runserver
```

## Authors

* **Uttam Velani**
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
