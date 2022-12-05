from flask import Flask, request, jsonify
import json
from receiptToPoints import receiptConverter
from idToPoints import idConverter

app = Flask(__name__)
tmpCache = {}

@app.route("/receipts/process", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        receipt = request.json
        output = receiptConverter(receipt)
        return jsonify(output)

@app.route("/receipts/<id>/points", methods=["GET"])
def pointValue(id):
        output = idConverter(id)
        return jsonify(output)


if __name__ == "__main__":
    app.run()
