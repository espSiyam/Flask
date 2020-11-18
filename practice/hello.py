from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '0659b56c3a4fb43903d3a5035f55b7e2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


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

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data ==  'password':
			flash('Loggned in successfully','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful', 'danger')
	return render_template('login.html', title='Login',form=form)


if __name__ == '__main__':
	app.run(debug=True)