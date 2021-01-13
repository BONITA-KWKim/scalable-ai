import flask

app = flask.Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    #result["code"] = "0000"
    result = {"code": "0000"}
    return flask.jsonify(result)


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    result = {"code": "0000"}
    return flask.jsonify(result)


if __name__ == '__main__':
    print("* Starting web server ...")
    app.run() 
