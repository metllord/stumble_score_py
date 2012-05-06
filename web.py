from flask import Flask, request, render_template, flash, redirect, url_for
from location.scoring import StumbleScore

app = Flask(__name__)
SECRET_KEY = 'fdsajjksdkljei3902jfdjfi02e0dnmk'
app.config.from_object(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('base.html')
    else:
        place = request.form['address']
        if not place:
            flash("You didn't enter an address. Have you been drinking?")
            return redirect(url_for('home'))
        location = StumbleScore(place)
        return render_template('results.html', **location())

if __name__ == "__main__":
	app.run(debug=True)
