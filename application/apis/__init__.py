from flask_restx import Api
from application.apis.sentiment import api as sentiment


api = Api(
    title='Sentiment Analysis',
    version='1.0',
    description='Sentiment Analysis'
)

api.add_namespace(sentiment, path='/sentiment')
