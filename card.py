from flask import Flask, url_for, request

i = 0
app = Flask(__name__)

from users.convert_image import *

@app.route(f'/D')
def card():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card" style="width: 18rem;">
  <img src="{url_for('static', filename=f'picture/{}.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 1">
  <div class="card-body">
    <h5 class="card-title"></h5>
    <p class="card-text"></p>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Кличка: {2}</li>
    <li class="list-group-item">Вид: {2}</li>
    <li class="list-group-item">Порода: {2}</li>
    <li class="list-group-item">Возраст: {2}</li>
  </ul>
  <div class="card-body">
    <button type="button" class="btn btn-primary btn-lg" onclick="window.location = 'http://127.0.0.1:8080/info';">дополнительно</button>  
  </div>
</div>
</div>
</body>
</html>'''


@app.route(f'/info')
def card_d():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card">
  <div class="card-header">   
  <div class="card-body">
    <h5 class="card-title">Дополнительная информация о {''}</h5>
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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
