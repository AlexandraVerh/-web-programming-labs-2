from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, redirect, request, session
import psycopg2

lab5 = Blueprint('lab5',__name__)

def dbConnect(): 
    conn = psycopg2.connect( 
        host="127.0.0.1", 
        database = "knowledge_base", 
        user = "aleksandra_knowledge_base", 
        password = "1235") 
 
    return conn; 
 
def dbClose(cursor,connection): 
    #закрываем курсор и соединение. порядок важен
    cursor.close() 
    connection.close() 

@lab5.route("/lab5/") 
def main(): 
    visibleUser = session.get('username', 'Anon') 
    # Прописываем параметры подключения к БД 
    conn = psycopg2.connect( 
        host="127.0.0.1", 
        database="knowledge_base", 
        user="aleksandra_knowledge_base", 
        password="1235", 
        port = 5432
    ) 
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы 
    cur = conn.cursor() 
    # Пишем запрос, который курсор должен выполнить 
    cur.execute("SELECT * FROM users;") 
    # fetchall - получить все строки, которые получились в результате выполнения SQL-запроса в execute 
    # Сохраняем эти строки в переменную result 
    result = cur.fetchall() 
 
    # Закрываем соединение с БД 
    cur.close() 
    conn.close() 
 
    print(result) 
 
    return render_template('lab5.html', username=visibleUser)
    
@lab5.route('/lab5/users')
def users():
    conn = psycopg2.connect(
        host="127.0.0.1", 
        database = "knowledge_base", 
        user = "aleksandra_knowledge_base", 
        password = "1235"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('lab5users.html', users=result)

@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    error = ''

    if request.method == 'GET':
        return render_template('register.html', error=error)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        error="Пожалуйста, заполните все поля"
        print(error)
        return render_template('register.html', error=error)

    hashPassword = generate_password_hash(password)

    conn = dbConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:#не получаем ббольше одной строки только один пользователь может быть с таким именем
        error = "Пользователь с данным именем уже существует"

        dbClose(cur, conn)
        return render_template('register.html', error=error)
    
    #сохраняем пароль в вижде хэша в бд
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")
    conn.commit()#фиксируем изменения
    dbClose(cur, conn)

    return redirect("/lab5/login")

@lab5.route('/lab5/login', methods=['GET', 'POST'])
def loginPage():
    error = ''

    if request.method == 'GET':
        return render_template('login2.html', error=error)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        error="Пожалуйста, заполните все поля"
        return render_template('login2.html', error=error)

    conn = dbConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")
    result = cur.fetchone()

    if result is None:
        error="Неправильный логин или пароль"
        dbClose(cur,conn)  # Закрытие соединения
        return render_template('login2.html', error=error)
    
    userID, hashPassword = result
    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)  # Закрытие соединения
        return redirect("/lab5/")
    else:
        error ="Неправильный логин или пароль"
        return render_template("login2.html", error=error)
    
@lab5.route("/lab5/new_article", methods=["GET", "POST"])
def createArticle():
    error = ''
    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("new_article.html")
        
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")
        
            if len(text_article) == 0:
                error="Заполните текст"
                return render_template("new_article.html", error=error)
        
            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id, title, article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")
            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur,conn)

            return redirect(f"/lab5/articles/{new_article_id}")
    return redirect("/lab5/login")

@lab5.route("/lab5/articles/<string:article_id>")#все нечисловые символы пока
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s", (article_id, userID))

        articleBody = cur.fetchone()#берет одну строку

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found!"
        
        #разбить статью на параграфы
        text = articleBody[1].splitlines()

        return render_template("articleN.html", article_text=text,
        article_title=articleBody[0], username=session.get("username"))
    
@lab5.route("/lab5/article_list")
def getArticleList():
    userID = session.get("id")
    username = session.get("username")
    articles_list = "Нет статей"
    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()
        
        cur.execute(f"SELECT id, title FROM articles WHERE user_id = {userID}")
        articles_list = cur.fetchall()

    return render_template("article_list.html", articles_list=articles_list, username=username)


@lab5.route("/lab5/logout")
def logout():
    session.clear()
    return redirect("/lab5/login")


