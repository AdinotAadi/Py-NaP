from logging import exception
from cryptography.fernet import Fernet

with open('key.key', 'rb')as file:
    key = file.read()

f = Fernet(key)


def encr(message):
    return f.encrypt(message.encode())


def decr(encmsg):
    try:
        return f.decrypt(encmsg).decode()
    except exception as e:
        print(e)
