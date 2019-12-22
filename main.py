from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<user>')
def user(user):
    lista = ['playera','pantalon','camiseta']
    return render_template('user.html',user=user, lista = lista)