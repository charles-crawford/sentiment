## An App for Sentiment Analysis

This is an example app that uses a built-in model from the Python library 
[Flair](https://github.com/flairNLP/flair) to predict the sentiment of the submitted text. 
One endpoint takes in a single object for sentiment prediction, and 
the other takes in a list for batch predictions. The sentiment model used is a transformer based 
model trained on movie and product reviews that is located 
[here](https://nlp.informatik.hu-berlin.de/resources/models/sentiment-curated-distilbert/sentiment-en-mix-distillbert.pt).
The app uses the [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/) library for virtually 
free documentation. The app is fully containerized with [Docker](https://www.docker.com) for ease of 
building and starting.

### Asynchronous Processing
The app is integrated with [Redis](https://redis.io) and [MongoDB](https://www.mongodb.com) for
processing batch requests asynchronously. The library 
[Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html) uses Redis 
to manage async processing. The Python library [Flower](https://flower.readthedocs.io/en/latest/) is
utilized to monitor the tasks that Celery is processing. The results of the async predictions are 
then written to mongodb. A [Mongo-Express](https://github.com/mongo-express/mongo-express) Docker 
container is also started to monitor the MongoDB entries.   

### Run the App 
#### On AWS EC2
If you're deploying locally just skip steps 1 and 2
1. [ssh into your AWS EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html).
2. [Install Docker on your EC2](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)
3. Clone the repo
4. Change directories into the repo
5. To build and run the app use the command

After Step 1 and 2, use these commands to deploy the app:

`git clone git@github.com:charles-crawford/sentiment.git`<br>
`cd sentiment-light`<br>
`docker compose up -d`

### Documentation
After starting the app, the documentation is located at `http://0.0.0.0:5001/`. You can also monitor 
the Celery tasks at  `http://0.0.0.0:5002/`. To check on any batch requests you sent, go to 
`http://0.0.0.0:8081/` to check Mongo-Express for your resulting predictions.

### Testing the App
After starting the app, the documentation is located at `http://0.0.0.0:5001/` where you can test in the 
UI provided by Flask-RESTX.
There is also a curl request in `applications/test-requests.sh` you can use to check 
if the app is up and running. Run these commands from your EC2 shell:

`chmod +x application/test-requests.sh`<br>
`./application/test-requests.sh`

###  Deployed on your EC2
Go to your AWS EC2 console and copy the public ip address for your EC2 instance.
After starting the app, the documentation is located at `http://{your-ec2-ip}:5001/`.
There is a commented out sample curl request in `applications/test-requests.txt` that you can copy and 
paste to your local shell to test the app.  Be sure to replace the IP address with your EC2 public IP.