from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, redirect, request, session
import psycopg2

rgz = Blueprint('rgz',__name__)

def dbConnect(): 
    conn = psycopg2.connect( 
        host="127.0.0.1", 
        database = "rgz_web", 
        user = "aleksandra_rgz_web", 
        password = "1235") 
 
    return conn; 
 
def dbClose(cursor,connection): 
    #закрываем курсор и соединение. порядок важен
    cursor.close() 
    connection.close() 

@rgz.route("/rgz/") 
def main(): 
    visibleUser = session.get('username', 'Anon') 
    # Прописываем параметры подключения к БД 
    conn = psycopg2.connect( 
        host="127.0.0.1", 
        database="rgz_web", 
        user="aleksandra_rgz_web", 
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
 
    return render_template('rgz.html', username=visibleUser)
    
@rgz.route('/rgz/users')
def users():
    conn = psycopg2.connect(
        host="127.0.0.1", 
        database = "rgz_web", 
        user = "aleksandra_rgz_web", 
        password = "1235"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('rgzusers.html', users=result)

@rgz.route('/rgz/register', methods=['GET', 'POST'])
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

    return redirect("/rgz/login")

@rgz.route('/rgz/login', methods=['GET', 'POST'])
def loginPage():
    error = ''

    if request.method == 'GET':
        return render_template('login.html', error=error)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        error="Пожалуйста, заполните все поля"
        return render_template('login.html', error=error)

    conn = dbConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")
    result = cur.fetchone()

    if result is None:
        error="Неправильный логин или пароль"
        dbClose(cur,conn)  # Закрытие соединения
        return render_template('login.html', error=error)
    
    userID, hashPassword = result
    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur,conn)  # Закрытие соединения
        return redirect("/rgz/")
    else:
        error ="Неправильный логин или пароль"
        return render_template("login.html", error=error)
    
@rgz.route("/rgz/logout")
def logout():
    session.clear()
    return redirect("/rgz/login")