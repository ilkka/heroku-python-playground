import os
import sys
import urlparse
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash

import playground.settings

app = Flask(__name__)

@app.route("/")
def hello():
    return "DATABASES contains {}".format(playground.settings.DATABASES)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

