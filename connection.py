from google.cloud import aiplatform
from google.oauth2 import service_account
import os

class AIPlatformClient:
    def __init__(self, credentials_path, project_id, location, staging_bucket,log):
        self.credentials_path = credentials_path
        self.project_id = project_id
        self.location = location
        self.staging_bucket = staging_bucket
        self.log=log

    def initialize(self):
        try:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
            aiplatform.init(
                project=self.project_id,
                location=self.location,
                staging_bucket=self.staging_bucket,
                credentials=service_account.Credentials.from_service_account_file(self.credentials_path),
                experiment='pred-1-exp',
                experiment_description='my experiment description'
            )

            self.log.info("Connection Established")
        except Exception as e:
            self.log.error("Initialization failed: {str(e)}")
