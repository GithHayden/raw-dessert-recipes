import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://admin:animals1234@ds233541.mlab.com:33541/raw_cookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)