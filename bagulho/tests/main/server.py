from flask import Flask
app = Flask(__name__)
import random


random_number = random.randint(0,9)
print(random_number)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'

@app.route('/<int:number>')
def acerto(number):
    if number == random_number:
        return '<h1 style="color:MediumSeaGreen">ACERTOO</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    if number <= random_number:
        return '<h1 style="color:DodgerBlue">MAIS ALTO</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    if number >= random_number:
        return '<h1 style="color:Tomato;">MAIS BAIXO</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True)