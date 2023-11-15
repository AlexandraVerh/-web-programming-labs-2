from flask import Blueprint, render_template, redirect, request
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
    visibleUser = 'Anon' 
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

    

    conn = dbConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        error = "Пользователь с данным именем уже существует"

        dbClose(cur, conn)
        return render_template('register.html', error=error)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")
    conn.commit()
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
        conn.close()  # Закрытие соединения
        return render_template('login2.html', error=error)
    
    userID, hashPassword = result
    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        conn.close()  # Закрытие соединения
        return redirect("/lab5/")
    else:
        error=("Неправильный логин или пароль")
        return render_template("login2.html", errors=errors)