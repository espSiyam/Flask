from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

	name = "Siyam"
	return render_template('basic.html', var = name)

if __name__ == "__main__":
	app.run(debug=True)