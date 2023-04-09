#!/usr/bin/python3
"""
Fabric script to deploy web static content
"""

from fabric.api import env, put, run
from os.path import exists, basename, splitext

env.hosts = ['35.175.104.175', '34.224.5.166']


def do_deploy(archive_path):
    """
    Deploys an archive to the web servers
    """
    # Check if archive_path exists
    if not exists(archive_path):
        return False

    # Get the file name without extension
    arName = basename(archive_path)
    arStr = splitext(arName)[0]

    try:
        # Upload archive to the temporary folder on the web server
        put(archive_path, "/tmp/")

        # Create the directory where the code will be deployed
        run(f"sudo mkdir -p /data/web_static/releases/{arStr}/")

        # Uncompress the archive into the deployment folder
        run(f"sudo tar -xzf /tmp/{arName} \
                -C /data/web_static/releases/{arStr}/")

        # Remove the archive from the server
        run(f"sudo rm /tmp/{arName}")

        # Move the files to a new folder and delete the old symbolic link
        run(f"sudo mv /data/web_static/releases/{arStr}/web_static/* \
            /data/web_static/releases/{arStr}/")
        run(f"sudo rm -rf /data/web_static/releases/{arStr}/web_static")

        # Delete the old symbolic link and create a new one
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{arStr}/ \
                /data/web_static/current")

        return True

    except Exception as e:
        # If there is an error, return False
        return False
