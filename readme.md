# Passwords Management System


## Key Features
- Random password generation
- Easy storage and retrieval

---

## Random password generation
Uses the built-in string and the secrets module in python to generate random strings having alphanumeric characters. The user can enter the desired size of the password to be generated.

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

## Encrypting the password

Now that the passwords and the key are generated, we need to encrypt then before storing in the database, to do this, we'll need to use the key we've generated in the previous step and utilize the symmetric encryption method to encrypt and decrypt said passwords.
```python
    def encryptPassword(self, password):
        password = password.encode("utf-8")
        encoded_text = hashlib.md5(password).hexdigest()
        return encoded_text
```

---

## Storing in the sqlite Database.

After generating strong passwords, we need to store the passwords in a database because remembering such passwords would be very difficult. For the storage, we will be utilizing the sqlite3 database.
This enables us to use the standard and easy to use SQL commands right within our app, hence allowing for easy storage and retrieval.
```python
    with sqlite3.connect(".vault") as db:
        cursor = db.cursor()
```

---

