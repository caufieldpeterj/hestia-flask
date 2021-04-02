# hestia-flask

# setting up virtual environment
python3 -m venv venv

# bash code that configures virtual env for us (locally) and manages it
. venv/bin/activate

# postgres is always running in the background of our computer, so flask just sends the requests o psql

# flask-bcrypt
# peewee - ORM, how flask stalks to PostgreSQL
# psycopg2-binary - db engine for psql, how we talk to postgres
# flask_login - 
# flask_cors - 
pip3 install flask-bcrypt peewee flask psycopg2-binary flask_login flask_cors

# pipe it
pip3 freeze > requirements.txt

# create 
touch app.py