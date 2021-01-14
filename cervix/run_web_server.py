import flask
import redis
import settings
import uuid
import json
import time


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
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))

            # indicate that the request was a success
            data["success"] = True
    elif "GET" == flask.request.method:
        print(db.ping())
        if True == db.ping():
            k = str(uuid.uuid4())
            t_data = {"id": k, "testField": "testValue"}
            db.rpush(settings.IMAGE_QUEUE, json.dumps(t_data))
            while True:
                output = db.get(k)
                if output is not None:
                    db.delete(k)
                    break
                # sleep for a small amount to give the model a chance
                # to classify the input image
                time.sleep(settings.CLIENT_SLEEP)
            return "Redis is ready"
        else:
            return "Redis is not ready"

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


if __name__ == "__main__":
    print("* Starting web service...")
    app.run()