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
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = f"versions/web_static_{time}.tgz"

    if not os.path.isdir("versions"):
        if local(f"mkdir -p versions").failed is True:
            return None
    if local(f"tar -cvzf {path} web_static").failed is True:
        return None
    size = os.path.getsize(path)
    return f"{path}"
