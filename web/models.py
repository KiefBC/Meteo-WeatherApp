from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.types import String
from main import db

Base = declarative_base()


class WeatherModel(db.Model):
    __tablename__ = 'City'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(255), unique=True, nullable=False)
    # more to come

    def __repr__(self):
        return f'<City {self.name}>'

    def __str__(self):
        return f'<City {self.name}>'
