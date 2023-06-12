from google.cloud import aiplatform
from google.oauth2 import service_account

def get_models_list(project_id, location,log):
    try:
        models_list = aiplatform.Model.list(
            project=project_id,
            location=location
        )
        log.info(models_list)
        return models_list
    except Exception as e:
        log.info(f"Failed to retrieve models list: {str(e)}")
        return None
