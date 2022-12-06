from flask import Flask, request, jsonify
import json
from receiptToPoints import receiptConverter
from idToPoints import idConverter

app = Flask(__name__)

receipt_list = []

@app.route("/receipts/process", methods=["POST", "GET"])
def main():
    if request.method == "GET":
        return jsonify(receipt_list)
    if request.method == "POST":
        receipt = request.json
        output = receiptConverter(receipt)
        newReceipt = {"id" : output["id"], "receipt": receipt, "points":output["points"]}
        receipt_list.append(newReceipt)
        return jsonify(output)

@app.route("/receipts/<id>/points", methods=["GET"])
def pointValue(id):
        
        return jsonify()


if __name__ == "__main__":
    app.run()
