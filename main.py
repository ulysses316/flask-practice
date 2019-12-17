from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def profile(name):
    return("<h1>Bienvenido {}</h1>".format(name))

@app.route('/id/<int:id>')
def book(id):
    id += 10
    return("The id of the book is {}".format(id))

# Nos quedamos en la pagina 32 de el libro de flask