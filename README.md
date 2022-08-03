Flask Doctor Rest API
=============

This repository contains the example code doctor hospital management API

## About The Project
The project contain CURD rest api for Doctor List along with authentication and access control management for each api resource.
The project is build with flask because of the reasons:

Features:
* Light-weight framework with minimalistic features. 
* Gives developer flexibility on decisions to build the application. 
* SQLAlchemy is a strong and hand on ORM framework. 
* Provides flexibility to expand the application quickly. suitable to microservice architecture
Drawback: 
* Some libs can have dependency conflict issue 
* Cost time and knowledge to init the project at the beginning

Component and tools: 
* click for handle command line interface 
* Flask-SQLAlchemy for handle sqlachemy injection into global application context 
* Flask-Bcrypt - Flask extension that provides bcrypt hashing utilities 
* Flask-Caching - caching data reduce loading to database
* flask-restx - handler resource and swagger documentation 
* PyJWT - handler for jwt authentication
* flask-marshmallow - data payload validation and serialization 
* pytest - intergration and unit testing

### Model structure

![Alt text](images/database.png "Title")

- Main model is doctor model, each doctor with work on once fix location (many to one) and hold many category (many to many)
- Additional table to store multiple language, each location, category and doctor description could have multiple language support, each entity have fix code and we have description text with change base on selected language
- Additional user table for auth and role management.

### Setup
1. Clone this repository.
2. Create a virtualenv and activate.
3. Install requirement packages. 
4. Set `.env` file with related environment variable.
5. Start database service in case you dont have available db connection
    ```sh
   docker-compose up
   ```
6. Init database schema
   ```sh
   flask migrate
   ```
7. seed database schema
   ```sh
   flask seed
   ```
8. Drop database schema (optional)
   ```sh
   flask drop-all
   ```
9. Start the Flask application on your original terminal window: `flask run`.
10. Go to `http://localhost:5000/api/v1/documentaion` to see API resource

```
> You can run the tests with `pytest` or `flask test` command.
```

### Setup with docker
- docker build 
```bash
docker image build -t flask_docker_hospital_api .
```
- docker run 
```bash
docker run -p 5000:5000 -d flask_docker_hospital_api
```

Some example usage for doctor API
----------------------------------

##### Login to get access token

```bash
curl -X 'POST' \
  'http://127.0.0.1:5000/api/v1/users/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "dung.do@gmail.com",
  "password": "password123"
}'
```

##### Creating a Doctor entity 

```bash
curl -X POST \
  http://localhost:5000/api/doctors/ \
  -H 'Content-Type: application/json' \
  -H 'Authorizatione: ' \
  -d '{
        "name": "John Witch",
        "description": {
            "en": "By filling out the needed information on the website, you can now make a fake medical prescription.",
            "fr": "En remplissant les informations nécessaires sur le site Web, vous pouvez désormais faire une fausse ordonnance médicale."
        },
        "location": "en",
        "price": 3000,
        "spec_list": [
            "anesthesiology",
            "dermatology"
        ]
    }'
```

##### Get list of doctor with authentication header

```bash
curl -X 'GET' \
  'http://127.0.0.1:5000/api/v1/doctors?lang_code=en' \
  -H 'accept: application/json' \
  -H 'Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTk2Mjc0NDQsImlhdCI6MTY1OTU0MTA0NCwidXNlciI6eyJ1cGRhdGVkX2F0IjpudWxsLCJpZCI6MSwiY3JlYXRlZF9hdCI6IjIwMjItMDgtMDJUMTU6Mjk6MTYuMjMyMDI4IiwidXNlcm5hbWUiOiJhZG1pbiIsImlzX2FkbWluIjp0cnVlLCJlbWFpbCI6ImR1bmcuZG9AZ21haWwuY29tIn19.XGF0rKQCuCkx2fuKUQpcfKUgyhEQRAtb8i9SidNS8mA'
```

Discussion
----------------------------------

##### Open point for improvement

- Implement more complex caching query for fetch doctor list, currently we catch base on filter query params with exp time, a standalone service should be design to handle create/update doctor data so data can be sync between cache and database. 
- Making more robust language table design, currently each entity have each language table, I try to have generic table and a link table between but the solution not working correctly.
- Batch create/update doctor api 
- isolate some of block code in view resource into seperated service.
- investigate in test case exception code not work correctly, suspect due to conflict betwee flast-restx and flask test client 
- ....
##### Production consideration 
- split up the application into smaller microservice ex, lanaguage support service, caching service trigger when create/update doctor data -> improve ability to scale up and responsibility seperation
- seup CI-CD for deployment. 
- store secret variable into third party app hosting.