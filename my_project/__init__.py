from flask import Flask

app = Flask(__name__)

from my_project.core.views import core
from my_project.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)
