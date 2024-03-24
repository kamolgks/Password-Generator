from config import PORT

from gen_pass import generate_password
from flask import Flask, render_template, request, send_file

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():  
    request_data = request.json
    try:
        length = int(request_data.get('length', 8))
        uppercase = request_data.get('uppercase', 'true') == 'true'
        lowercase = request_data.get('lowercase', 'true') == 'true'
        numbers = request_data.get('numbers', 'true') == 'true'
        symbols = request_data.get('symbols', 'true') == 'true'

        if length < 8 or length > 128:
            return "Ti invalid", 400

    except (ValueError, TypeError):
        return "Invalid length", 400

    password = generate_password(
        length, uppercase, lowercase, numbers, symbols)

    with open('generated_password.txt', 'w') as pass_file:
        pass_file.write(f'Your password: {password}')

    return password


@app.route('/download_pass')
def download_pass():
    return send_file(path_or_file='generated_password.txt', as_attachment=True, download_name='password.txt')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
