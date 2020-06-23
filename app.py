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

@app.route('/insert_catches', methods=['POST'])
def insert_catches():
    catch_log = mongo.db.catch_log
    catch_log.insert_one(request.form.to_dict())
    return redirect(url_for('get_catches'))

@app.route('/edit_catch_log/<catch_log_id>')
def edit_catch_log(catch_log_id):
    the_catch_log =  mongo.db.catch_log.find_one({"_id": ObjectId(catch_log_id)})
    all_area =  mongo.db.area.find()
    return render_template('edit_catch_log.html', catch_log=the_catch_log, area=all_area)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)