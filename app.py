import logging
import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from data.config import PORT, host
from handlers.handlers import (
    index,
    generate_password_route,
    downloadPassword,
    error_handler_404,
)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('flask.app')

app = Flask(__name__, template_folder='templates', static_folder='static')
app.wsgi_app = ProxyFix(app.wsgi_app)  

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True  
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  
app.config['JSON_SORT_KEYS'] = False  


@app.after_request
def add_security_headers(response):
    
    headers = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'SAMEORIGIN',
        'X-XSS-Protection': '1; mode=block',
        'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
    }
    response.headers.extend(headers)
    return response

app.add_url_rule('/', 'index', index)
app.add_url_rule('/generate_password', 'generate_password_route', generate_password_route, methods=['POST'])
app.add_url_rule('/download_password', 'downloadPassword', downloadPassword)
app.add_url_rule('/error', 'error_handler', error_handler_404)

app.register_error_handler(404, error_handler_404)

if __name__ == '__main__':
    logger.info(f"Запуск сервера на http://{host}:{PORT}")
    app.run(host=host, port=PORT, debug=False, threaded=True)
