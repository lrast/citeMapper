from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup the application
app = Flask(__name__)

# get configs 
from webapp.config import Configs
app.config.from_object(Configs)

# get routing info
import webapp.routes

# connect to the database migration service
db = SQLAlchemy(app)
migrate = Migrate(app, db)

