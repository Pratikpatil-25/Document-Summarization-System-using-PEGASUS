from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path

from src.summarizer.config.configuration import ConfigurationManager
from src.summarizer.components.doc_ingestion import DocIngestion

app = FastAPI(
    title="Document Summarization API",
    version="1.0",
    description="Upload PDF, DOCX or TXT files and generate summaries."
)

# Load configuration
config = ConfigurationManager()

document_ingestion_config = ( config.get_doc_ingestion_config() )

document_ingestion = DocIngestion(config = document_ingestion_config )


@app.get("/")
def home():
    return {
        "message": "Document Summarization API is running."
    }


@app.post("/upload")
def upload_document(
    file: UploadFile = File(...)
):
    """
    Upload a document.

    Supported formats:
    - PDF
    - DOCX
    - TXT
    """

    try:

        saved_path = document_ingestion.save_document(file)

        return {
            "message": "Document uploaded successfully.",
            "filename": file.filename,
            "saved_path": str(saved_path)
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )