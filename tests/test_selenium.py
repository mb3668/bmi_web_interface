from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture
def browser():
	path = "driver/chromedriver"
	selenium_service = Service(path)
	driver = webdriver.Chrome(service=selenium_service)
	yield driver
	driver.quit()

def test_bmi_input(browser):
	# Launch app
	browser.get("http://localhost:5000")

	# Get height and weight features
	feet_input = browser.find_element("id", "height_feet")
	inches_input = browser.find_element("id", "height_inches")
	weight_input = browser.find_element("id", "weight")

	# Tested inputs
	feet = "5"
	inches = "7"
	weight = "140"

	# Pass input
	feet_input.send_keys(feet)
	inches_input.send_keys(inches)
	weight_input.send_keys(weight)

	# Submit inputs
	submit_button = browser.find_element("id", "submit")
	submit_button.click()

	browser.get(f'http://127.0.0.1:5000/bmi_submission?height_feet={feet}&height_inches={inches}&weight={weight}')

	# Test output
	bmi = "21.92"
	category = "Normal"

	# Extract result after click
	result_element = browser.find_element("id", "result")
	result_text = result_element.text
	print(result_text)

	# Run actual tests
	assert browser.current_url == "http://127.0.0.1:5000/bmi_submission?height_feet=5&height_inches=7&weight=140"
	assert result_text == f'Your BMI is {bmi}, your BMI category {category}.'
