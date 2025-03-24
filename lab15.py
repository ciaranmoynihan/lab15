from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def hello():
    s1 = '<p>afaik</p>'
    s2 = '<p>btw</p>'
    s3 = '<p>jic</p>'
    s4 = '<p>lol</p>'
    return s1 + s2 + s3 + s4

@app.route('/ciaran')
def t_test():
   return render_template('template1.html')

