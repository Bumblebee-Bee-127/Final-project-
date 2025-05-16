from flask import Flask, url_for, request

i = 0
app = Flask(__name__)

@app.route('/z')
def navigator(i):
    return '''<!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1,
    shrink-to-fit=no">
    <title>каталог</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <title>Привет, Яндекс!</title>
    </head>
    <body>
    <h1>Привет, Яндекс!</h1>
    <div class="alert alert-primary" role="alert">
    А мы тут компонентами Bootstrap балуемся
    </div>
    <div class="btn-group dropend">
   <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
      Dropend
   </button>
   <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Another action</a></li>
      <li><a class="dropdown-item" href="#">Something else here</a></li>
   </ul>
</div>
    </body>
    </html>'''
        



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
