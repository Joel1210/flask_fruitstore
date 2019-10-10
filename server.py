from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_form = request.form['strawberry']
    raspberry_form = request.form['raspberry']
    apple_form = request.form['apple']
    blackberry_form = request.form['blackberry']
    firstname = request.form['first_name']
    lastname = request.form['last_name']
    studentid = request.form['student_id']
    int_strawberry = int(strawberry_form)
    int_raspberry = int(raspberry_form)
    int_apple = int(apple_form)
    int_blackberry = int(blackberry_form)
    count = int_strawberry + int_raspberry + int_apple + int_blackberry
    print(f"Charging {firstname} {lastname} for {count} fruits")

    return render_template("checkout.html", strawberry_order=strawberry_form, raspberry_order=raspberry_form, apple_order=apple_form, blackberry_order=blackberry_form, firstnamech= firstname, lastnamech= lastname, studentidch= studentid, count_order=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    