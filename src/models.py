from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeingKey
from sqlalchemy.orm import Mapped, mapped_column, relationShip

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), nullable= False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorite_characters_list: Mapped[list['FavoriteCharacters']] = relationShip(back_populates = 'user')
    favorite_planets_list: Mapped[list['FavoritePlanets']] = relationShip(back_populates = 'user')
    favorite_starships_list: Mapped[list['FavoriteStarships']] = relationShip(back_populates = 'user')

class FavoriteCharacters(db.Model):
    __tablename__ = 'favorite_character'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeingKey('user.id'))
    user: Mapped['User'] = relationShip(back_populates = 'favorite_characters_list')
    character_id: Mapped[int] = mapped_column(ForeingKey('characters.id'))
    character: Mapped['Characters'] = relationShip(back_populates = 'favorite_characters_by')

class FavoritePlanets(db.Model):
    __tablename__ = 'favorite_planet'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeingKey('user.id'))
    user: Mapped['User'] = relationShip(back_populates = 'favorite_planets_list')
    planet_id: Mapped[int] = mapped_column(ForeingKey('character.id'))
    planet: Mapped['Planets'] = relationShip(back_populates = 'favorite_planet_by')

class FavoriteStarships(db.Model):
    __tablename__ = 'Favorite_starship'
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeingKey('user.id'))
    user: Mapped['User'] = relationShip(back_populates = 'favorite_starships_list')
    starship_id: Mapped[int] = mapped_column(ForeingKey('characters.id'))
    starship: Mapped[list['FavoriteStarships']] = relationShip(backpopultes = 'favorite_starship_by')


class Characters(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    height: Mapped[str] = mapped_column(Integer(80))
    weight: Mapped[str] = mapped_column(Integer(80))
    favorite_character_by: Mapped[list['FavoriteCharacters']] = relationShip(back_populates = 'character')

class Planets(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    population: Mapped[str] = mapped_column(Integer(80))
    size: Mapped[str] = mapped_column(Integer(80))
    favorite_planet_by: Mapped[list['FavoritePlanets']] = relationShip(back_populates = 'planet') 

class Starships(db.Model):
    __tablename__ = 'starship'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(80),nullable=False)
    speed: Mapped[str] = mapped_column(Integer(80))
    size: Mapped[str] = mapped_column(Integer(80))
    favorite_startship_by: Mapped[list['FavoriteStarships']] = relationShip(backpopulates = 'starship')