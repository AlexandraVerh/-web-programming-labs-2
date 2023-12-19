from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9',__name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        sender_name = request.form.get('sender_name')
        recipient_gender = request.form.get('recipient_gender')
        recipient_name = request.form.get('recipient_name')

        return redirect(url_for('lab9.card', sender_name=sender_name, recipient_gender=recipient_gender, recipient_name=recipient_name))
    else:
        return render_template('lab9/index.html')


@lab9.route('/lab9/card', methods=['GET'])
def card():
    sender_name = request.args.get('sender_name')
    recipient_gender = request.args.get('recipient_gender')
    recipient_name = request.args.get('recipient_name')

    return render_template('lab9/card.html', sender_name=sender_name, recipient_gender=recipient_gender, recipient_name=recipient_name)

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