import os
import json


CONF_FILE = './confidentials/instagram.json'

def set_env():
    with open(CONF_FILE, mode='r') as f:
        j = json.load(f)
    
    os.environ['INSTAGRAM_ID'] = j['id']
    os.environ['INSTAGRAM_PASSWORD'] = j['pass']
