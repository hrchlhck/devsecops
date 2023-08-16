from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<head><title>DevSecOps</title></head><h1>Olá, mundo!</h1>"

def capitalize(s: str):
    return s.capitalize()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)