#!/usr/bin/python3
""" fabric script that generates a .tgz archive """
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """ compress web_static and store in versions
    Args:
        no args
    Returns:
        path to created archive
        if it failed - None
    """

    """ save current time and full tgz path """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = f"versions/web_static_{time}.tgz"

    """ if folder does not exist, create it """
    if not os.path.isdir("versions"):
        if local(f"mkdir -p versions").failed is True:
            return None

    """ create the archive and return path """ 
    if local(f"tar -cvzf {path} web_static").failed is True:
        return None
    return f"{path}"
