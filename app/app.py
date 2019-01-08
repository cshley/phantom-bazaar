from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/submit-order", methods=['GET', 'POST'])
def submit_order():
    if request.method == "GET":
        return render_template('submit-order.html')
        

    if request.method == "POST":
        name     = request.form['name']
        quantity = request.form['quantity']
        price    = request.form['price']
        expiry   = request.form['expiry']

        print(name, quantity, price, expiry)

