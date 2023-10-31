from flask import Blueprint, render_template, redirect, request
lab4 = Blueprint('lab4',__name__)

@lab4.route("/lab4/")
def lab():
    return render_template('lab4.html')

@lab4.route("/lab4/login", methods = ['GET','POST'])
def login():
    
    if request.method == 'GET':
        return render_template('login.html')
    
    username = request.form.get('username')
    password = request.form.get('password')   

    
    if username == '':
        error = 'Не введён логин '
        return render_template('login.html', error=error, username=username, password=password)
        
    if  password == '':
        error  = 'Не введён пароль '
        return render_template('login.html', error=error, username=username, password=password)

    if username == 'alex' and password == '123':
        return render_template('success.html',  username=username, password=password)
    else:
        error  = 'Неверный логин и/или пароль '
        return render_template('login.html', error=error, username=username, password=password)
    


@lab4.route('/lab4/holodil', methods=['GET', 'POST'])
def holodil():
    if request.method == 'GET':
        return render_template('holodil.html')
    
    temperature = request.form.get('temperature')
    error = ''
    message = ''  # Начальное значение для переменной message
    snowflakes = ''  # Начальное значение для переменной snowflakes
    
    if temperature is None or temperature == '':
        error = 'ошибка: не задана температура'
        return render_template('holodil.html', error=error, temperature=temperature)
    
    if int(temperature) < -12:
        error = 'не удалось установить температуру — слишком низкое значение'
        return render_template('holodil.html', error=error, temperature=temperature)
    
    if int(temperature) > -1:
        error = 'не удалось установить температуру — слишком высокое значение'
        return render_template('holodil.html', error=error, temperature=temperature)
    
    if -12 <= int(temperature) <= -9:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️❄️'
        return render_template('holodil.html', error=error, temperature=temperature, message=message, snowflakes=snowflakes)

    if -8 <= int(temperature) <= -5:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️❄️'
        return render_template('holodil.html', error=error, temperature=temperature, message=message, snowflakes=snowflakes)

    if -4 <= int(temperature) <= -1:
        message = f'Установлена температура: {temperature}°C'
        snowflakes = '❄️'
        return render_template('holodil.html', error=error, temperature=temperature, message=message, snowflakes=snowflakes)

    
@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno(): 
    if request.method == 'GET': 
        return render_template('zerno.html') 

    error = {}
    zerno = request.form.get('zerno') 
    ves = request.form.get('ves') 
    message = ''

     
    if ves is None or ves == '': 
        error = 'не введен вес' 
    elif float(ves) <= 0:  # float для запятой 
        error = 'неверное значение веса'
    elif zerno: 
        if zerno == 'ячмень': 
            price = 12000 
        elif zerno == 'овес': 
            price = 8500 
        elif zerno == 'пшеница': 
            price = 8700 
        elif zerno == 'рожь': 
            price = 14000 

        total_cost = float(ves) * price 

        if float(ves) > 50: 
            total_cost *= 0.9 
            message = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб. Применена скидка за большой объем.'.format(zerno, ves, total_cost) 
        else: 
            message = 'Заказ успешно сформирован. Вы заказали {}. Вес: {} т. Сумма к оплате: {} руб.'.format(zerno, ves, total_cost) 
        if float(ves) > 500: 
            message = 'Такого объема сейчас нет в наличии.'

    return render_template('zerno.html', error=error, zerno=zerno, ves=ves, message=message)

@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies(): 
    if request.method == 'GET': 
        return render_template('cookies.html') 
    
    color = request.form.get('color')
    headers = {
        'Set-Cookie': 'color=' + color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '',303,headers