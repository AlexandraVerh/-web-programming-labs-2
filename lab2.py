from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/example')
def example():
    name = 'Верхозина Александра'
    num = '2'
    grup = 'ФБИ-14'
    kurs = '3 курс'
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши',  'price': 120},
        {'name': 'апельсины', 'price': 80}, 
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]
    books = [
        {'author': 'Ли Бардуго', 'nazv': 'Продажное королевство', 'zanr': 'Фентези', 'str': '672страниц'},
        {'author': 'Марисса Мейер', 'nazv': 'Проклятие', 'zanr': 'Фентези', 'str': '640 страницы'},
        {'author': 'Ли Мие', 'nazv': '"Магазин снов" мистера Талергута. Дневники грез', 'zanr': 'Фентези', 'str': '288 страницы'},
        {'author': 'Ребекка Куанг', 'nazv': 'Вавилон. Сокрытая история', 'zanr': 'Фентези', 'str': '640 страниц'},
        {'author': 'Антонина Крейн', 'nazv': 'Шолох. Долина колокольчиков', 'zanr': 'Фентези', 'str': '572 страниц'},
        {'author': 'Майк Омер',  'nazv': 'Пламя одержимости', 'zanr': 'ДЕТЕКТИВНЫЙ РОМАН. ТРИЛЛЕР', 'str': '448 страниц'},
        {'author': 'Майк Омер', 'nazv': 'Тринадцатая карта', 'zanr': 'ДЕТЕКТИВНЫЙ РОМАН. ТРИЛЛЕР', 'str': '192 страниц'},
        {'author': 'Дженнифер Линн Барнс', 'nazv': 'Последний гамбит', 'zanr': 'ДЕТЕКТИВНЫЙ РОМАН. ТРИЛЛЕР', 'str': '416 страницы'},
        {'author': 'Лэй Ми', 'nazv': 'Ящик Скиннера', 'zanr': 'ДЕТЕКТИВНЫЙ РОМАН. ТРИЛЛЕР', 'str': '156 страниц'},
        {'author': 'Агата Кристи', 'nazv': 'Десять негритят', 'zanr': 'ДЕТЕКТИВНЫЙ РОМАН. ТРИЛЛЕР', 'str': '288 страниц'}
        ]
    return  render_template('example.html', name=name,num=num,grup=grup,kurs=kurs,
                             fruits=fruits, books=books)

@lab2.route("/lab2/")
def lab():
    return render_template('lab2.html')

@lab2.route("/lab2/mult")
def mult():
    return render_template('mult.html')