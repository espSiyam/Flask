from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '0659b56c3a4fb43903d3a5035f55b7e2'

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
def hello_world():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
	app.run(debug=True)