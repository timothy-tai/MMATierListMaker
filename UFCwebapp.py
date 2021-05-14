from flask import Flask, render_template, redirect, url_for, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')
mongo = PyMongo()
app = Flask(__name__)
app.config["MONGO_URI"] = config.get('dbAccess', 'fighterdb')
mongo.init_app(app)

@app.route("/")
def home():
    fighter_collection = mongo.db.temp_app
    rank = 1
    for fighter in fighter_collection.find():
        fighter_collection.update_one({ '_id': fighter['_id']}, { '$set' : {'rank' : rank}})
        rank += 1
    fighter_list = fighter_collection.find()
    return render_template('index.html', fighter_list=fighter_list)

@app.route("/add_fighter", methods=["POST"])
def add_fighter():
    fighter_collection = mongo.db.temp_app
    fighter = request.form.get('fighter')
    client = MongoClient(config.get('dbAccess', 'fighterdb'))
    db = client.get_database('ufc_db')
    result = db.fighter_records.aggregate([
        {
            '$search': {
                'text': {
                    'query': fighter, 
                    'path': 'name'
                }, 
                'highlight': {
                    'path': 'name'
                }
            }
        }, {
            '$limit': 1
        }
    ])
    fighterToInsert = list(result)[0]
    fighterToInsert['rank'] = 0
    fighter_collection.insert_one(fighterToInsert)
    return redirect(url_for('home'))

@app.route("/remove_fighter/<name>")
def remove_fighter(name):
    fighter_collection = mongo.db.temp_app
    fighter_collection.delete_one({'name': name})
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()
