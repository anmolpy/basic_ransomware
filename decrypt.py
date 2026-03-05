import os
from cryptography.fernet import Fernet 

files = []

for file in os.listdir():
    if file == 'encrypt.py' or file == 'decrypt.py' or file == 'key.key':
        continue
    if os.path.isfile(file):
        files.append(file)

with open("key.key", "rb") as k:
    key = k.read()

for file in files:
    with open(file, "rb") as f:
        contents = f.read()
        content_decrypted = Fernet(key).decrypt(contents)
    with open(file, "wb") as f:
        f.write(content_decrypted)

print('decrypted with key')