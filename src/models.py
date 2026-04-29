from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
from sqlalchemy import Integer
from sqlalchemy import BigInteger

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=False, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[Optional[str]] = mapped_column(String(120), nullable=True, unique=False)
    terrain: Mapped[Optional[str]] = mapped_column(String(120), nullable=True, unique=False)
    population: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True, unique=False)
    diameter: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, unique=False)
    rotation_period: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, unique=False)
    orbital_period: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, unique=False)
    gravity: Mapped[Optional[str]] = mapped_column(String(50), nullable=True, unique=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "surface_water": self.surface_water,
            "description": self.description,
            "image_url": self.image_url
        }