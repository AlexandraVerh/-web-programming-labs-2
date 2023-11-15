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