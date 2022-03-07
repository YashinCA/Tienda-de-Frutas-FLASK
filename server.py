from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    firstname_from_form = request.form['first_name']
    lastname_from_form = request.form['last_name']
    student_id_from_form = request.form['student_id']
    apple_from_form = request.form['apple']
    raspberry_from_form = request.form['raspberry']
    strawberry_from_form = request.form['strawberry']
    fruisttotal_from_form = int(
        apple_from_form)+int(raspberry_from_form)+int(strawberry_from_form)
    print(request.form)
    return render_template("checkout.html", first_name=firstname_from_form, last_name=lastname_from_form, student_id=student_id_from_form, apple=int(apple_from_form), raspberry=int(raspberry_from_form), strawberry=int(strawberry_from_form), total=fruisttotal_from_form)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
