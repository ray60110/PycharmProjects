from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def index2():
    render_template('index.html')


app.run(debug=True, host='0.0.0.0', port=8000)
