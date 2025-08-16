# git pull 
`git pull git@gitgub_link`

# cd to Project directory (Not a inner Django project directory

`cd project_directory`

# create venv
`python3 -m venv .venv`

# Activate venv python
`source .venv/bin/activate`

# Install python packages for the project
`pip install -r requirements.txt`

# update your database username and password in the settings.py accordingly

```
DATABASES = {
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wsq_project',
        'USER': 'suba',
        'PASSWORD': 'subakaran',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

# Run migration
`python manage.py migrate`

# Run server 
`python manage.py runserver`





