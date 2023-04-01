from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def categorize_bmi(bmi):
	"""
	Categorize the user BMI into one of four categories

	:param bmi:
	users body mass index

	:return:
	string, BMI category
	"""
	if 18.5 <= bmi < 25:
		result = "Normal"
	elif 25 <= bmi < 30:
		result = "Overweight"
	elif bmi >= 30:
		result = "Obese"
	else:
		result = "Underweight"

	return result

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		height_feet = request.form['height_feet']
		height_inches = request.form['height_inches']
		weight = request.form['weight']
		return redirect(url_for('bmi_submission', height_feet=height_feet, height_inches=height_inches, weight=weight))
	return render_template("form.html")

@app.route('/bmi_submission')
def bmi_submission():
	height_feet = request.args.get('height_feet')
	height_inches = request.args.get('height_inches')
	weight = request.args.get('weight')

	# Calculate total height
	total_height = int(height_feet)*12 + int(height_inches)

	# Calcualte bmi
	print(int(weight))
	print(int(total_height))
	bmi = (int(weight) / total_height**2) * 703

	return render_template('index.html', bmi=round(bmi, 2), bmi_category=categorize_bmi(bmi))
