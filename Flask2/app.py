from flask import Flask

## Configuration



app = Flask(__name__)

@app.route("/flask2")
def home():
    return "Welcome to Flask 2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
