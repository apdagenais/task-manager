# Initializes Flask app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

# Flask extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager() # Login/logout sessions

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Start extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login' # redirects to /login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    from app.routes import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

