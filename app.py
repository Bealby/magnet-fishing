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

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/areas')
def areas():
    return render_template("areas.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/')
@app.route('/get_catches')
def get_catches():
    return render_template("catch_log.html", catch_log=mongo.db.catch_log.find())

@app.route('/add_catches')
def add_catches():
    return render_template('/add_catches.html', area=mongo.db.area.find(), magnet=mongo.db.magnet.find())

@app.route('/insert_catches', methods=['POST'])
def insert_catches():
    catch_log = mongo.db.catch_log
    catch_log.insert_one(request.form.to_dict())
    return redirect(url_for('get_catches'))

@app.route('/edit_catch_log/<catch_log_id>')
def edit_catch_log(catch_log_id):
    the_catch_log =  mongo.db.catch_log.find_one({"_id": ObjectId(catch_log_id)})
    all_area =  mongo.db.area.find()
    all_magnet = mongo.db.magnet.find()
    return render_template('edit_catch_log.html', catch_log=the_catch_log, area=all_area, magnet=all_magnet)

@app.route('/update_catch_log/<catch_log_id>', methods=["POST"])
def update_catch_log(catch_log_id):
    catch_log = mongo.db.catch_log
    catch_log.update( {'_id': ObjectId(catch_log_id)},
    {
        'name':request.form.get('name'),
        'email':request.form.get('email'),
        'magnet': request.form.get('magnet'),
        'area_name': request.form.get('area_name'),
        'location_name':request.form.get('location_name'),
        'catches':request.form.get('catches'),
        'catch_date':request.form.get('catch_date')
    })
    return redirect(url_for('get_catches'))

@app.route('/delete_catch_log/<catch_log_id>')
def delete_catch_log(catch_log_id):
    mongo.db.catch_log.remove({'_id': ObjectId(catch_log_id)})
    return redirect(url_for('get_catches'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)