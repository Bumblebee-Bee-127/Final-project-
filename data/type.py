import sqlalchemy
from db_session import SqlAlchemyBase


class Type(SqlAlchemyBase):
    __tablename__ = 'type'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    association_table = sqlalchemy.Table(
        'association',
        SqlAlchemyBase.metadata,
        sqlalchemy.Column('pets', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('pets.id')),
        sqlalchemy.Column('type', sqlalchemy.Integer,
                          sqlalchemy.ForeignKey('type.id')))

    categories = orm.relationship("Type",
                                  secondary="association",
                                  backref="pets")