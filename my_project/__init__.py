import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

#############
# DATABASE
#############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "mysecretkey"


db = SQLAlchemy(app)
Migrate(app, db)

#############

#############
# Login Configs
#############

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

# BluePrint Configs

from my_project.core.views import core
from my_project.users.views import users
from my_project.blog_posts.views import blog_posts as bp
from my_project.error_pages.handlers import error_pages


# Register Blueprints
app.register_blueprint(users)
app.register_blueprint(bp)
app.register_blueprint(core)
app.register_blueprint(error_pages)
