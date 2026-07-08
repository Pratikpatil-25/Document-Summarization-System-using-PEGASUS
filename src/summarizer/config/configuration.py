from src.summarizer.constants import *
from src.summarizer.utils.common import read_yaml, create_directories
from src.summarizer.entity.config_entity import DocIngestionConfig
from pathlib import Path

class ConfigurationManager:
    def __init__(
        self,
        config_file_path = CONFIG_FILE_PATH,
        params_file_path = PARAMS_FILE_PATH,
        schema_file_path = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])


    def get_doc_ingestion_config(self) -> DocIngestionConfig:
        config = self.config.document_ingestion

        create_directories([config.root_dir])

        doc_ingestion_config = DocIngestionConfig(
            root_dir=Path(config.root_dir),
            upload_dir=Path(config.upload_dir),
            supported_extensions=config.supported_extensions,
        )

        return doc_ingestion_config
