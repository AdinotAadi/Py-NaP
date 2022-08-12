import secrets
import string


def randstr(n):
    characters = string.ascii_letters + string.digits + string.punctuation
    output = "".join(secrets.choice(characters) for i in range(n))
    return output
