from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup')
def signup_form():
	return render_template('signup.html')

@app.route('/thanks')
def thanks():
	first = request.args.get('first')
	last = request.args.get('last')

	return render_template('thanks.html', first=first, last=last)

@app.errorhandler(404)
def not_found(any_error):
 	return render_template('404.html')

if __name__ == "__main__":
	app.run(debug=True)