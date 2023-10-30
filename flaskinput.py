
print ("aaa")
from flask import Flask
from flask import Flask,jsonify,request

from flask import Flask, request, render_template

flaskinput = Flask(__name__)


"""
@flaskinput.route("/")
def hello():
  return "Hello World CS298- Jim2 !"
"""

myDict = {'dumm1': [1, 2, 3, 4, 5],
          'RFRO': [1.5, 1, 1, 2.2, 1],
          'PCCO': [3, 4, 5, 6, 7]   }

@flaskinput.route('/')
def my_form():
    return render_template('my-form.html')


@flaskinput.route('/returnmydict', methods = ['GET'])
def ReturnJSON1():
    if(request.method == 'GET'):
        return jsonify(myDict)


@flaskinput.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }

        return jsonify(data)


@flaskinput.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    
    return processed_text


if __name__ == '__main__':
     flaskinput.run (host="0.0.0.0", port=8080)