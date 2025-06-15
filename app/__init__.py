from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.heroes import heroes_bp
    from app.routes.powers import powers_bp
    from app.routes.hero_powers import hero_powers_bp

    app.register_blueprint(heroes_bp)
    app.register_blueprint(powers_bp)
    app.register_blueprint(hero_powers_bp)

    return app