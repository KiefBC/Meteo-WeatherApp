from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.types import String
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class WeatherModel(db.Model):
    __tablename__ = 'City'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    # more to come

    def __repr__(self):
        return f'<City {self.name}>'

    def __str__(self):
        return f'<City {self.name}>'
