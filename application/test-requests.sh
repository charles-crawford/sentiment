# sample request for the single prediction
curl --location --request POST 'http://0.0.0.0:5001/sentiment/predict-one' \
--header 'Content-Type: application/json' \
--data-raw '{"plain_text": "Some text that could be good or bad."}'

# sample request for the batch predictions
curl --location --request POST '0.0.0.0:5001/sentiment/predict-batch' \
--header 'Content-Type: application/json' \
--data-raw '{"text_list": ["Some text that could be good or bad.", "Some good text.", "Some bad text."]}'