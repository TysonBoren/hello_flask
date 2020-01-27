from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

#do not need this as of video 'Creating a SQLite Database in Flask with SQLAlchemy'. Dont understand why yet. 
# @app.route('/')
# def hello():
#     return 'Hey Flask'

#telling server where to put things. - 'daniel floyd'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique = False)
    content = db.Column(db.String(144), unique = False)
    
    def __init__(self, title, content):
        self.title = title
        self.content = content

class GuideSchema(ma.Schema):
    class meta:
        fields = ('title', 'content')

guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)
# from app import db. Wrote that in terminal and daniel said to make note of it. 


if __name__ == '__main__':
    app.run(debug=True)
    
    