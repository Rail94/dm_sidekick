from flask import Flask
from app.routes.home import home_bp
from app.routes.initiative import initiative_bp
from app.routes.wariatures import wariatures_bp
from app.routes.deck_of_illusions import deck_of_illusions_bp
from app.routes.probability import probability_bp

# Blueprint Registration
def create_app():
	app = Flask(__name__)

	app.register_blueprint(home_bp)
	app.register_blueprint(initiative_bp)
	app.register_blueprint(wariatures_bp)
	app.register_blueprint(deck_of_illusions_bp)
	app.register_blueprint(probability_bp)

	return app
