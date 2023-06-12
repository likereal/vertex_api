import configparser

class Config:
    def __init__(self):
        # Create the ConfigParser object
        self.config = configparser.ConfigParser()

        # Read the INI file
        self.config.read('dev.ini')

    def get_credentials_path(self):
        return self.config.get('Credentials', 'credentials_path')

    def get_project_id(self):
        return self.config.get('Project', 'project_id')

    def get_location(self):
        return self.config.get('Project', 'location')

    def get_staging_bucket(self):
        return self.config.get('Storage', 'staging_bucket')

    def get_display_name(self):
        return self.config.get('Endpoint', 'display_name')

    def get_model_path(self):
        return self.config.get('Endpoint', 'model_path')

    def get_endpoint_path(self):
        return self.config.get('Endpoint', 'endpoint_path')

    def get_filepath(self):
        return self.config.get('FilePath', 'filepath')
