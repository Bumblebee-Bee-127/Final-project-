import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Pets(SqlAlchemyBase):
    __tablename__ = 'pets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    breed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    owner = sqlalchemy.Column(sqlalchemy.String,
                              sqlalchemy.ForeignKey("pet.id"))
    user = orm.relationship('User')


    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    #is_get = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    #name_image = sqlalchemy.Column(sqlalchemy.String, default=True)
    #data_image = sqlalchemy.Column(sqlalchemy.String, default=True)

    pets = orm.relationship("Pets", back_populates='user')

