from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, \
    EmailField
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль',
                                   validators=[DataRequired()])
    surname = StringField('имя', validators=[DataRequired()])
    name = StringField('Фалимия', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    speciality = StringField('Номер телефона', validators=[DataRequired()])
    address = StringField('Адресс', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')