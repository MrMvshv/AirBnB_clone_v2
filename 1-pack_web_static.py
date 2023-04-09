#!/usr/bin/python3
""" fabric script to create an archive file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ compress a file and return it's path """

    """save the current time and filename path"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    fPath = "versions/web_static_{}.tgz".format(time)

    try:
        """create directory called versions"""
        local("mkdir -p versions")

        """create archive file"""
        local("tar -cvzf {} web_static/".format(fPath))

        """return the path to the archive file created"""
        return "{}".format(fPath)

        """return none if an error occurs"""
    except Exception as e:
        return None
