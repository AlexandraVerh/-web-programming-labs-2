from flask import Blueprint, render_template, request, abort

lab8 = Blueprint('lab8',__name__)


@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses = [
    {"name": "c++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "c#", "videos": 8} #если цена не указана, то курс бесплатный
]

#Здесь мы определяем, что у нас будет специальный путь, по которому будет
#"жить" API
#здесь список курсов
@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return courses

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        abort(404)  # возвращаем ошибку 404, если номер выходит за пределы
    return courses[course_num]

#удаление курса
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num < 0 or course_num >= len(courses):
        abort(404)  
    del courses[course_num]
    return '', 204

#изменение существующего курса
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    course = request.get_json()
    if course_num < 0 or course_num >= len(courses):
        abort(404) 
    courses[course_num] = course
    return courses[course_num]

#добавление нового курса
@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    courses.append(course)
    return {"num": len(courses)-1} #возвращение номера нового курса

