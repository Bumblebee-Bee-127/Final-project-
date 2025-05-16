from flask import Flask, url_for, request

i = 0
app = Flask(__name__)

@app.route(f'/')
def card_d():
    return f'''<!DOCTYPE html>
        <html lang="en">
        <head>
        <body>
       <div class="card">
  <div class="card-header">   
  </div>
  <div class="card-body">
    <h5 class="card-title">Дополнительная информация о {''}</h5>
    </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item">Номер владельца: {2}</li>
    <li class="list-group-item">Почта: {2}</li>
  </ul>
    <p class="card-text">Немного и питомце: {'something'}</p>
    <a href="#" class="btn btn-primary">Забрать!</a>
  </div>
</div>
<div class="card w-75 mb-3">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
    <a href="#" class="btn btn-primary">Button</a>
  </div>
</div>
</div>
</body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
