from data import db_session
from data.pets import Pets

db_session.global_init("db/blogs.db")

session = db_session.create_session()

pet = Pets()
pet.name = "Лили"
pet.type = 'кошка'
pet.breed = 'Сиамская'
pet.owner = '2, 3'
pet.age = 2
session.add(pet)

session.commit()