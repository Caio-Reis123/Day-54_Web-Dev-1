from flask import Flask
app = Flask(__name__)

# COMANDOS:
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"
# flask run

def make_bold(func):
    def wrapped():
        return '<b>' + func() + '</b>'
    return wrapped

def make_emphasis(func):
    def wrapped():
        return '<em>' + func() + '</em>'
    return wrapped

def make_underlined(func):
    def wrapped():
        return '<u>' + func() + '</u>'
    return wrapped

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
    '<p>This is a paragratph.</p>' \
    '<img src="https://media4.giphy.com/media/K4x1ZL36xWCf6/giphy.gif?cid=ecf05e47a9dc96da37668a2a99f47402194fdbc0ac205b31&rid=giphy.gif&ct=g" width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return 'Bye'

@app.route('/<name>')
def greet(name):
    return f'Hello {name}'

if __name__ == '__main__':
    app.run(debug=True)