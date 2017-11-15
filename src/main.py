import os
from flask import Flask, jsonify, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb:27017')
db = client.tododb

representatives = db.representatives


@app.route('/representatives', methods=['GET'])
def getRepresentatives():
	db_reps = db.representatives
	
	json_reps = []

	for rep in db_reps.find():
		json_reps.append({'name' : rep['name'], 'company' : rep['company']})
	
	return jsonify({'result' : json_reps})

@app.route('/test', methods=['GET'])
def test():
	name = 'Andersch Von Monegrabben'
	company = 'EA'

	query = representatives.find_one({'name' : name})

	if query:
		out = {'name' : query['name'], 'company' : query['company']}
	else:
		representatives.insert({'name' : name, 'company' : company})
		out = name + " added"
	
	return jsonify({'result' : out})

@app.route('/representatives/<name>', methods=['GET'])
def getRepresentativeByName(name):
	db_reps = db.representatives
	query = representatives.find_one({'name' : name})
	
	if query:
		out = {'name' : query['name'], 'company' : query['company']}
	else:
		out = 'No results found'

	return jsonify({'result' : out})

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)
