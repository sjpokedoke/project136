from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")

def allstar():
    return jsonify({
        "data": data,
        "message": "Success!"
    }), 200

@app.route("/stars")

def starsdata():
    name = request.args.get("Star_name")
    stars_data = next(item for item in data if item["Star_name"] == name)
    return jsonify({
        "data": stars_data,
        "message": "Success!"
    }), 200

if __name__ == "__main__":
    app.run()