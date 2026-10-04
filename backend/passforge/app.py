"""Flask application factory."""

from __future__ import annotations

import os

from flask import Flask, jsonify

from .routes import api


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        MAX_CONTENT_LENGTH=16 * 1024,
        ALLOWED_ORIGIN=os.getenv("FRONTEND_URL", "*"),
    )
    app.register_blueprint(api, url_prefix="/api")

    @app.after_request
    def add_cors_headers(response):
        response.headers["Access-Control-Allow-Origin"] = app.config["ALLOWED_ORIGIN"]
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Cache-Control"] = "no-store"
        return response

    @app.errorhandler(413)
    def request_too_large(_error):
        return jsonify(error="La solicitud es demasiado grande."), 413

    return app


app = create_app()
