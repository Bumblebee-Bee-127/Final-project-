import datetime
import sqlalchemy
from sqlalchemy import orm

from db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'pets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("pet.id"))
    user = orm.relationship('User')

    news = orm.relationship("Pets", back_populates='user')

