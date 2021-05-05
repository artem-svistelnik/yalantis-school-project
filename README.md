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

`python manage.py runserver`



