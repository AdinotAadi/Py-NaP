from modules.randomString import *
from modules.encrdecr import *

if __name__ == "__main__":
    n = 32
    char = randstr(n)
    print(char)
    encrypted = encr(char)
    print(encrypted)
    decrypted = decr(encrypted)
    print(decrypted)
