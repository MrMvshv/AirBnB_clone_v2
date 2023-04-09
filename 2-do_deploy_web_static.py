#!/usr/bin/python3
"""
fabric script that distributes an archive
to servers and sets up shop
"""
import os
from fabric.api import put, env, run

# define hosts, user and ssh key
env.hosts = ['35.175.104.175', '34.224.5.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    send archive and extract on server
    :param archive_path path to archive
    :type archive_path: str
    :return: if deployed - True, error - False
    """
    #check if archive exists
    if not os.path.exists(archive_path):
        return False

    #get filename w/out extension and archive name
    archive = archive_path.split('/')[-1]
    folder = archive_path.split('.')[0]

    if put(archive_path, f"/tmp/{archive}").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{folder}/").failed is True:
        return False

    if run(f"mkdir -p /data/web_static/releases/{folder}/").failed is True:
        return False
    if run(f"tar -xzf /tmp/{archive} -C \
            /data/web_static/releases/{folder}/").failed is True:
        return False
    if run(f"rm /tmp/{archive}").failed is True:
        return False

    if run(f"mv  /data/web_static/releases/{folder}/web_static/* \
                /data/web_static/releases/{folder}/").failed is True:
        return False
    if run(f"rm -rf \
            /data/web_static/releases/{folder}/web_static").failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run(f"ln -s /data/web_static/releases/{folder}/ \
                /data/web_static/current").failed is True:
        return False
    return True
