import random
import string

from flask import Flask, render_template, request


app = Flask(__name__)


def generate_password(length, uppercase, lowercase, numbers, symbols):
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

    password = ''.join(random.choice(charset) for _ in range(length))
    return password


@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    quantity = int(request.form.get('quantity'))
    length = int(request.form.get('length'))
    uppercase = request.form.get('uppercase') == 'true'
    lowercase = request.form.get('lowercase') == 'true'
    numbers = request.form.get('numbers') == 'true'
    symbols = request.form.get('symbols') == 'true'
    passwords = []

    for _ in range(quantity):
        password = generate_password(
            length,
            uppercase, 
            lowercase, 
            numbers, 
            symbols,
        )
        passwords.append(password)

    with open('generated_passwords.txt', 'w') as file:
        file.write('\n'.join(passwords))

    return 'Passwords generated and saved'


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
