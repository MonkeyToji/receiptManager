from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from receiptToPoints import receiptConverter
from idToPoints import idConverter

app = Flask(__name__)

@app.route("/receipts/process", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        receipt = request.json
        output = receiptConverter(receipt)
        return jsonify(output)


@app.route("/points", methods=["GET"])
def pointValue():
        idValue = request.json
        output = idConverter(idValue)
        return jsonify(output)

if __name__ == "__main__":
    app.run()
