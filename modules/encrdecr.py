from cryptography.fernet import Fernet


key = Fernet.generate_key()
fernet = Fernet(key)


def encr(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage


def decr(encmsg):
    decmsg = fernet.decrypt(encmsg).decode()
    return decmsg