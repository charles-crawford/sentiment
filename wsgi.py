from application import celery
from application.utils.factory import create_app
from waitress import serve
import logging
import subprocess

# Set the logging to info to log into log file
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

start_worker_cmd = 'celery -A application.celery worker --loglevel INFO --without-gossip --without-mingle -O fair --pool threads'
subprocess.Popen(start_worker_cmd.split(' '))
start_monitor_cmd = 'celery -A application.celery flower'
subprocess.Popen(start_monitor_cmd.split(' '))

app = create_app(celery=celery)

if __name__ == "__main__":
    serve(app, host='0.0.0.0',  port=5000)
