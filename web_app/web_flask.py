#!/usr/bin/python3
"""URL web application"""

import uuid
import base62
from urllib.parse import urlparse
from datetime import datetime
from flask import Flask, request, redirect, render_template, abort, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='static')
CORS(app, resources="/*", origins="0.0.0.0")

# db connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://flask:f1ask@mysql/url_db'
db = SQLAlchemy(app)

# creates table in Mysql as `url` for the `url_db` database
class Url(db.Model):
    """ creates table `url` """
    short = db.Column(db.String(60), primary_key=True)
    original = db.Column(db.String(256), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, original):
        """ initilizes new rows with respective values """
        self.short = base62.encode(int(uuid.uuid4()))
        self.original = original

db.create_all()
#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404

@app.route('/', strict_slashes=False, methods=['GET', 'POST'])
def add_url():
    """ validates url and returns shortend url """
    if request.method == 'POST':
        originalUrl = request.form.get('ogUrl')
        # validates original urls prefix for proper redireciton
        if urlparse(originalUrl).scheme == '':
            originalUrl = 'http://' + originalUrl

        check = Url.query.filter_by(original=originalUrl).first()
        if check is not None: # prevents duplicate url entries
            url = check.short
            return render_template('index.html', shortUrl=url), 200

        # create new row in db with users url
        newurl = Url(originalUrl)
        shortUrl = newurl.short
        db.session.add(newurl)
        db.session.commit()

        return render_template('index.html', shortUrl=shortUrl), 201  # POST
    return render_template('index.html'), 200  # GET

@app.route('/<url>', strict_slashes=False)
def uri_handle(url):
    """redirects orginal webpage based on short url"""
    originalUrl = Url.query.filter_by(short=url).first()
    if originalUrl is None:  # if short url doesnt exist
        abort(404)
    return redirect(originalUrl.original)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
