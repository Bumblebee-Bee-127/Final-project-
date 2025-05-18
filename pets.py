import datetime
import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from flask import Flask

from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

from data import db_session

SqlAlchemyBase = orm.declarative_base()
__factory = None

class Pets(SqlAlchemyBase):
    __tablename__ = 'pets'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    breed = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_get = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    name_image = sqlalchemy.Column(sqlalchemy.String, default=True)
    data_image = sqlalchemy.Column(sqlalchemy.String, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("pet.id"))
    user = orm.relationship('User')

    news = orm.relationship("Pets", back_populates='user')


def main():
    pet = Pets(name="Луна", type="кошка", breed="Сиамская",
               information="something", age = '3 года', name_image="pet_1",
               data_image="/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5"
                          "PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAJYA"
                          "yADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0K"
                          "xwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKzt"
                          "LW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQ"
                          "J3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhY"
                          "aHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDjiKYBk5p7eg70FdoqRD"
                          "X4FQMMDPTFPdiRzS29q97dRwpzk8/SmkDNrw3pzO5unHy/w11gCohc8AVHaW629ukSDAUYqK+m2rsB4XljVMkyNYvfLiY5+d+APSuMvJdq8dTxWnqV39onZs/KOBWTbobq"
                          "73H7inihIDS0TTmlkRQPmJy1d5cyx6PpRIwNq4Ue9VPD2neRB50ijew4+lY3ibUPtN39nRv3cf6mm+wkrsw5C9zcl25dzk10enWgiiWszS7TzJN5HHauiCbQMdqBjXwBVOQ5"
                          "JqxK+BWfPMIhyRg0hjJCDnjpUUS5Jkx9KY9zE2FEi8+9Ss6BMKQRjtQMq3LgA1Qxxk96nnbfJt7d6i6mkMRV71IFpQMU5VpiBVqRUpVWpVWgB0MWW9hVhhgZxTo02J71Debh"
                          "ASpx6mm9ECMa7nY3AAXGKjLhSOhz+lWXhjMhaRwfcVVkiEcjZYHiuV7nVG1rCXI3tujGCcZHpUZfeVj6LnOB61E8pV1GaViAVZep7Uihsm5pSeidDSbFjkSSPnsQaf8AKdxyc9"
                          "QO1RynaQQMqeooTCw6aQBAcck0xWEgDOMEUxSSAffoabcsI4w3KgdPeiwdCpqN55S+Wo5IrIVSxyadM7Szszdc0i9elbxVkc8ndkyRg8YxSSw4GR+tSxBifu/nVieMmPmmIqWUvlbg"
                          "eg5rZtUM67THnjNYtrGHutrdK6K0YRv5acCs5mkNiWLT1ZGcJj6dqnhiS2XDA7c5zU8cCrG7IxyTnk1IkYmj3buB1FZ3NRCd4UsMjsaqGMsHKjKKevpV3YNh28H+lV5QxVgpwCOlBSI"
                          "htdGAHzdh6VCd8b5cAgnJ9qkkdgwZc4IxUwjDxZ5YdPekA3aFHygDd0qMJtfnIPrT2jdkO7AI4FSCPfhMZbFA7lVkMnygc9z6U/yzny2wcdGq1FDsyc8nk1JFAhZ1BDq3Iz2osJsqMoi"
                          "cBvqKsytxnB9896bcKQwXg/0qWYMEUEE4HPvTAqSRgxnBGG/nT4flhaJV3Hv9atkRPGCF24HAPrSQL5Tu7HHfI/lSsFyoSZHVTxgYoAILl1PHAqyFSRi3Az2qGRWErAkhc8UAUppSsgXr"
                          "mnK4D45HvT5ACeB84700tuxjrQgaJkIEo+QHJ6mkuFbyztHfp6VIi/KM/LjmhQpcuWGMdDTEQMrbgAM5FPijVFBzluwIqRHBZXBwCcYpZIw2fmHtSGRAlmAPygDBqMAtIAByBzUpxjk/N"
                          "jgD1p7wpHKCsm07cN9aAI1kZV2MM46eoppYEsqIMcE4pfMYNvA5A5xSqRjI+93I9KAsCERXO8D5QOtJGrJvkJ2+nvUm75AGAJ6j6UkzMXDcbQOlFwsNB2nY3K+tP8tVKhDwcioCMShv4T"
                          "3qwVy5YnB7c0DY2EEF1YZYcYFQ7FDDOdwOfwqRGIuAxb5s0932jORvDdPSgRFKRIWXHPrUU1o8saFXxu6jPapxyhJGGPY0xnKFWIAOaaYmii6rpwKq7mMgkH0NVba++0zgTybUHJxWruW"
                          "43qxBVulQTaHaQ2PyHM5y27Paq0I2Lny/ZAU6H7uetNCBW+Z9pYVzjX0yKi5YBOlakF3HLb5bJYYwKGmNFsKzEgEBf600Rndw3zE8VJAcrv2kP71CTmTJ4x2qNix8kjqxOevX2p+R5Qy"
                          "wyahk3eX5noeR7U6P98SyL8mKYh0cR2NuYVAtoJRtzk9AKskMkfOKjVW35XgZoQmh4j2RJgD5aDcRmQIwKkc/WpBHujGDmmThWGNoBOOfSh7ghroGQ87T2quYxhe471JOXwFUZwMCkH"
                          "youRn1oAjMeFAx3zTPK4xnpU+CycVGwby85GAaYiPyiMgtxSKvz8YPbFPGX4HpmmxqSwPOelNCIpIcOM9+tSFBsxUz43qG5wKJQu0uDxnFMkrrHnntTvKPVTk/yp8exy+TTgQmT69q"
                          "AIhgjp0qNt2MjpTg/mTBVxgUkoZlIB6noKYmSwHcqepNXwvFZlluEm09hWmGzWiRi9xdtLtoBpwqhGiF5of7uKkxgVHJyKkCqwNdV4Z00xQm5kHzv0z2FY2l2JvrxVx8g5au6SMRIq"
                          "KMADFUiWJIwij3flXMa1eFEMSn5m5atfUbxURmJ+VBx71xN5cmV3kc0gKN3KfuL95uK2/D+mGaZEwNo5asWxhNzcGUjPOFr0nRbBbOyDMArt8zVa0ELqt6um6UcECRhtUVwaK082D"
                          "kljzWnr+oG+viqn91HwtJpNoWfzCKSK2NWxtxFCBirMhxT8bVxUEpOMCgRWmOVJzXDeJNbeOVrWIjp8xrtpTwRXlGq5bV7nP/AD0NSykVzcTMc+Y351NFfXsBBjuJBjoM0sNuWAPap"
                          "/swx0pFWLdp4jdTtukzn+Na37aeK5j82Jgyn0rjpLf2ptvc3Gny74WI9VPQ00xNHeAU9RWdpmqQ6jFlTtkX7yHrWoopiHqtWIY8t7Co1FXIk2pnuaaAUiq16wS1YnpVs1RvnV4HjZ"
                          "cjvnpSk9AitTCWdZTJ5OCAOhqMb3iDSDkdD60qoinbFhWU4+tJ56RnY7dSRj0Ncp2bbDF27FdkBIPX0qORUaTckmeM1IzBdw4O7oaqKyqdp+U7sUwsPYujKARt71IpyxB5FJgSYzx"
                          "jiogCj57DqaQErxkyk4xgdD3rI1S9O5Yl6qcmtC8vHhiVuCuDz3rnQxkkaV+ec/jWkI63M6ktLBjjnqakTIHpTFBY5NXYoNy9PxrQxHWz7fm4NWRKJFPH4UxbMKM5+lOVcIeRkUFI"
                          "pxKBegdq1bVt0rLgnHesiLJvk571u2sTRvu456+9ZzNKZpRSEgAjkCp0UsmUJDH1qGCNXyzZJ7YNKf3cqhw2FrI2J3JEIiLfNjP41A0hJLFQx9u9WDxjjIxnNRZKnHr3x0oAZGvIcq"
                          "NmfypTtTqCQOTUmV8ogjOOaaFjddu3qMg5piGNGXZW3YU8mncDDqeRkcd6aI2wYwTkDAPXimQxSwKSeec80AWkbEYLcMRk0wyFsdiRgAVHvdiS2MN0Udqcrsl0oYcKMgj1oGSrGXA"
                          "JHK8+9S8lgxPykd+1N2eW4mjY89cnvTXmLDyyoIoELtDuWJ4HGB/OmkuZVRTu/ve9Oj3QpgDkjnNRhdzg7treooGJNAHnXy2w2M9aLiQsu3btUDn1qFUl83dnC9jU7ZdSX4boKQIq"
                          "HoAnHGCTTUjG1n/hHA9zTp1KxHcMMO1IA/lhsH5j0oGPG1YgxJAPrT0ljlU/Jk44+tMlKmVUC5A6A96RcREHBAJ+YCmIdxhMkAk84pbUbXkYnew7H0qHd+9VlGNh/CrCRyK4yMhgea"
                          "EDGRIiSjPJPzH2ouJFnkDNkAjAxTCp3nPG4dKmYKttGzcFTkikGxEqAExhuCOtCqIt65+frT1kyr+WORgGkXErnIIyMkn1oC4kIk2gkBmJ/Klk8vaCTjPFKjx5O4kHFRbeCAcgfpQA"
                          "6bIiVV4XG4CmKxikVjghSM/SpSFDgMeWxRJGkbN84OeOneiwAI9zmbA5OQKilOH3kfUVKA6ofm7YWmL+8ZN/OaAESRWjwSRgcGorhsnGMripWgAnwpyPT0odQWAPLDqKAIolVR8pBG"
                          "M05gcFjyvSneUVYgY3GnlMQjA4znJpgV2ghm2xkDJxkgdKkFpDaiWTyx93j2NDJ0YKdpOMinGRhEy9QRjBp3JcTJ/",
                user_id=1, is_get=False)
    db_sess.add(pet)
    db_sess.commit()

if __name__ == '__main__':
    main()
