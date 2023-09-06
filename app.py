from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctupe html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>web-сервер на flask</h1>

        <ol>
            <a href="/lab1" target="_blank" >Первая лабораторная</a>
        </ol>

        <footer>
            &copy; Верхозина Александра Андреевна, ФБИ-14, 3 курс,2023
        </footer>
    </body>
</html>
"""

@app.route("/lab1")
def lab1():
    return """
<!doctupe html>
<html>
    <head>
        <title>Верхозина Александра Андреевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>

        <p>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>

        <footer>
            &copy; Верхозина Александра, ФБИ-14, 3 курс,2023 год
        </footer>
    </body>
</html>
"""
@app.route('/lab1/g')
def g():
    return '''
<!doctype html>
<html>
    <head>
        <title>Верхозина Александра Андреевна, лабораторная 1</title>
    </head>
    <body>
    <link rel="stylesheet"  href="'''+ url_for('static', filename='lab1.css')+'''">
         <header>
            НГТУ, ФБ, Лабораторная работа 1
         </header>

        <h1>Дуб</h1>
        <img src="'''+ url_for('static', filename='g.jpg')+'''" >

        <footer>
            &copy; Верхозина Александра, ФБИ-14, 3 курс,2023 год
        </footer>
    </body>
</html>
'''

    