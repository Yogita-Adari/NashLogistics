from flask import Flask
from flask_cors import CORS
from .db import Base, ENGINE
from .controller.delivery_controller import bp as delivery_bp

def create_app():
    app = Flask(__name__)
    CORS(app)  # allow all for now
    Base.metadata.create_all(bind=ENGINE)  # create tables
    app.register_blueprint(delivery_bp)
    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(port=5001, debug=True)
