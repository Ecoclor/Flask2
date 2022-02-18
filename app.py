from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hola, caracola!"
    echo("Hola   2")