from flask import Flask, url_for, request

i = 0
app = Flask(__name__)

@app.route(f'/')
def card():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card" style="width: 18rem;">
  <img src="{url_for('static', filename='img/pet_2.png')}" style="width: 48rem;" class="card-img-top" alt="Pet 1">
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
    <a href="#" class="card-link">Дополнительная информация</a>  
  </div>
</div>
</div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
