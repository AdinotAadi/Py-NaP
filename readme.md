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

