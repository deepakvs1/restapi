  Django REST API Project
--------------------------
This project is a Django-based RESTful API that provides endpoints for interacting with a specific data and saved to mongodb cloud server


1. create a repository
2. Open terminal where type command - python -m venv djenv
3. to activate env - djenv\Scripts\activate
4. Package you need to install
       - pip install -r requirement.txt
5. create a project - django admin startproject restapi
6. change directory - cd restapi
7. create an app - python manage.py startapp employee
8. add "employee" and "rest_framewok" in installed app- employee/setting.py  
9. project run command - python manage.py runserver

API Endpoints
---------------
    Registration: /register
        Method: GET
        Description: Renders the registration page.
    Login: /login
        Method: GET
        Description: Renders the login page.
    Employee Detail: /api/employee
        Method: POST
        Description: Adds an employee profile to the MongoDB database.
    Retrieve Employee Profile: /api/employee/{name}
        Method: GET
        Description: Retrieves an employee profile from the MongoDB database based on the provided name.
    Update Employee Profile: /api/employee/{name}
        Method: PUT
        Description: Updates an existing employee profile in the MongoDB database based on the provided name.
    Delete Employee Profile: /api/employee/{name}
        Method: DELETE
        Description: Deletes an employee profile from the MongoDB database based on the provided name.

Database Connection
---------------------
The project utilizes MongoDB Atlas as the database service. Make sure you have set up your MongoDB Atlas cluster and obtained the connection string. Replace the myclient line in views.py with your MongoDB Atlas connection string.

