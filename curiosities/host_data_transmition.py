import flask
app = flask.Flask(__name__)

@app.route("/data")
def data():
    name = flask.request.args.get("name")
    print(name)
    return ""
app.run(host="0.0.0.0", port=3001)
