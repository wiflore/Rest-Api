from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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
api.add_resource(Divide, "/divide")

@app.route('/')
def welcome():
    return "Welcome"

if __name__=="__main__":
    app.run(debug=True)