#!/usr/bin/env python

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'hello': 'world'}

api.add_resource(HelloWorld, "/")

'''
@app.route('/')
def hello():
	return "Hello, World!"
'''

if __name__ == "__main__":
# if we are running like python blah.py this will be true
# but if we had imported this file from another file it would be false
	app.run(debug=True)