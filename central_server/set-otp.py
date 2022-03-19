#!usr/bin/python
import os
import subprocess

name = "sed -i \'s/# admin.site.__class__ = OTPAdminSite/admin.site.__class__ = OTPAdminSite/g\' central_server/urls.py"
subprocess.call(name, shell=True)
