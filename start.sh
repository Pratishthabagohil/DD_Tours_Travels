#!/bin/bash
python3 manage.py migrate
gunicorn your_project_name.wsgi
