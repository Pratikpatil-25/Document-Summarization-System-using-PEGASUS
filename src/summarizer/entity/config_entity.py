from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True) # frozen enures that once an instance of the following class is created the class attributes can't be modified.
class DocIngestionConfig:
  root_dir: Path
  upload_dir: Path
  supported_extensions: list[str]