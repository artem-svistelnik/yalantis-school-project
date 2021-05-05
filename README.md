# yalantis-python-school

**Инструкция по развертыванию и запуску**

В пустой дериктории выполнить команду:

`git clone https://github.com/artem-svistelnik/yalantis-python-school.git`

Создать виртуальное окружение (venv) и запустить его

Перейти в папку с проектом

`cd yalantis-python-school`

Установить все необходимые зависимости 

`pip install -r requirements.txt `

Создать миграцию

`python manage.py makemigrations course_api`

Применить миграцию

`python manage.py migrate`

Создать суперпользователя

`python manage.py createsuperuser`

Запустить сервер

`python manage.py runserver `
_Можно добавить в конце строки номер порта. Например : "5000"_


**Последующим необходимо заполнить базу несколькими записями в таблице "курсы"**

**Роутинг по пунктам :**

1. _Додавання курсу в каталог_:
 post запрос на http://localhost:5000/api/courses/ c данными в формате json
`{
    "course_title": "new",
    "start_date": "2021-05-04",
    "finish_date": "2021-05-21",
    "lectures_count": 15
}`

2. _Відображення списку курсів_:
get запрос на http://localhost:5000/api/courses/

3. _Відображення деталей курсу по id (детальна сторінка курсу повинна відображати повну інформацію про курс)_:
get запрос на http://localhost:5000/api/courses/id/

4. _Пошук курсу за назвою і фільтр по датах_:

    4.1 Фильтр по датах`?start_date=04.05.2021&finish_date=21.05.2021` 
         get запрос: http://localhost:5000/api/courses/?start_date=04.05.2021&finish_date=21.05.2021

    4.2 Поиск  `?search=something`
        get запрос : http://localhost:5000/api/courses/?search=something

5. _Зміна атрибутів курсу_:
put запрос на : http://localhost:5000/api/courses/id/ c данными в формате json
`{
    "course_title": "changed title",
    "start_date": "2021-05-04",
    "finish_date": "2021-05-21",
    "lectures_count": 15
}`

6. _Видалення курсу_:

delete запрос на http://localhost:5000/api/courses/id/

