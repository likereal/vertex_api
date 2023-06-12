from google.cloud import aiplatform
from google.oauth2 import service_account

class EndpointManager:
    def __init__(self, display_name,log):
        self.display_name = display_name
        self.log=log
    def create_endpoint(self):
        try:
            endpoint = aiplatform.Endpoint.create(display_name=self.display_name)
            self.log.info('Endpoint created-',endpoint)
            return endpoint
        except Exception as e:
            self.log.error(f"Endpoint creation failed: {str(e)}")
            return None

    def deploy_model(self, endpoint, model_path,log):
        try:
            model = aiplatform.Model(model_path)
            endpoint.deploy(model,
                            min_replica_count=1,
                            max_replica_count=5,
                            machine_type='n1-standard-4',
                            accelerator_type='NVIDIA_TESLA_K80',
                            accelerator_count=1)
            self.log.info("Endpoint deployed to model-",model)
        except Exception as e:
            self.log.error(f"Model deployment failed: {str(e)}")

