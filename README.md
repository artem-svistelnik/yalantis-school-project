# yalantis-python-school

**Deployment and launch instructions**

In an empty directory, execute the command::

`git clone https://github.com/artem-svistelnik/yalantis-python-school.git`

Create virtual environment (venv) and run it

`python3 -m venv venv`

`source venv/bin/activate`

Go to the directory with the project

`cd yalantis-python-school`

Install all required dependencies

`pip install -r requirements.txt `

Create migration

`python manage.py makemigrations course_api`

Apply migration

`python manage.py migrate`

Create superuser

`python manage.py createsuperuser`

run server

`python manage.py runserver `
_You can add a port number at the end of the line. For example: "5000"_


**Next, you need to fill the base with several entries in the "courses" table**

**Description of requests :**

1. _Adding a course to the catalog_:
 post requests on http://localhost:5000/api/courses/ with data in json format
`{
    "course_title": "new",
    "start_date": "2021-05-04",
    "finish_date": "2021-05-21",
    "lectures_count": 15
}`

2. _The list of courses_:
get requests on http://localhost:5000/api/courses/

3. _Course details by id (detailed course page display full course information)_:
get requests on http://localhost:5000/api/courses/id/

4. _Search for a course by name and filter by date_:

    4.1 Filter by date`?start_date=04.05.2021&finish_date=21.05.2021` 
         get requests on: http://localhost:5000/api/courses/?start_date=04.05.2021&finish_date=21.05.2021

    4.2 Search  `?search=something`
        get requests on : http://localhost:5000/api/courses/?search=something

5. _Changing course attributes_:
put requests on : http://localhost:5000/api/courses/id/ with data in json format
`{
    "course_title": "changed title",
    "start_date": "2021-05-04",
    "finish_date": "2021-05-21",
    "lectures_count": 15
}`

6. _Deleting a course_:

delete requests on http://localhost:5000/api/courses/id/


# Tests

**Run tests:**

`python manage.py test`

