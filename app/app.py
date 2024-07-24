from flask import Flask, render_template, jsonify
from flask.wrappers import Response

# from init_db import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@db/candles_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/candles")
def get_candles() -> Response:
    candles = Candle.query.all()
    candles_list = [
        {
            "name": c.name,
            "description": c.description,
            "price": c.price,
            "quantity": c.quantity,
        }
        for c in candles
    ]
    return jsonify(candles_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
