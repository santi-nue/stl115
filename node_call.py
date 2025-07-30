from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the app"""
    Popen(["copyparty", "--rp-loc", "/home/jovylan"])
