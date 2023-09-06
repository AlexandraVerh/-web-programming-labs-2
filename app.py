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
        
        <a href="/menu" target="_blank" >Меню</a>

        <h2>Реализованные роуты</h2>
        <ul>
            <li>
                <a href="/lab1/g" target="_blank" >/lab1/g - дуб</a>
            </li>
            <li>
                <a href="/lab1/student" target="_blank" >/lab1/student - студент</a>
            </li>
            <li>
                <a href="/lab1/python" target="_blank" >/lab1/python - питон</a>
            </li>
            <li>
                <a href="/lab1/kot" target="_blank" >/lab1/kot - Коты</a>
            </li>
        </ul>
        

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
@app.route('/lab1/student')
def student():
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

        <h1>Верхозина Александра Андреевна</h1>
        
        <img src="'''+ url_for('static', filename='logo.png')+'''" >

        <footer>
            &copy; Верхозина Александра, ФБИ-14, 3 курс,2023 год
        </footer>
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
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

        <h1>Python</h1>

        <p>
        Задумка по реализации языка появилась в конце 1980-х годов, а разработка его реализации началась в 1989 году 
        сотрудником голландского института CWI <b>Гвидо ван Россумом</b>. 
        Для распределённой операционной системы Amoeba требовался расширяемый скриптовый язык,
        и Гвидо начал разрабатывать Python на досуге, позаимствовав некоторые наработки для языка ABC 
        (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). 
        В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. 
        С самого начала Python проектировался как объектно-ориентированный язык.
        </p>
        
        <img src="'''+ url_for('static', filename='pyt.jpg')+'''" >
        <div>

        <p>
        Гвидо ван Россум назвал язык в честь популярного британского комедийного телешоу 1970-х <i>«Летающий цирк Монти Пайтона»</i>, 
        поскольку автор был поклонником этого телешоу, как и многие другие разработчики того времени, 
        а в самом шоу прослеживалась некая параллель с миром компьютерной техники.
        </p>

        <p>
        Наличие дружелюбного, отзывчивого сообщества пользователей считается, наряду с дизайнерской интуицией Гвидо, 
        одним из факторов успеха Python. Развитие языка происходит согласно чётко регламентированному процессу создания, 
        обсуждения, отбора и реализации документов PEP <i>(англ. Python Enhancement Proposal)</i> — предложений по развитию Python.
        </p>

        <p>
        3 декабря 2008 года, после длительного тестирования, вышла первая версия Python 3000 
        (или Python 3.0, также используется сокращение Py3k). В Python 3000 устранены многие недостатки архитектуры с максимально возможным 
        (но не полным) сохранением совместимости со старыми версиями Python.
        </p>

        <p>
        Дата окончания срока поддержки Python 2.7 первоначально была установлена на 2015 год, 
        а затем перенесена на 2020 год из опасения, что большая часть существующего кода не может быть легко перенесена на Python 3. 
        Поддержка Python 2 была направлена лишь на уже существующие проекты, новые проекты должны были использовать Python 3. 
        Официально Python 2.7 не поддерживается с 1 января 2020 года, хотя последнее обновление вышло в апреле 2020. 
        Больше никаких исправлений безопасности или других улучшений для Python 2.7 не будет выпущено.
        С окончанием срока службы Python 2.x поддерживаются только Python 3.6.x и более поздние версии.
        </p>

        </div>
        <img src="'''+ url_for('static', filename='py.jpg')+'''" >
        <footer>
            &copy; Верхозина Александра, ФБИ-14, 3 курс,2023 год
        </footer>
    </body>
</html>
'''   
@app.route('/lab1/kot')
def kot():
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

        <h1>Презентация котов</h1>

        <p>
        Здравствуйте. Раз этот роут был на свободную тему, то я решила познакомить Вас со своими котами. На первом фото, которое представлено ниже, 
        изображен мой кот по кличке Мартин, два года назад я забрала его из приюта и теперь он радует меня каждый день. У него много смешных фотографий
        и вообще он очень мягкий и добрый!
        </p>
        
        <img src="'''+ url_for('static', filename='mar.jpg')+'''" >

        <p>
        Следующим героем является моя вторая кошка по кличке Кишка (ударение на и). Она младше Мартина и немного противная. Ее мы спасли с СТО в январе
        и теперь у меня дома в два раза больше шерсти.
        </p>

        <img src="'''+ url_for('static', filename='kis.jpg')+'''" >

        <div>
        <p>
        Спасибо, что посмотрели, надеюсь они вам понравились!
        </p>
        </div>

        <footer>
            &copy; Верхозина Александра, ФБИ-14, 3 курс,2023 год
        </footer>
    </body>
</html>
'''