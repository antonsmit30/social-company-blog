from flask import Flask

app = Flask(__name__)

from my_project.core.views import core
app.register_blueprint(core)
