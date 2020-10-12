from flask import Flask , render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7bfd83d67ecf6d9fa113ae1018bcdbcd'

posts = [
	{
		'author': 'Sohag Ahammed Siyam',
		'title': 'Blog post 1',
		'content': 'First blog content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Anis ul Haque',
		'title': 'Blog post 2',
		'content': 'Second blog content',
		'date_posted': 'April 21, 2018'		
	}
]

@app.route("/")
@app.route("/home")
def hello():
	return render_template('home.html', posts = posts, title='Home')

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html',title='Register', form = form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html',title='Login', form = form)



if __name__ == '__main__':
	app.run(debug=True)