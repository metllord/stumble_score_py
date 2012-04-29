from flask import Flask
app = Flask(__name_)

@app.route("/")
def home():
	return "Welcome to StumbleScore"

if __name__ == "__main__":
	app.run()
