from flask import redirect, Blueprint, render_template, request
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from flask import url_for

lab6 = Blueprint('lab6',__name__)

@lab6.route("/lab6/")
def lab6_view():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "Аноним"

    return render_template("lab6.html", username=username)

@lab6.route("/lab6/check")
def main():
    #То же самое, что select * from users
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/checkarticles")
def checkarticles():
    all_articles = articles.query.all()
    print(all_articles)
    return "result in console!"

@lab6.route("/lab6/register", methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template("register2.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    # Проверка пустого имени пользователя
    if not username_form:
        error = "Пустое имя!"
        return render_template("register2.html", error=error)

    # Проверка длины пароля
    if len(password_form) < 5:
        error = "Пароль должен содержать не менее 5 символов!"
        return render_template("register2.html", error=error)

    # Проверка наличия пользователя с таким именем
    existing_user = users.query.filter_by(username=username_form).first()
    if existing_user:
        error = "Пользователь с таким именем уже существует!"
        return render_template("register2.html", error=error)

    # Создание нового пользователя
    hashed_password = generate_password_hash(password_form, method="pbkdf2")
    new_user = users(username=username_form, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login3.html")

    username_form = request.form.get("username")
    password_form = request.form.get("password")

    if not username_form or not password_form:
        error = "Поле имя и/или пароль не заполнено"
        return render_template("login3.html", error=error)

    my_user = users.query.filter_by(username=username_form).first()

    if my_user is None:
        error = "Пользователь не существует"
        return render_template("login3.html", error=error)

    if not check_password_hash(my_user.password, password_form):
        error = "Неправильный пароль"
        return render_template("login3.html", error=error)

    login_user(my_user, remember=False)
    return redirect("/lab6/articles")


@lab6.route("/lab6/articles")
@login_required
def article_list():
    my_articles = articles.query.filter_by(user_id=current_user.id).all()
    return render_template("list_articles.html", articles=my_articles)

@lab6.route("/lab6/add_article", methods=['GET', 'POST'])
@login_required
def add_article():
    if request.method == "GET":
        return render_template("add_article.html")

    title_form = request.form.get("title")
    text_form = request.form.get("text")

    # Создание новой статьи
    new_article = articles(user_id=current_user.id, title=title_form, article_text=text_form)
    db.session.add(new_article)
    db.session.commit()

    return redirect(url_for("lab6.article_list"))


@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/")


@lab6.route("/lab6/article/<int:article_id>")
@login_required
def view_article(article_id):
    article = articles.query.get(article_id)
    if not article:
        return "Статья не найдена"
    return render_template("article_details.html", article=article)
