from google.cloud import aiplatform
from google.oauth2 import service_account
import os
from connection import AIPlatformClient
from logs import log_information
from endpoint import EndpointManager
from online_prediction import PredictionManager
from model import get_models_list
from config import Config
from batch_predictions import batchprediction

# Create an instance of the Config class
config = Config()
# Retrieve the values
credentials_path = config.get_credentials_path()
project_id = config.get_project_id()
location = config.get_location()
staging_bucket = config.get_staging_bucket()
display_name = config.get_display_name()
model_path = config.get_model_path()
endpoint_path = config.get_endpoint_path()

filepath = config.get_filepath()
instance = {
    'Id': '52',
    'Time': '2024-12-01'
}
log = log_information().log(filepath)

client = AIPlatformClient(credentials_path, project_id, location, staging_bucket,log)
client.initialize()

 


# endpoint_manager = EndpointManager(display_name,log)
# endpoint = endpoint_manager.create_endpoint()
# if endpoint:
#     endpoint_manager.deploy_model(endpoint, model_path,log)

prediction_manager = PredictionManager(endpoint_path,log)
prediction = prediction_manager.predict(instance)
if prediction:
    print(prediction)

#get models list 

#models_list = get_models_list(project_id, location,log)

#batch prediciton 
batch=batchprediction().predict(log)
fetch=batchprediction().fetch_output(log)

