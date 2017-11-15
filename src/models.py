import datetime
from flask_mongoengine import MongoEngine
from mongoengine import *

mongo_engine = MongoEngine()

#test
class Credentials(Document):
	email = StringField(max_length=60)
	password = StringField()

class Representatives(Document):
	name = StringField(max_length=60)
	company = StringField()
	credentials = Credentials()