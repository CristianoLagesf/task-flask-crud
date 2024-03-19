from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return"hello"

@app.route("/about")
def about():
    return"hello about me"

if __name__ == "__main__":  
    app.run(debug=True)