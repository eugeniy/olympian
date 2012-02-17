from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('OLYMPIAN_SETTINGS')

    from olympian.admin import admin
    app.register_blueprint(admin)

    return app
