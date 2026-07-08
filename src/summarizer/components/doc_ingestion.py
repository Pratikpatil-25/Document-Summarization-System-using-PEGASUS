import os
from src.summarizer.utils.common import create_directories
from src.summarizer.logging import logger
from src.summarizer.utils.common import get_size
from src.summarizer.entity.config_entity import DocIngestionConfig
from pathlib import Path
import shutil
from fastapi import UploadFile


class DocIngestion:
    """
    Responsibilities:
    -----------------
    1. Create the required artifact directories.
    2. Validate uploaded document type.
    3. Save uploaded document.
    """

    def __init__(self, config: DocIngestionConfig):
        self.config = config

        create_directories(
            [
                self.config.root_dir,
                self.config.upload_dir
            ]
        )



    def validate_document(self, filename: str) -> bool:

        extension = Path(filename).suffix.lower()

        return extension in self.config.supported_extensions
    


    def save_document(self, uploaded_file: UploadFile) -> Path:
        
        if not self.validate_document(uploaded_file.filename):
            raise ValueError(
                f"Unsupported file type: {Path(uploaded_file.filename).suffix}"
            )

        destination = ( self.config.upload_dir / uploaded_file.filename )

        with open(destination, "wb") as file:
            shutil.copyfileobj(
                uploaded_file.file,
                file
            )

        logger.info(
            f"Document saved successfully at: {destination}"
        )

        return destination