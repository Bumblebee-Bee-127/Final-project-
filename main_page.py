from flask import Flask, url_for, request

i = 0
app = Flask(__name__)


from card import *

@app.route('/z')
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
</body>
</html>'''

@app.route('/z')
def navigator_2():
    for i in range(4):
        return card()
        
@app.route("/index")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
