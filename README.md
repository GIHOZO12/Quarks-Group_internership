# Quarks-


### Tech Stack
Python

Django

Django REST Framework

In-memory data structure (Python dictionary)

#Simple rest Api, using django rest framework.

This project is a technical task for the Quarks Group Backend Internship. It implements a simple RESTful API using Django and Django REST Framework, with **in-memory storage** and two endpoints: one for creating users and another for retrieving them by user_id.

Endpoints:

- `POST  http://127.0.0.1:8000/api/users/` - Create a new user.

#### Request Body (JSON):
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}

### Response for it
{
  "user_id": "2fce7f41-81d9-444c-b61f-c147d1afde51"
}
```

- `GET  http://127.0.0.1:8000/api/users/{user_id}/` - Retrieve a user by user_id.

#### Response for it
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}

**if user_id is not found:

{
  "error": "User not found"
}

How to run my project locally:

- Clone the repository
- Create a virtual environment and activate it
- Install the requirements using pip
- Run server with this command : python manage.py runserver


 Test API (using Postman)
POST: http://127.0.0.1:8000/api/users_view/  
Request Body:
{
    "name": "John Doe",
  "email": "john@example.com"
}

Response:
{
  "user_id": "2fce7f41-81d9-444c-b61f-c147d1afde51"
}




GET: http://127.0.0.1:8000/api/get_user/<user_id>/
request body:
{
    "user_id": "2fce7f41-81d9-444c-b61f-c147d1afde51"
}

Response:
{
  "name": "John Doe",
  "email": "john@example.com"
}
