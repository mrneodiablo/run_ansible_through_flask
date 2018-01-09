import os, sys, shutil
from setuptools import setup

setup(
    name='flask_ansible',
    version='1.0',
    author='dongvt',
    author_email='vothanhdong18@gmail.com',
    description='service uppatch real',
    include_package_data=True,
    install_requires=['Flask==0.12.*', 'ansible==2.2.0.*', 'supervisor==3.3.3.*', 'gunicorn=19.7.*', 'requests'],
)


print """   *************************************
                [install supervisord]    
"""

current_dir = os.getcwd()
source_config_supervisor = current_dir + "/install/supervisord.conf"
shutil.copy(src=source_config_supervisor, dst="/etc/")
try:
    os.mkdir( "/var/log/gunicorn/")
except Exception as e:
    print "Error mkdir /var/log/gunicorn/ \n"
    print "Pmkdir /var/log/gunicorn/"
    print Exception.message

print "Start Supervisor"
print "supervisord -c /etc/supervisord.conf"

