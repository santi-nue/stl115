from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the n8n app"""
    Popen(["copyparty"])
