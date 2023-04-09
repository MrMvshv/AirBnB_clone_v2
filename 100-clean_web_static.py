#!/usr/bin/python3
"""
fabric script that deletes outdated
archives
"""
import os
from fabric.api import *

env.hosts = ['35.175.104.175', '34.224.5.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """ Deletes old archives """
    number = int(number)
    if number < 0:
        return
    elif number == 0:
        number = 1

    with lcd('./versions'):
        local('ls -t | tail -n +{} | xargs rm -rf'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))
