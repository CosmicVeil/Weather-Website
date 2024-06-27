from flask import Flask, render_template, request
import math
from flask import render_template
import requests

# import json to load JSON data to a python dictionary 
import json 

# urllib.request to make a request to api 
import urllib.request 
import urllib.parse


app = Flask(__name__) 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route('/', methods =['POST', 'GET']) 
def weather(): 
	if request.method == 'POST': 
		#city = request.form['city'] 
		city = urllib.parse.quote_plus(request.form['city'])
	else: 
		# for default name toronto 
		city = 'toronto'

	# your API key will come here 
	api = '24f574679f980320483598a0a357b70c'

	# source contain json data from api 
	#source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api + "&units=metric").read() 
	source = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}" + "&units=metric")

	
	# converting JSON data to a dictionary 
	list_of_data = source.json()
	

	
	# data for variable list_of_data
	try: 
		data = {
			"cityname": city.replace('+',' ').title(),
			"country_code": str(list_of_data['sys']['country']), 
			"coordinate": str(list_of_data['coord']['lon']) + ', '
						+ str(list_of_data['coord']['lat']), 
			"temp": str(list_of_data['main']['temp']) + 'C',
			"feels_like": str(list_of_data['main']['feels_like']) + 'C', 
			"description": "There are currently " + str(list_of_data['weather'][0]['description']).lower(),
			"pressure": str(list_of_data['main']['pressure']), 
			"humidity": str(list_of_data['main']['humidity']), 

		} 
		return render_template('index.html', data = data) 
	except:
		pass




if __name__ == '__main__': 
	app.run(debug = True) 
