#!/usr/bin/python3
"""
fabric script that creates and
distributes an archive to servers
"""
from fabric.api import put, env, run

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.175.104.175', '34.224.5.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def deploy():
    """ Does a full deployment to servers """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
