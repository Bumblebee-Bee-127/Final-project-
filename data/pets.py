import datetime
import sqlalchemy
from sqlalchemy import orm

from db_session import SqlAlchemyBase


class Pets(SqlAlchemyBase):
    __tablename__ = 'pets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    breed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_get = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    name_image = sqlalchemy.Column(sqlalchemy.String, default=True)
    data_image = sqlalchemy.Column(sqlalchemy.String, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("pet.id"))
    user = orm.relationship('User')

    news = orm.relationship("Pets", back_populates='user')

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
