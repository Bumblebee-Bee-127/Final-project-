from flask import Flask, url_for, request

i = 0
app = Flask(__name__)

from user_form import *
from av import *
from card import card


@app.route('/')

@app.route('/index')
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
  <button type="button" class="btn btn-primary">Primary</button>
  <button type="button" class="btn btn-secondary">Secondary</button>
</div>
   </a>
</head>
<body>
    <h1>Добро пожаловать на сайт!</h1>
    <div id="carouselWithControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="{url_for('static', filename='img/pet_1.png')}" class="d-block w-100" alt="Pet 1">
          </div>
          <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_2.png')}" class="d-block w-100" alt="Pet 2">
          </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_3.png')}" class="d-block w-100" alt="Pet 3">
            </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_4.png')}" class="d-block w-100" alt="Pet 4">
          </div>
           <div class="carousel-item">
            <img src="{url_for('static', filename='img/pet_5.png')}" class="d-block w-100" alt="Pet 5">
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

@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/123.jpg')}"
    alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/i')
def show_i():
    global i
    i += 1
    return str(i)


@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
    <html lang="en">
    <head>
    <some static>
    <title>Привет, {username}</title>
    </head>
    <body>
    <h1>Привет, {username}!</h1>
    </body>
    </html>'''


@app.route('/two_params/<username>/<int:number>')
def two_params(username, number):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Пример с несколькими параметрами</title>
</head>
<body>
<h2>{username}</h2>
<div>Это первый параметр и его тип: {str(type(username))[1:-1]}</div>
<h2>{number}</h2>
<div>Это второй параметр и его тип: {str(type(number))[1:-1]}</div>
</body>
</html>'''





@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return login()



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
