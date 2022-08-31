import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from app import passwd

password = passwd.encode()  # Convert to type bytes
salt = b'\x0b\x8e\x81\xd2\xfdR\xc0\xa9\xd56\x1e6\x0e\x1e\x96h'  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
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
