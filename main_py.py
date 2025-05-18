from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user, logout_user, current_user

from data import db_session
from data.pets import Pets
from data.user import User
from forms.user import RegisterForm, LoginForm
from forms.pet_form import Petaddform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title="Главная")


@app.route('/pets')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('pets.html', title="Работы", jobs=jobs)


@app.route('/pet_add', methods=['GET', 'POST'])
def job_add():
    db_sess = db_session.create_session()
    form = JobAddForm()
    form.team_leader.choices = [str(user) for user in db_sess.query(User).all()]
    if form.validate_on_submit():
        job = Jobs(
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        job.user = db_sess.query(User).filter(User.email == form.team_leader.data.split()[-1]).first()
        db_sess.add(job)
        db_sess.commit()
        return redirect('/pets')
    return render_template('pet_register.html', title='Создание работы', form=form)


@app.route('/register_user', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user)
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
