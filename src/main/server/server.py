import os
from flask import Flask

from src.main.routes.routes import user_route_bp

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'src', 'presentation', 'templates')

app = Flask(__name__, template_folder=template_dir)
app.config['SECRET_KEY'] = 'secret_key'

app.register_blueprint(user_route_bp)