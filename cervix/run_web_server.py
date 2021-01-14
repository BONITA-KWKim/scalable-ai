import flask
import redis
import settings

app = flask.Flask(__name__)
db = redis.StrictRedis(host=settings.REDIS_HOST,
    port=settings.REDIS_PORT, db=settings.REDIS_DB)


@app.route("/")
def homepage():
    return "Welcome to the Keras REST API!"


@app.route("/predict", methods=["GET", "POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if "POST" == flask.request.method:
        if flask.request.files.get("image"):
            # indicate that the request was a success
            data["success"] = True
    elif "GET" == flask.request.method:
        print(db.ping())
        if True == db.ping():
            return "Redis is ready"
        else:
            return "Redis is not ready"

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


if __name__ == "__main__":
	print("* Starting web service...")
	app.run()