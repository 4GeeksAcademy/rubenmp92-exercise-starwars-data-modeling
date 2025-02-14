import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)  #nullable false para tener que escribirlo si o si 
    planet = Column(String(20))
    # pais = Column(Integer, ForeignKey('country.ID'))
    # pais_relationship = relationship(Country)
    email = Column(String(50), unique=True)
    password = Column(String(25))

class Character(Base):
    __tablename__ = 'character'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Integer)
    mass = Column(Integer)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey('character.ID'))
    character_relationship = relationship(Character)

class Planets(Base):
    __tablename__= 'planets'
    ID = Column(Integer, primary_key=True)
    name = Column(String(20))
    volume = Column(Integer)

class FavouritePlanets(Base):
    __tablename__= 'favorite_planets'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    planets_id = Column(Integer, ForeignKey('planets.ID'))
    planets_relationship = relationship(Planets)

class VehiclesStarships(Base):
    __tablename__='vehicles_starships'
    ID = Column(Integer, primary_key=True)
    name = Column(String(25))
    type = Column(String(25))
    car_licence = Column(Integer)

class FavouriteVehiclesStarships(Base):
    __tablename__= 'favourite_vehicles_startships'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    user_relationship = relationship(User)
    vehicles_staships_id = Column(Integer, ForeignKey('vehicles_starships.ID'))
    vehicles_staships_relationship = relationship(VehiclesStarships)
    


# class Country(Base):
#     __tablename__ = 'country'
#     ID = Column(Integer, primary_key=True)
#     name = Column(String(10))

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'  #recomendable todas las tablas con el nombre en minuscula (address)
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     #nombre columna = Colummn(data_type, atributos...)
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     #primero tipo de dato (ej integer), luego la llave foranea ForeignKey y a donde apunta (ej tabla person y columna id)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person) #vamos a llamar a relationship (lo importamos) y a Person (con mayuscula que es la tabla)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
