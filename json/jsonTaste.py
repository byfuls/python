import json

################
# dict to json
################
dictObj = {1: "a", 2: "b", 3: "c"}
jsonObj = json.dumps(dictObj)
print(jsonObj)

################
# class to json
################
class objClass:
	def __init__(self):
		self.a = 1
		self.b = 2
		self.c = 3
classObj = objClass()
jsonObj = json.dumps(classObj.__dict__)
print(jsonObj)
