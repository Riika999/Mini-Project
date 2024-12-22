from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('instance.config.Config')

    db.init_app(app)
    CORS(app)  

    api = Api(app)
    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
