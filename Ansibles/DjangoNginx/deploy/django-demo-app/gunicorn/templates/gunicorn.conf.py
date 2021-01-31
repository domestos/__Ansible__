
command = '{{project_dir}}/venv/bin/gunicorn'
pythonpath = '{{project_dir}}/venv/bin/python'

workers = 2
syslog = True
bind = ['127.0.0.1:{{gunicorn_port}}']
umask = 0
loglevel = "debug"
logfile = '/var/log/gunicorn/error.log'
limit_request_fields  = 32000
limit_request_field_size = 0
user = '{{ project_user }}'
group = '{{ project_user }}'
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
