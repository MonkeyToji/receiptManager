from flask import Flask, render_template, request, redirect, url_for
from practice import wordCheck

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        receipt = request.form['receiptInput']
        output = wordCheck(receipt)
        print(output)
        return redirect(url_for("home"))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()
