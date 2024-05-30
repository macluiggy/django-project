# INSTRUCTIONS

## 1. Clone the repository

## 2. go to backend folder and run the following commands
```bash
pip install django djangorestframework
```

## 3. make migrations
```bash
python manage.py makemigrations
```

## 4. migrate
```bash
python manage.py migrate
```

## 5. run the server
```bash
python manage.py runserver
```


The first thing you should do is create a role, a country and an area



Go to [http://localhost:8000/country/create](http://localhost:8000/country/create)
use a request body like this:
```json
{
    "name": "Colombia"
}
```
Go to [http://localhost:8000/role/create](http://localhost:8000/role/create)
use a request body like this:
```json
{
    "name": "Admin",
    "country_id": 1 // the id of the country you created
}
```

Go to [http://localhost:8000/area/create](http://localhost:8000/area/create)
use a request body like this:
```json
{
    "name": "Antioquia",
    "country": 1 // the id of the country you created
}
```


Then create an user and login
Go to [http://localhost:8000/auth/register](http://localhost:8000/auth/register)
use a request body like this:
```json
{
    "username": "admin",
    "password": "admin",
    "email": "admin@mail.com",
    "area": 1, // the id of the area you created
    "role": 1, // the id of the role you created
}

```

Go to [http://localhost:8000/auth/login](http://localhost:8000/auth/login)
use a request body like this:
```json
{
    "username": "admin",
    "password": "admin"
}
```

Then you can use the token to make requests to the other endpoints

In headers set the `Authorization` with the value `Token <token> `where token is the token you get when you login


You can check the authorization to check if the user with the role can access the endpoint
First create a post
Go to [http://localhost:8000/post/create](http://localhost:8000/post/create)
Don't forget to set the `Authorization` header
use a request body like this:
```json
{
    "title": "Post 1",
    "content": "Content of post 1"
}
```

Then you can check the authorization to check if the user with the role can access the endpoint
Go to [http://localhost:8000/comments/add/1](http://localhost:8000/comments/add/1)
user the id of the post you created
use a request body like this:
```json
{
    "content": "Comment 1"
}
```

Then you can check the authorization to check if the user with the role can access the endpoint
since you just created, it should not let you comment the post

to change that you should create a permission and a role permission for that permission and role
Go to [http://localhost:8000/permission/create](http://localhost:8000/permission/create)
use a request body like this:
```json
{
    "name": "posts.comment"
}
```

Go to [http://localhost:8000/permissions/role_permission/create](http://localhost:8000/permissions/role_permission/create)
use a request body like this:
```json
{
    "role": 1, // the id of the role you created
    "permission": 1, // the id of the permission you created
    "allowed": true
}
```

Then you can check the authorization to check if the user with the role can access the endpoint
Go to [http://localhost:8000/comments/add/1](http://localhost:8000/comments/add/1)
user the id of the post you created
use a request body like this:
```json
{
    "content": "Comment 1"
}
```

Then you can check the authorization to check if the user with the role can access the endpoint
since you now add a permission to the role, it should let you comment the post