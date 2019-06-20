from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/chats/', methods=['POST'])
def create():
    mongo.db.chats.insert({"user_id": request.form['user_id']})
    return '', 200

@app.route('/chats/<string:id>', methods=['GET'])
def get_all(id):
    chats = mongo.db.chats.find({}, {"_id": 0})
    result = []
    for chat in chats:
        result.append(chat)

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
