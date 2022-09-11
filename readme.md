# Py.NaP - a Notes and Passwords Management System


## Key Features
- Random password generation
- Easy storage and retreival
- Store and share encrypted text notes

---

## Random password generation
Uses the built-in string and the secrets module in python to generate random strings having alphanumeric characters. These strings are by default 32 characters long, but the user can change it to be longer or shorter, 64 characters or 16 characters respectively.

Following are the string constants used to generate random passwords.
- ascii_letters : contain both lowercase and uppercase letters.
- digits : contains digits '0123456789'
- punctuation : contains characters like '!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~'

One of the ways to generate random strings for passwords would be to use the built-in 'random' module in python.

```python
import random
import string


def randstr(n):
    # n is the number of characters in the password.
    characters = string.ascii_letters + string.digits + string.punctuation
    output = "".join(random.choice(characters) for i in range(n))
    return output
```

But this method does not generate cryptographically secure random strings, hence leaving such passwords vulnerable to targeted attacks. Cryptographically-protected passwords use salted one-way cryptographic hashes of passwords.
To counter this, we have to use the built-in 'secrets' module, which helps us in generating said cryptographically secure passwords.

```python
import secrets
import string


def randstr(n):
    # n is the number of characters in the password.
    characters = string.ascii_letters + string.digits + string.punctuation
    output = "".join(secrets.choice(characters) for i in range(n))
    return output

```
---

## Generating the key to encrypt and decrypt passwords

To encrypt and decrypt the passwords, the user has to enter the master password, which will be used to generate a key, which is different for every master password.
```python
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from app import passwd

password = passwd.encode()  # Convert to type bytes
salt = b'<salt>'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

with open('key.key', 'wb') as f:
    f.write(key)

```

---

## Encrypting and Decrypting the passwords

Now that the passwords and the key are generated, we need to encrypt then before storing in the database, to do this, we'll need to use the key we've generated in the previous step and utilize the symmetric encryption method to encrypt and decrypt said passwords.
```python
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

```

---

## Storing in the MySQL Database.

After generating strong passwords, we need to store the passwords in a database because remembering such passwords would be very difficult. For the storage, we will be utilizing the MySQL database. The app interacts with the database using the mysql-connector-python module (Python-MySQL Connector).
This enables us to use the standard and easy to use SQL commands right within our app, hence allowing for easy storage and retrieval.
```python
import mysql.connector


def dbconnect():
    connector = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="tiger",
        database="test")
    cur = connector.cursor()
    return cur
```

---

