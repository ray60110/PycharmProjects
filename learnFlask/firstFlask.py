from flask import Flask
# from flask import request

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='Ray'):
#    name= request.args.get('name', name)
    return 'Hello Flask from {}!'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
#   we create a new route application that add two number together.
#   the default is str value, if we want to change it like <int: >
#   turn to int value.
def add(num1, num2):
    return "{} + {} = {}".format(num1, num2, num1+num2)

app.run(debug=True, port=8000, host='0.0.0.0')