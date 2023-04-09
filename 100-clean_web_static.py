#!/usr/bin/python3
""" deletes out-of-date archives, using the function do_clean"""
import os
from fabric.api import *

env.hosts = ['35.175.104.175', '34.224.5.166']


def do_clean(number=0):
    """Deletes out-of-date archives of the static files
    Args:
        number (Any): The number of archives to keep
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
