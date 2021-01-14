import settings
import redis
import time
import json


# connect to Redis server
db = redis.StrictRedis(host=settings.REDIS_HOST,
    port=settings.REDIS_PORT, db=settings.REDIS_DB)


def classify_process():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    print("* Loading model...")
    # To do
    print("* Model loaded")

    # continually pool for new images to classify
    while True:
        # attempt to grab a batch of images from the database, then
        # initialize the image IDs and batch of images themselves
        queue = db.lrange(settings.IMAGE_QUEUE, 0,
            settings.BATCH_SIZE - 1)
        imageIDs = []
        batch = None

        for q in queue:
            # deserialize the object and obtain the input image
            q = json.loads(q.decode("utf-8"))
            # update the list of image IDs
            imageIDs.append(q["id"])

        # check to see if we need to process the batch
        if len(imageIDs) > 0:
            for imageID in imageIDs:
                output = {"result": "testResult"}
                db.set(imageID, json.dumps(output))

            # remove the set of images from our queue
            db.ltrim(settings.IMAGE_QUEUE, len(imageIDs), -1)

        # sleep for a small amount
        time.sleep(settings.SERVER_SLEEP)


# if this is the main thread of execution start the model server
# process
if __name__ == "__main__":
    classify_process()