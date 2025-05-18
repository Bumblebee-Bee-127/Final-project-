from data import db_session
from data.user import User

db_session.global_init("db/blogs.db")

session = db_session.create_session()

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.number = "88005553535"
user.address = "somewhere"
user.email = "scott_chief@mars.org"
user.hashed_password = "cat"
session.add(user)