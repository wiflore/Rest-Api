from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users':0
})

class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set": {"num_of_users":new_num}})
        return str("Hello user " + str(new_num))

def checkPostedData(postedData, functionName):
    NumberTypes = (int, float, complex)
    if not isinstance(postedData['y'], NumberTypes): return 301
    if not isinstance(postedData['x'], NumberTypes): return 301

    if (functionName == "divide"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        elif(postedData['y']==0):
            return 302
        else :
            return 200

    else:
        if "x" not in postedData or "y" not in postedData:
            return 301
        else :
            return 200        
        

class Add(Resource):
    def post(self):
        #equivalent ["POST"]
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson = {
                'Message':"An error happened",
                'Status Code':status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x+y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }

        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        #equivalent ["POST"]
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "subtract")
        if (status_code!=200):
            retJson = {
                'Message':"An error happened",
                'Status Code':status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x-y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }

        return jsonify(retMap)

class Multiply(Resource):
    def post(self):
        #equivalent ["POST"]
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "add")

        if (status_code!=200):
            retJson = {
                'Message':"An error happened",
                'Status Code':status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x*y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }

        return jsonify(retMap)

class Divide(Resource):
    def post(self):
        #equivalent ["POST"]
        postedData = request.get_json()

        status_code = checkPostedData(postedData, "divide")
        if (status_code!=200):
            retJson = {
                'Message':"An error happened",
                'Status Code':status_code
            }
            return jsonify(retJson)

        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = x/y

        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        
        return jsonify(retMap)
    pass

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/hello")

@app.route('/')
def welcome():
    return "Welcome"

if __name__=="__main__":
    app.run(host='0.0.0.0')