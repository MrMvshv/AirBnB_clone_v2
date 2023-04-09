#!/usr/bin/python3

""" Fabric script that distributes an archive to your web server
"""

import os
from fabric.api import put, env, run

# Define hosts, user and ssh key
env.hosts = ['35.175.104.175', '34.224.5.166']


def do_deploy(archive_path):
    """distributes an archive to your web servers.
    """
    # Check if archive_path exists
    if not os.path.exists(archive_path):
        return False

    # Get filename w/out extension and archive name
    archive = archive_path.split('/')[-1]
    folder = archive_path.split('.')[0]

    try:
        # Upload archive to /tmp on server
        put(archive_path, f"/tmp/{archive}")

        # Remove the archive if it exists on server
        run(f"rm -rf /data/web_static/releases/{folder}/")

        # Create dir on server
        run(f"mkdir -p /data/web_static/releases/{folder}/")

        # Decompress the archive to folder
        run(f"tar -xzf /tmp/{archive} -C /data/web_static/releases/{folder}/")

        # Remove the downloaded archive from /tmp
        run(f"rm /tmp/{archive}")

        # Move files to the root folder
        run(f"mv  /data/web_static/releases/{folder}/web_static/* \
                /data/web_static/releases/{folder}/")

        # Remove folder tree
        run(f"rm -rf /data/web_static/releases/{folder}/web_static")

        # Remove old link
        run("rm -rf /data/web_static/current")

        # Create new link
        run(f"ln -s /data/web_static/releases/{folder}/ \
                /data/web_static/current")

        return True

    except Exception as e:
        # Error handling
        return False
