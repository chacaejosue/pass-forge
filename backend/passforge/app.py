"""Flask application factory."""

from __future__ import annotations

import os

from flask import Flask, jsonify, request

from .routes import api


def create_app() -> Flask:
    app = Flask(__name__)
    configured_origins = os.getenv("FRONTEND_URL", "http://localhost:4321,http://127.0.0.1:4321")
    app.config.from_mapping(
        MAX_CONTENT_LENGTH=16 * 1024,
        ALLOWED_ORIGINS={origin.strip() for origin in configured_origins.split(",") if origin.strip()},
    )
    app.register_blueprint(api, url_prefix="/api")

    @app.after_request
    def add_cors_headers(response):
        # Read the request origin without adding credentials or wildcard access.
        origin = request.headers.get("Origin", "")
        if origin in app.config["ALLOWED_ORIGINS"]:
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Vary"] = "Origin"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        return response

    @app.errorhandler(413)
    def request_too_large(_error):
        return jsonify(error="La solicitud es demasiado grande."), 413

    return app


app = create_app()
