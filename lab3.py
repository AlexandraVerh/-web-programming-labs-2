from flask import Blueprint, redirect, url_for, render_template
lab3 = Blueprint('lab3',__name__)

@lab3.route("/lab3/")
def lab():
    return redirect("/lab3/form1")


@lab3.route("/lab3/form1")
def form1():
    return render_template('lab3.html')

