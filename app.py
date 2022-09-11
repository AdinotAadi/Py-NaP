from modules.randomString import *
from modules.encrdecr import *


def main():
    print("Enter the master password: ")
    passwd = input("Enter the master password:")
    n = 32
    char = randstr(n)
    print(f"Generated string: {char}")
    encrypted = encr(char)
    print(f"Encrypted string: {encrypted}")
    decrypted = decr(encrypted)
    print(f"Decrypted string: {decrypted}")
    if (char == decrypted):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
