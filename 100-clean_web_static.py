#!/usr/bin/python3
"""
fabric script that deletes outdated
archives
"""
import os
from fabric.api import *

env.hosts = ['35.175.104.175', '34.224.5.166']


def do_clean(number=0):
    """Delete out-of-date archives

    Args:
        number (int): The number of archives to keep

    If number = 0 or 1, keep the most recent archive only
    If number = 2, keep 2 most recent archives, etc
    """
    num = int(number)
    
    if num == 0:
        num = 1

    archives = sorted(os.listdir("versions"))
    [archives.pop() for n in range(num)]

    with lcd("versions"):
        [local(f"rm -rf ./{ar}") for ar in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        [archives.pop() for n in range(num)]
        [run(f"rm -rf ./{ar}") for ar in archives]
