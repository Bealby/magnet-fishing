import os
if os.path.exists("env.py"):
    import env
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'magnet_fishing'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_catches')
def get_catches():
    return render_template("catch_log.html", catch_log=mongo.db.catch_log.find())

@app.route('/add_catches')
def add_catches():
    return render_template('/add_catches.html', area=mongo.db.area.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)