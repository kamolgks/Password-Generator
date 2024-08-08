import string
import random

from flask import (
    render_template, 
    request, 
    send_file, 
    jsonify,
)

def index():
    return render_template('index.html')

def generate_password_route():
    request_data = request.json
    try:
        length = int(request_data.get('length', 8))
        if length < 8 or length > 128:
            return jsonify({"error": "Password length must be between 8 and 128"}), 400
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid length"}), 400

    options = {
        'uppercase': request_data.get('uppercase', 'true') == 'true',
        'lowercase': request_data.get('lowercase', 'true') == 'true',
        'numbers': request_data.get('numbers', 'true') == 'true',
        'symbols': request_data.get('symbols', 'true') == 'true'
    }

    character_set = (
        (string.ascii_uppercase if options['uppercase'] else '') +
        (string.ascii_lowercase if options['lowercase'] else '') +
        (string.digits if options['numbers'] else '') +
        (string.punctuation if options['symbols'] else '')
    )

    if not character_set:
        return jsonify({"error": "No character types selected"}), 400

    password = ''.join(random.choice(character_set) for _ in range(length))

    with open('handlers/generated_password.txt', 'w') as pass_file:
         pass_file.write(f'Your password: {password}')

    return password

def downloadPassword():
    path = "handlers/generated_password.txt"
    return send_file(path_or_file=path, as_attachment=True)

def error_handler_404(x):
    print(f'{x}')
    return render_template('404.html'), 404