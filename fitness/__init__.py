import os

from flask import Flask
from flask_login import (
  LoginManager,
  current_user,
  login_required,
  login_user,
  logout_user,
)

from fitness.user import User

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'fitness.sqlite'),
    )

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from . import diary
    app.register_blueprint(diary.bp)
    app.add_url_rule('/', endpoint='index')


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Flask-Login helper to retrieve a user from our db
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app