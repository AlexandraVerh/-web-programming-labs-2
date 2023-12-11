from flask import Blueprint, render_template, redirect, request, session

lab7 = Blueprint('lab7',__name__)

@lab7.route("/lab7/") 
def main():
     return render_template('lab7/index.html')

@lab7.route('/lab7/drink')
def drink():
     return render_template('lab7/drink.html')