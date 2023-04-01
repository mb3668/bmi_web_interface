from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		height = request.form['height']
		weight = request.form['weight']
		return redirect(url_for('result', height=height, weight=weight))
	return render_template("form.html")

@app.route('/result')
def result():
	height = request.args.get('height')
	weight = request.args.get('weight')
	return render_template('index.html', height=height, weight=weight)
