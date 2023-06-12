from google.cloud import aiplatform
from google.oauth2 import service_account
from google.cloud import storage
import os

class batchprediction:
    def predict(self,log):
        try:
            model = aiplatform.Model('projects/quiet-seer-385808/locations/us-central1/models/6538146938523484160')
            batch_prediction_job = model.batch_predict(
            job_display_name='my-batch-prediction-job25',
            
            machine_type='n1-standard-4',
            instances_format='csv',
            predictions_format= "csv",

            gcs_source=['gs://bucket_for_gcp_api_batch_predictions/Google_Demo_1.csv'],
            gcs_destination_prefix='gs://bucket_for_gcp_api_batch_predictions/batch_preds/',
            service_account='89457747473-compute@developer.gserviceaccount.com'
            )
            log.info(batch_prediction_job)
            
        except Exception as e:
            log.info("Prediction failed")
            return None
        
    def fetch_output(self,log):
        local_directory = r'C:\relanto\api\gcp\final1'
        bucket_name = 'bucket_for_gcp_api_batch_predictions'
        prefix = 'batch_preds/'

        storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)

        for blob in blobs:
            destination_path = os.path.join(local_directory + 'Output')
            blob.download_to_filename(destination_path)
            log.info(f"Downloaded {blob.name} to {destination_path}")
            
