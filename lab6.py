from flask import redirect, Blueprint, render_template, request
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user
from flask import url_for

lab6 = Blueprint('lab6',__name__)

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