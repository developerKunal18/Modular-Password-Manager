import os
from utils import encode, decode

MASTER_FILE = "master.txt"

def setup_master():
    if not os.path.exists(MASTER_FILE):
        with open(MASTER_FILE, "w") as file:
            file.write(encode("admin"))

def verify_password(password):
    with open(MASTER_FILE, "r") as file:
        saved = decode(file.read())

    return password == saved
