from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from receiptToPoints import receiptConverter

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        receipt = request.json
        output = receiptConverter(receipt)
        return jsonify(output)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
