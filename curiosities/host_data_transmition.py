import flask
app = flask.Flask(__name__)

@app.route("/data")
def data():
    name = flask.request.args.get("name")
    file.write(flask.request.remote_addr + "\n")
    print(name)
    return ""

@app.route("/close")
def close_server():
    file.close()
    exit()
file = open("log", "w")

app.run(host="0.0.0.0", port=3001)
file.close()
