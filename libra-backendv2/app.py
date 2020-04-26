from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
import os
import uuid
import fastsemsim

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db2.sqlite')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1@localhost:5432/libra' #Actual configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:MESA2611@localhost:5432/libra'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = "mysecret"
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Init DB
db = SQLAlchemy(app)

# Init DB Engine
db_engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

# Init Marsh
ma = Marshmallow(app)

# Init BCrypt
bcrypt = Bcrypt(app)

# Init Migrate
migrate = Migrate(app, db)

# Init Ontology
hpo = fastsemsim.load_ontology( ontology_type='Ontology', source_file='./ontologyMetric/hp.obo',file_type='obo')

CORS(app, expose_headers='Authorization')
#app.config['CORS_HEADERS'] = 'Content-Type'
from .views import *

# Run server
if __name__ == '__main__':
  app.run(debug=True)
  # app.secret_key = os.urandom(24)
  # app.run(debug=True,host="0.0.0.0",use_reloader=False)

