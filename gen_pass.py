import string, secrets

def generate_password(length=8, uppercase=True, lowercase=True, numbers=True, symbols=True):
    if length < 8:
        return "Password length should be at least 8 characters."

    charset = ""
    if uppercase:
        charset += string.ascii_uppercase
    if lowercase:
        charset += string.ascii_lowercase
    if numbers:
        charset += string.digits
    if symbols:
        charset += string.punctuation

    if not charset:
        return "No character set selected"

    password = ''.join(secrets.choice(charset) for _ in range(length))
    return password