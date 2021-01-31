#!/bin/bash
source {{project_dir}}/venv/bin/activate
exec gunicorn -c "{{project_dir}}/gunicorn.conf.py" --chdir {{project_dir}}  config.wsgi