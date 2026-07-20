from apiflask import APIFlask

from myapp.config import Config
from myapp.extensions import db, jwt

from myapp.core.errors import register_error_handlers

from flask_cors import CORS


def create_app(config_class=Config):
    app = APIFlask(__name__)
    app.config.from_object(config_class)
    
    CORS(app)
    
    register_error_handlers(app)
    
    app.security_schemes = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    app.config["SECURITY"] = [{"BearerAuth": []}]

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Import semua model
    import myapp.models
    
    # ----- blueprint -----
    from myapp.features.auth.routes import auth_bp
    from myapp.features.mesin_pencarian.routes import pencarian_bp
    from myapp.features.surat.routes import surat_bp

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(pencarian_bp)
    app.register_blueprint(surat_bp)

    return app