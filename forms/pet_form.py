from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/pet_form', methods=['POST', 'GET'])
def pet_form():
    if request.method == 'GET':

        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Регистрация</title>
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
<h2>Анкета для регистрации</h2>
<h3>вашего питомца</h3>

<div>
    <form class="login_form" method="post" enctype="multipart/form-data">
        <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите кличку" name="name">
        <input type="text" class="form-control" id="vid" aria-describedby="vidHelp" placeholder="Введите вид животного" name="vid">
        <input type="text" class="form-control" id="poroda" aria-describedby="porodaHelp" placeholder="Введите породу" name="poroda">
        <input type="digit" class="form-control" id="year" aria-describedby="yearHelp" placeholder="Введите возрат животного" name="year">
        <div class="form-group">
            <label for="classSelect">Как скоро Вы хотите отдать питомца?</label>
            <select class="form-control" id="classSelect" name="class">
              <option>В течении нескольких недель</option>
              <option>В течении месяца</option>
              <option>В течении года</option>
              <option>Мне всё равно</option>
              <option>Другое</option>
            </select>
        </div>
        <div>
            
        <div class="form-group">
            <label for="form-check">Укажите пол питомца</label>
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
        <div class="form-group">
            <label for="about">Почему Вы хотите Отдать питомца?</label>
            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию питомца</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>

        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Вы хороший человек?</label>
    </div>
    <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</div>
</body>
</html>'''
    elif request.method == 'POST':
        print(request.form)
        return Успешно!



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
