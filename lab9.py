from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9',__name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
   
        return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error.html'), 404

# Обработчик ошибки 500
@lab9.app_errorhandler(500)
def internal_server_error(e):
    return render_template('lab9/error500.html'), 500

# Роут, вызывающий ошибку 500
@lab9.route('/lab9/500')
def trigger_internal_server_error():
    raise Exception('Internal Server Error')