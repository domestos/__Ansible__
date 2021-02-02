#!/bin/bash
source {{project_dir}}/venv/bin/activate
cd  {{project_dir}} 
exec daphne -b 0.0.0.0 -p  {{daphne_port }} config.asgi:application