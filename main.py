from flask import Flask


i = 0
app = Flask(__name__)

from av import *


@app.route('/user_form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Регистрация пользователя</title>
                          </head>
                          <body>
                            <h1>Регистрация</h1>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <input type="age" class="form-control" id="age" placeholder="Введите возраст" name="age">

                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>

                                    <button type="submit" class="btn btn-primary">Зарегестрироваться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['age'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/')
def carousel():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Добро пожаловать на сайт!</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
          crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
            crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css"
          href="{url_for('static', filename='css/style.css')}">
</head>   
<body>
    <div class="d-grid gap-2 d-md-flex justify-content-md-end">
  <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/login';">Войти</button>
  <button type="button" class="btn btn-secondary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/user_form';">Зарегистрироваться</button>
</div>
   </a>
</head>
<body>
    <h1>Добро пожаловать на сайт!</h1>
    <div id="carouselWithControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="{url_for('static', filename='img/pet_1.png')}" style="height: 30rem;" style="wight: 170rem;" alt="Pet 1">
          </div>
          <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_2.png')}" style="height: 30rem;" style="wight: 170rem;" alt="Pet 2">
          </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_3.png')}" style="height: 30rem;" style="wight: 170rem;" alt="Pet 3">
            </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_4.png')}" style="height: 30rem;" style="wight: 170rem;" alt="Pet 4">
          </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_5.png')}" style="height: 30rem;" style="wight: 170rem;" alt="Pet 5">
          </div>

       </div>
         <a class="carousel-control-prev" href="#carouselWithControls" role="button" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
   </a>
   <a class="carousel-control-next" href="#carouselWithControls" role="button" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
   </a>
</div>
</body>
</html>'''






if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
