from flair.models import TextClassifier
from flair.tokenization import Sentence
from pymongo import MongoClient
from .. import celery
import os


def load_model():
    return TextClassifier.load('en-sentiment')


def get_collection():
    client = MongoClient(os.environ.get('MONGODB_URL'))
    db = client[os.environ.get('MONGO_DB_NAME')]
    collection = db[os.environ.get('MONGO_COLLECTION_NAME')]
    return collection


sentiment_model = load_model()


@celery.task()
def get_sentiment_batch(text_list):
    collection = get_collection()
    sentiments = []
    for text in text_list:
        sentence = Sentence(text)
        sentiment_model.predict(sentence)
        sentence = sentence.to_dict()
        del sentence['entities']
        sentiments.append(sentence)

    collection.insert_many(sentiments)


def get_sentiment(text):
    sentence = Sentence(text)
    sentiment_model.predict(sentence)
    sentence = sentence.to_dict()
    del sentence['entities']
    return sentence
