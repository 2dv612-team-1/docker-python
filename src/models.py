import datetime
from flask_mongoengine import MongoEngine
from mongoengine import *

mongo_engine = MongoEngine()

class User(mongo_engine.Document):
	name = StringField(max_length=60)
	company = StringField()
	email = StringField(max_length=60)
	password = StringField()