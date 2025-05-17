from flask import Flask, url_for, request

i = 0
app = Flask(__name__)


from user_form import *

@app.route('/m')
def navigator():
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
  <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/';">Выйти</button>
  <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/';">Добавить питомца</button>
</div>
<div class="card" style="width: 20rem;">
  <img src="{url_for('static', filename=f'pictures/cat_1.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 1">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text"></p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: Луна</li>
    <li class="list-group-item">Вид: кошка</li>
    <li class="list-group-item">Порода: Сиамская</li>
    <li class="list-group-item">Возраст: 3 года</li>
  </ul>
  <div class="card-body">
    <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/info1';">дополнительно</button>  
  </div>
</div>
<div class="card" style="width: 20rem;">
  <img src="{url_for('static', filename=f'pictures/cat_2.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 2">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text"></p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: Маня</li>
    <li class="list-group-item">Вид: кошка</li>
    <li class="list-group-item">Порода: отсутствует</li>
    <li class="list-group-item">Возраст: 4 года</li>
  </ul>
  <div class="card-body">
    <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/info2';">дополнительно</button>  
  </div>
</div>
<div class="card" style="width: 20rem;">
  <img src="{url_for('static', filename=f'pictures/dog_1.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 3">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text"></p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: Лола</li>
    <li class="list-group-item">Вид: собака</li>
    <li class="list-group-item">Порода: Австралийская овчарка</li>
    <li class="list-group-item">Возраст: 2 года</li>
  </ul>
  <div class="card-body">
    <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/info3';">дополнительно</button>  
  </div>
</div>
</body>
</html>'''

@app.route(f'/D')
def card(im, name, type, breed, age):
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card" style="width: 20rem;">
  <img src="{url_for('static', filename=f'pictures/{im}.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 1">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text"></p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: {name}</li>
    <li class="list-group-item">Вид: {type}</li>
    <li class="list-group-item">Порода: {breed}</li>
    <li class="list-group-item">Возраст: {age}</li>
  </ul>
  <div class="card-body">
    <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/info';">дополнительно</button>  
  </div>
</div>
</div>
</body>
</html>'''


@app.route(f'/info1')
def card_1():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card">
  <div class="card-header">   
  <div class="card-body">
    <h5 class="card-title">Дополнительная информация</h5>
    </div>
    </div>
  <ul class="list-group list-group-flush">
     <li class="list-group-item">Кличка: Луна</li>
    <li class="list-group-item">Вид: кошка</li>
    <li class="list-group-item">Порода: Сиамская</li>
    <li class="list-group-item">Возраст: 3 года</li>
  </ul>

   <div class="card-body">
    <p class="card-text">Немного и питомце: {'something'}</p>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/m';">Забрать!</button>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/m';">назад</button>
  </div>
</div>
</div>
</body>
</html>'''


@app.route(f'/info2')
def card_2():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card">
  <div class="card-header">   
  <div class="card-body">
    <h5 class="card-title">Дополнительная информация</h5>
    </div>
    </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: {2}</li>
    <li class="list-group-item">Вид: {2}</li>
    <li class="list-group-item">Порода: {2}</li>
    <li class="list-group-item">Возраст: {2}</li>
  </ul>

   <div class="card-body">
    <p class="card-text">Немного и питомце: {'something'}</p>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/b';">Забрать!</button>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/';">назад</button>
  </div>
</div>
</div>
</body>
</html>'''


@app.route(f'/info3')
def card_3():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card">
  <div class="card-header">   
  <div class="card-body">
    <h5 class="card-title">Дополнительная информация</h5>
    </div>
    </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: Лола</li>
    <li class="list-group-item">Вид: собака</li>
    <li class="list-group-item">Порода: Австралийская овчарка</li>
    <li class="list-group-item">Возраст: 2 года</li>
  </ul>

   <div class="card-body">
    <p class="card-text">Немного и питомце: {'something'}</p>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/b';">Забрать!</button>
    <button type="submit" class="btn btn-primary" onclick="window.location = 'http://127.0.0.1:8080/';">назад</button>
  </div>
</div>
</div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
