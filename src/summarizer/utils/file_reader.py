from pathlib import Path
from ensure import ensure_annotations
from src.summarizer.logging import logger
import fitz
from docx import Document



# read text file
@ensure_annotations
def read_text_file(path: Path) -> str:
    """
    Load text from a file.

    Args:
        path (Path): Path of text file.

    Returns:
        str: File contents.
    """

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    logger.info(f"Text File read from {path}")

    return text



# read pdf file
@ensure_annotations
def read_pdf_file(path: Path) -> str:
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    logger.info(f"PDF File read from {path}")
    return text


# read word file
@ensure_annotations
def read_word_file(path: Path) -> str:
    
    doc = Document(path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    logger.info(f"Word File read from {path}")
    return text