from flask import Blueprint, render_template, request

lab7 = Blueprint('lab7',__name__)


@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


@lab7.route('/lab7/drink')
def drink():
    return render_template('lab7/drink.html', name=None)


paid = False

@lab7.route('/lab7/api', methods=['POST'])
def api():
    data = request.json
    global paid  # Используем глобальную переменную paid

    if data['method'] == 'get-price':
        return get_price(data['params'])
    
    if data['method'] == 'pay':
        response = pay(data['params'])
        if not response.get("error"):
            paid = True  # Обновляем состояние оплаты после успешной оплаты
        return response
    
    if data['method'] == 'refund':
        if paid:  # Проверяем состояние оплаты
            response = refund(data['params'])
            paid = False  # Обновляем состояние оплаты после успешного возврата
            return response
        else:
            return {"result": None, "error": "Оплата еще не выполнена"}
    
    abort(400)

def get_price(params):
    return {'result': calculate_price(params), "error": None}

def calculate_price(params):
    drink = params.get('drink')
    milk = params.get('milk')
    sugar = params.get('sugar')

    # Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара - на 10.
    if milk:
        price += 30
    if sugar:
        price += 10

    return price

def pay(params):
    card_num = params['card']
    if len(card_num) != 16 or not str(card_num).isdigit():
        return {"result": None, "error": "Неверный номер карты"} 

    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV/CVC"}
    
    price = params['price']  # Используем переданную цену

    return {"result": f'С карты {card_num} списано {price} руб', "error": None}

def refund(params):
    card_num = params['card']
    if len(card_num) != 16 or not str(card_num).isdigit():
        return {"result": None, "error": "Неверный номер карты"}

    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV/CVC"}

    return {"result": f'Деньги возвращены на карту {card_num}', "error": None}


