#!/usr/bin/python3
"""Fabric script that creates and
distributes an archive to servers.
"""

# Import fabric
from fabric.api import put, env, run

# Import the required functions
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

# Set up the fabric environment variables
env.hosts = ['35.175.104.175', '34.224.5.166']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def deploy():
    """ 
    Does a full deployment to servers
    """
    # compress the archive
    path = do_pack()

    if path is None:
        # Return false if archive is not created
        return False

    # Deploy to remote server
    return do_deploy(path)
