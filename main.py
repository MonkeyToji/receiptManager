from flask import Flask, request, jsonify
import json
from receiptToPoints import receiptConverter

app = Flask(__name__)

receipt_list = {}

@app.route("/receipts/process", methods=["POST", "GET"])
def main():
    if request.method == "GET":
        return jsonify(receipt_list)
    if request.method == "POST":
        receipt = request.json
        output = receiptConverter(receipt)
        newReceipt = {"receipt": receipt, "points":output["points"]}
        if(receipt_list.get(output["id"])):
            return {'Error': 'This receipt already exist'}
        else:
            receipt_list[output["id"]] = newReceipt
            return jsonify({'id': output["id"]})

@app.route("/receipts/<id>/points", methods=["GET"])
def pointValue(id):
    if receipt_list.get(id):
        targetReceipt = receipt_list[id]
        return {'points': targetReceipt['points']}
    return {'Error' : 'No Value At This Id Number!'}

if __name__ == "__main__":
    app.run()
