from logging import exception
from cryptography.fernet import Fernet

with open('key.key', 'rb')as file:
    key = file.read()

f = Fernet(key)

def encr(message):
    encMessage = f.encrypt(message.encode())
    return encMessage


def decr(encmsg):
    try:
        decmsg = f.decrypt(encmsg).decode()
        return decmsg
    except exception as e:
        print("Invalid master password.")