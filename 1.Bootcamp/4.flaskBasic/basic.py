from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('basic.html')

@app.route('/info')
def info():
	return '<h1>Puppes are cute!</h1>'

@app.route('/puppy/<name>')
def puppy(name):
	return '<h1>100th letter: {}</h1>'.format(name[100])

if __name__ == "__main__":
	app.run(debug=True)