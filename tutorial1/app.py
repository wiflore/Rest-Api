from flask import Flask, jsonify, request
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!2"

@app.route('/page1')
def page1():
    return str(100*random.random())

@app.route('/page2')
def page2():
    json = {
        'num1':str(100*random.random()),
        'num2':str(10*random.random()**2),
        'extra':[
            {'name':'n'}, 
            {'earning':3834384}
        ]
    }
@app.route('/post', methods=["POST"])
def post():
    
    dataDict = request.get_json()

    try:
        retJSON = {"result":dataDict['x'] + dataDict['y']}
    except:
        return "ERROR", 305

    return jsonify(retJSON), 200


    
    return jsonify(json)
if __name__ == "__main__":
    app.run(debug=True)

#can return JSON, page.html, render_template('index.html'), String