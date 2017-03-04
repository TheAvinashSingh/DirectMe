Direct Me
=========

[![Build Status](https://travis-ci.org/Software-Incubator/DirectMe.svg?branch=dev)](https://travis-ci.org/Software-Incubator/DirectMe)
[![codecov](https://codecov.io/gh/Software-Incubator/DirectMe/branch/dev/graph/badge.svg)](https://codecov.io/gh/Software-Incubator/DirectMe)
[![Code Health](https://landscape.io/github/Software-Incubator/DirectMe/dev/landscape.svg?style=flat)](https://landscape.io/github/Software-Incubator/DirectMe/dev)

Setup Instructions
------------------

Your will need a PostgreSQL database

Run the following commands after cloning the project:

- Run database migrations: `python manage.py migrate`
- Load initial data: `python manage.py loaddata db.json`
- Add the cron jobs: `python manage.py crontab add`


You might also need to configure the following environment variables:
- AWS_ACCESS_KEY_ID
- AWS_S3_CUSTOM_DOMAIN
- AWS_S3_SIGNATURE_VERSION
- AWS_SECRET_ACCESS_KEY
- AWS_STORAGE_BUCKET_NAME
- DATABASE_URL
- DJANGO_SETTINGS_MODULE
- EMAIL_HOST
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- EMAIL_PORT
- EMAIL_USE_TLS
- IS_HEROKU
- OPBEAT_APP_ID
- OPBEAT_ORGANIZATION_ID
- OPBEAT_SECRET_TOKEN
- SECRET_KEY
- SOCIAL_AUTH_GOOGLE_OAUTH2_KEY


<LOVE.PEACE.CODE/>