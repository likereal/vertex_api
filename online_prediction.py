from google.cloud import aiplatform
from google.oauth2 import service_account

class PredictionManager:
    def __init__(self, endpoint_path,log):
        self.endpoint_path = endpoint_path
        self.log=log

    def predict(self, instance):
        try:
            endpoint = aiplatform.Endpoint(self.endpoint_path)
            prediction = endpoint.predict(instances=[instance])
            self.log.info(prediction.predictions[0]['value'])
            return prediction
        except Exception as e:
            self.log.info(f"Prediction failed: {str(e)}")
            return None