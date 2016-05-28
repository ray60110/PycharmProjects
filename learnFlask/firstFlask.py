from flask import Flask
from flask import render_template
# from flask import request

app = Flask(__name__)

@app.route('/<name>')
def index(name='defaultRAY'):
    return render_template('index.html', name_html=name)
#    return 'Hello Flask from {}!'.format(name)

#    view's args is default value. if you type nothing in requests. it should get value from here
#    name= request.args.get('name', name)


@app.route('/')
@app.route('/join/<int:num1>/<int:num2>')
@app.route('/join/<float:num1>/<float:num2>')
@app.route('/join/<int:num1>/<float:num2>')
@app.route('/join/<float:num1>/<int:num2>')
#   we create a new route application that add two number together.
#   the default is str value, if we want to change it like <int: >
#   turn to int value.

#   change int to float make them able to calculate decimal number.
def add(num1=5, num2=3):
    context= {'num11': num1, 'num21': num2}
    return render_template("add.html", **context)

#    return '''
#    <!doctype html>
#    <html>
#    <head><title>ADD NUMBER!</title></head>
#    <body><h1>{} + {} = {}</h1></body>
#    </html>
#    '''.format(num1, num2, num1+num2)

app.run(debug=True, port=8000, host='0.0.0.0')