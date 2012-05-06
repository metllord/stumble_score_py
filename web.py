from flask import Flask, request, render_template
from location.scoring import StumbleScore

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        return render_template('base.html')
    else:
        location = StumbleScore(request.form['address'])
        return render_template('results.html', **location())

if __name__ == "__main__":
	app.run(debug=True)
