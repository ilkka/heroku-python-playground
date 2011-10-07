import os
import sys
import urlparse
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

app = Flask(__name__)

@app.route("/")
def hello():
    if os.environ.has_key('DATABASE_URL'):
        return "DATABASE_URL is {}".format(urlparse.urlparse(os.environ.get('DATABASE_URL')))
    else:
        return "No DATABASE_URL in environ :("

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

