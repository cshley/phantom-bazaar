from flask import Flask, render_template, request
app = Flask(__name__)


# This tells our webserver what to do when it gets a request to /submit-order
# i.e in a web browser if someone goes to phantom-bazaar.co.uk/submit-order 
# then we should run this piece of code

@app.route(
  # This string tells us what route we should watch for, 
  # in this particular case we are watching for a request
  # to /submit-order
  "/submit-order", 

  # This array tells us what methods we should respond too
  # in this particular case its GET and POST, but there are many others.

  # GET is the standard type of request your browser will make when you 
  # visit a webpage.

  # POST is a special type of request, indicating that we'd like to send
  # a special payload to the webserver, in our case this will be the HTML
  # form elements we've previously described in submit-order.html
  methods=['GET', 'POST'])
def submit_order():

    # This block of code will only run if the method is GET
    # i.e this is what we'll show when a user comes to submit-order page
    # for the first time.
    if request.method == "GET":
        # This is saying that we should just send back the submit-order.html
        # page without any fancy gubbins.
        return render_template('submit-order.html')
        

    # This block of code will only run if the method is POST
    # i.e this is what we'll do when someone hits submit on the page.
    if request.method == "POST":
        name     = request.form['name']
        quantity = request.form['quantity']
        price    = request.form['price']
        expiry   = request.form['expiry']

        # For now, we'll say that a failed order is one that has a 
        # name of "wood", because wood is already a commodity that exists
        # and this is a market for things that dont yet exist.
        if name == "wood":
            # We've failed to submit this order for whatever reason
            # lets send the submitted-failure page back to the user
            return render_template('submitted-failure.html')

        # Otherwise, we've successfully submitted the order; Huzzah.
        return render_template('submitted-success.html')
