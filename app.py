from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello again from Dockerised Flask <br><br> THIS IS AN UPDATE PUSHED TO GITHUB AND AUTOMATICALLY DEPLOYED BY AZURE CI/CD Pipeline"

@app.route("/route32a")
def route32a():
    return "Hello from the 32A"

@app.route("/route")
def route():
    number=request.args.get('number')
    return "Hello from the {}".format(number)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')
