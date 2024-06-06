from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
 login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)
    login.login_view = 'auth.login'

    from app.routes import auth_routes, waste_routes
    app.register_blueprint(auth_routes.auth_bp, url_prefix='/auth')
    app.register_blueprint(waste_routes.waste_bp, url_prefix='/waste')

    return app
