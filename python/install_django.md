## How to setup Django project? 

# Setup python in venv
`mkdir project_folder_name`

`cd project_folder_name`

`python -m venv .venv`

`source .venv/bin/activate`


# Install python libraries

`pip install django  python-dotenv django-cors-headers djangorestframework djangorestframework_simplejwt pillow`


**postgres SQL**
`pip install psycopg[binary]`

# Create Django project
`django-admin startproject project_name .`

# Config database in settings.py

**postgres**
```DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bthouse',
        'USER': 'suba',
        'PASSWORD': 'subakaran',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

**mysql**

```DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'divide_to_share',  
        'USER': 'root',  
        'PASSWORD': 'password',  
        'HOST': 'localhost',  
        'PORT': '3306',  
    }
}
```

# Create a app
`python manage.py startapp app_name`

# Run server 
`python manage.py runserver`

#Run first migration
`python manage.py migrate`

# Create admin username and password 
`python manage.py createsuperuser`






