#!usr/bin/python
import subprocess

subprocess.call("pip3 install -r ../requirements.txt", shell=True)
subprocess.call("python3 manage.py migrate && python3 manage.py createsuperuser", shell=True)
subprocess.call("python3 manage.py makemigrations peer && python3 manage.py migrate", shell=True)
subprocess.call("python3 manage.py runserver", shell=True)

