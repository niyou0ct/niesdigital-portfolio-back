from flask import Flask, request
from flask import json
from flask.json import jsonify

app = Flask(__name__)

incomes = [
    {'description': 'salary', 'amount': 5000}
]

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/api/contact', methods=['POST'])
def get_contact_form():
    # email: str = request.json['email']
    # company: str = request.json['company']
    # detail: str = request.json['detail']

    # response_data = jsonify({email: email, company: company, detail: detail})
    # return response_data

    response = request.get_data()
    return response


@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
