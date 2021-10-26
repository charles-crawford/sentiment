## An App for Sentiment Analysis

This is an example app that uses a built-in model from the Python library Flair to predict the 
sentiment of the submitted text. One endpoint takes in a single object for sentiment prediction, and 
the other takes in a list for batch predictions.

### Asynchronous Processing
The app is integrated with redis and mongodb for processing batch requests asynchronously. 
The library celery uses redis to manage async processing. 
The results of the async predictions are then written to mongodb.

### Run the App
To build and run the app use the command: `docker compose up -d` 

### Documentation
After starting the app, the documentation is located at http://0.0.0.0:5001/.