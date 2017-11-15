import os
from flask import Flask, jsonify, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGODB_HOST'] = "172.18.0.3"
app.config['MONGODB_PORT'] = 27017

from models import mongo_engine
mongo_engine.init_app(app)

from models import Representatives, Credentials

@app.route('/representatives', methods=['GET'])
def representatives():
	json_reps = []

	for rep in Representatives.objects:
		json_reps.append({'name' : rep.name, 'company' : rep.company})
	
	return jsonify({'result' : json_reps})

@app.route('/test', methods=['GET'])
def andersch():
	input_name = 'Andersch Von Monegrabben'
	company = 'EA'

	query = Representatives.objects.get(company = company)

	if query:
		out = {'name' : query['name'], 'company' : query['company']}
	else:
		representative = Representatives(name = query.name, company = query.company)
		representative.save()

		out = name + " added"
	
	return jsonify({'result' : out})

@app.route('/representatives/<input_name>', methods=['GET'])
def getRepresentativeByName(input_name):
	#query = Representatives.objects(name = input_name)			returns 'QuerySet' of duplicates
	#query = Representatives.objects.get(name = input_name)		raises DoesNotExist if no document matches the query
	#query = Representatives.objects(name = input_name)[0] 		find one(first) among duplicates

	query = Representatives.objects(name = input_name)[0]

	if query:
		out = {'name' : query.name, 'company' : query.company}
	else:
		out = 'No results found'

	return jsonify({'result' : out})

#testest
@app.route('/register', methods=['POST'])
def addCredentials():
	json_data = request.json
	query = Representatives.objects(email = json_data['email'])

	if query:
		status = 'this user is already registered'
	else:
		representative = Representatives(name = json_data['name'], company = json_data['company'], credentials = Credentials(email = json_data['email'], password = json_data['password']))
		representative.save()

	return jsonify({'result': status})

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)
