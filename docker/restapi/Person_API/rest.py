from flask import Flask, jsonify, request, render_template
from sql import SQlConnector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/person', methods=['GET'])
def get_person() :
    connector = SQlConnector()


    data = connector.get_persons()


    return render_template("savedPersons.html", persons = data)

@app.route('/person', methods=['POST'])
def post_person():
    connector = SQlConnector()

    person = request.get_json()

    if (person == None):
        firstName = request.form['first_name']
        lastName = request.form['last_name']
        person = {
            'first_name': firstName,
            'last_name': lastName
        }

        print(person)
        
    if (person == None):
        return render_template("uploadFail.html")
    try:
        data = connector.save_person(person["first_name"], person["last_name"])
    except:
        return render_template("uploadFail.html")

    return render_template("uploadSuccess.html" if data != None else "uploadFail.html")

app.run(debug=False, host='0.0.0.0', port=5000)