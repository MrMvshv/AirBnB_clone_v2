#!/usr/bin/python3
"""
fabric script that distributes an archive
to servers and sets up shop
"""
import os
from fabric.api import put, env, run

env.hosts = ['35.175.104.175', '34.224.5.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ send archive and extract on server
    Args:
        archive_path (str): path to archive
    Returns:
        if deployed - True
        if file doesn't exist or error - False
    """

    if not os.path.exists(archive_path):
        return False

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
"""    print("New version deployed!")"""
    return True
