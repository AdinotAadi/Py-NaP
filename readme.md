# NaP.Py - a Notes and Passwords Management System


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
