import os
import sys
import urlparse
import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash
from contextlib import closing


if not os.environ.has_key('DATABASE_URL'):
    raise Exception("No DATABASE_URL in environment")


# some configuration
DATABASE_URL = urlparse.urlparse(os.environ['DATABASE_URL'])
DEBUG = True
SECRET_KEY = 'development-secret'
USERNAME = 'admin'
PASSWORD = 'secret'


app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('CONFIG_FILE', silent=True)


def connect_db():
    """Return a database connection object."""
    u = app.config['DATABASE_URL']
    return psycopg2.connect(
            host=u.hostname,
            port=u.port,
            database=u.path[1:],
            user=u.username,
            password=u.password
            )


def init_db():
    """Initialize DB with schema data."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().execute(f.read())
        db.commit()


@app.route("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

