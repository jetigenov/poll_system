# Poll API System

### Installation
1. clone repository `git@github.com:jetigenov/poll_system.git`
2. create virtualenv with python3.7 `virtualenv venv`
3. install postgres 13 `brew install postgresql@13`
4. install requirements `pip install -r requirements.txt`
5. make migrations
    - `python manage.py makemigrations`
    - `python manage.py migrate`
6. create superuser
    - `python manage.py createsuperuser`
7. runserver
    - `python manage.py runserver`

### Build poll system main image
`docker build -f docker-compose.yml`

##### Add polls (POST)
- Access: `Admin`
- URL: `/api/polls/`
- QUERY PARAMETERS: `name`, `end_date`, `description`
###### Update/Delete polls (PUT, DELETE)
- Access: `Admin`
- URL: `/api/polls/<poll_id>/`

##### Add questions to polls(POST)
- Access: `Admin`
- URL: `/api/polls/<poll_id>/questions/`
- QUERY PARAMETERS: `text`, `type_question`(text_field or radio or check_boxes), `poll`
###### Update/Delete questions (PUT, DELETE)
- Access: `Admin`
- URL: `/api/polls/<poll_id>/questions/<question_id>/`
##### Add/Read choices for question(POST, GET)
- Access: `Admin`
- URL: `/api/polls/<poll_id>/questions/<question_id>/choices/`
- QUERY PARAMETERS: `text`

##### Get list for active polls(GET)
- Access: `AllowAll`
- URL: `/api/active_polls/`

##### Taking a poll (POST)
- Access: `Authorized user`
- URL: `/api/polls/<poll_id>/questions/<question_id>/answers/`

##### Get list for finished users polls (GET)
- Access: `Authorized user`
- URL: `/api/my_polls/`