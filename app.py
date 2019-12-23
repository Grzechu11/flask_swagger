# app.py - a minimal flask api using flask_restful
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route('/index')
def main():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    content = "Welcome!"
    content = " " + formatted_now
    return content

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')