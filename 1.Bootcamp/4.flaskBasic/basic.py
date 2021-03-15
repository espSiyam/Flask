from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

	name = "Siyam"
	letters = list(name)
	pupp = {'pup_name':'doggo'}
	return render_template('basic.html', var1 = name, var2 = letters, var3 = pupp)

if __name__ == "__main__":
	app.run(debug=True)