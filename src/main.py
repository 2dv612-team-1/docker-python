import os
from flask import Flask, jsonify, redirect, url_for, request, render_template
import bcrypt

app = Flask(__name__)
app.config['MONGODB_HOST'] = "172.18.0.2"
app.config['MONGODB_PORT'] = 27017

from models import mongo_engine
mongo_engine.init_app(app)

from models import User

user = User(email = 'test@testson.com', company = 'EA')
user.save()

@app.route('/users', methods=['GET'])
def users():
	result = []

	for rep in User.objects:
		result.append({'name' : rep.name, 'company' : rep.company})
	
	return jsonify({'result' : result})

@app.route('/test', methods=['GET'])
def andersch():
	input_name = 'Andersch Von Monegrabben'
	company = 'EA'

	try:
		query = User.objects.get(company = company)
		
		if query:
			result = {'name' : query.name, 'company' : query.company}
		else:
			user = User(name = query.name, company = query.company)
			user.save()
			result = name + " added"

	except User.DoesNotExist:
		result = 'No andersch found'

	return jsonify({'result' : result})

@app.route('/getUserByEmail/<email>', methods=['GET'])
def getUserByÉmail(email):
	#query = Representatives.objects(name = input_name)			returns 'QuerySet' of duplicates
	#query = Representatives.objects.get(name = input_name)		raises DoesNotExist if no document matches the query
	#query = Representatives.objects(name = input_name)[0] 		find one(first) among duplicates
	result = 'No results found'

	try:
		query = User.objects.get(email = email)

		if query:
			result = {'name' : query.name, 'company' : query.company}

	except User.DoesNotExist:
		result = 'No registered user with that email'

	return jsonify({'result' : result})


@app.route('/register', methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		try:
			query = User.objects.get(email = request.form['email'])
			result = 'this user is already registered'

		except User.DoesNotExist:
			hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())#bcrypt.checkpw
			user = User(password = hashpass)
			user.save()
			result = 'success'

	return jsonify({'result': result})

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=80)
