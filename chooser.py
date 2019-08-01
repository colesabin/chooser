from flask import Flask, render_template, jsonify
from random import randrange

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Good Ham </h1>"

@app.route("/random")
def random():
    return render_template('random.html')

@app.route("/rand_num")
def rand_num():
    result = {"number": randrange(1000000000)}
    print(result)
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
