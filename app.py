import logging
from flask import Flask

from data.config import PORT, host
from handlers.handlers import (
    index,
    generate_password_route,
    downloadPassword,
    error_handler_404,
)

app = Flask(__name__, template_folder='templates', static_folder='static')

app.add_url_rule('/', 'index', index)
app.add_url_rule('/generate_password', 'generate_password_route', generate_password_route, methods=['POST'])
app.add_url_rule('/download_password', 'downloadPassword', downloadPassword)
app.add_url_rule('/error', error_handler_404)

app.register_error_handler(404, error_handler_404)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(f"Starting server on http://{host}:{PORT}")
    app.run(debug=True, port=PORT)
