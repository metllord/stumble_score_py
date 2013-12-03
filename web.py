import os
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
        distance = request.form['distance']
        if not place:
            flash("You didn't enter an address. Have you been drinking?")
            return redirect(url_for('home'))
        location = StumbleScore(place, distance)
        return render_template('results.html', **location())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
