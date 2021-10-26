from flask_restx.fields import String, Boolean, Raw, List, Float, Nested


class DataTransferObjects:
    def __init__(self, ns):
        self.ns = ns

        self.general_responses = {200: 'OK',
                                  404: "Resource not found",
                                  400: "Bad Request",
                                  500: "Internal Server Error"}

        self.plain_text = self.ns.model('plain_text', {
            'plain_text': String(example='some sample text')
        })

        self.text_list = self.ns.model('text_list', {
            'text_list': List(String(), example=['This is the first sentence.', 'This is the second sentence.'])
        })

        self.label = self.ns.model('label', {
            'value': String(example='POSITIVE'),
            'confidence': Float(example=.9)
        })

        self.prediction = self.ns.model('prediction', {
            'text': String(example='some sample text'),
            'labels': List(Nested(self.label))
        })

        self.predictions = self.ns.model('predictions', {
            'predictions': List(Nested(self.prediction))
        })
