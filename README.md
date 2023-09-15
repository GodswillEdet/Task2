# REST API for User Management

This is a simple REST API for managing Users. It allows you to perform CRUD (Create, Read, Update, Delete) operations on a user data.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.7+)
- Django
- Django Rest Framework

You can install Django and Django Rest Framework using pip:

```sh
pip install django djangorestframework
```

## Installation

1. Clone this repository:
```sh
git clone https://github.com/GodswillEdet/Task2.git
cd Task2
```
2. Install the required dependencies:
```sh
pip install -r requirements.txt
```
3. Run database migrations:
```sh
python manage.py migrate
```

## Usage
To run the API, use the following command:
```sh
python manage.py runserver
```

## API Endpoints

Create a User: POST /api/

List Users: GET /api/

Retrieve a User: GET /api/{user_id}/

Update a User: PUT /api/{User_id}/ or PATCH /api/{User_id}/

Delete a User: DELETE /api/{user_id}/




## Examples


Here are some examples of how to use the API:

- Create a User:
```sh
curl -X POST -H "Content-Type: application/json" -d '{"name": "John"}' http://127.0.0.1:8000/api/
```

- Fetch details of a user:
```sh
curl http://127.0.0.1:8000/api/{user_id}/
```

- Modify details of an existing user:
```sh
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Updated"}' http://127.0.0.1:8000/api/{user_id}/
```

- Remove a person:
```sh
curl -X DELETE http://127.0.0.1:8000/api/{user_id}/
```

- List all persons:
```sh
curl http://127.0.0.1:8000/api/
```
