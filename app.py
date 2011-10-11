import os
import sys
import urlparse
import psycopg2
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

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

@app.route("/")
def hello():
    return "DATABASE_URL is {}".format(app.config['DATABASE_URL'])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

