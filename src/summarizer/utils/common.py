import os
from box.exceptions import BoxValueError  # This exception occurs when converting an empty dictionary or invalid data into a ConfigBox.
import yaml
from src.summarizer.logging import logger
import json  
import joblib  # Used to save and load Python objects in binary format.
               # Commonly used in ML for:
                # Saving trained models
                # Saving preprocessors
                # Saving scalers
from ensure import ensure_annotations # This is a decorator that checks whether function arguments match their type hints.
from box import ConfigBox  # ConfigBox converts a dictionary into an object. So that we can access dictionary items using '.' notation. Eg. dict = {"k1":"val1","k2":"val2"} we can only access 'val1' using dict['k1'] but it is easy using this syntax : "dict.k1". ConfigBox allows us this as it converts the dictionary into an object.
from pathlib import Path 
from typing import Any  # Any means the variable can be of any data type.



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):  # if verbose == True then the function prints diagnostic info such as which dir is being created or noting if already exists. if verbose == False then the function runs silently, providing no output unless an error occurs.
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as file:
        json.dump(data, file, indent=4)  # indent parameter specifies the number of spaces to use for indentation, making the JSON output human-readable.

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)




# @ensure_annotations
# def save_text(path: Path, text: str):
#     """
#     Save text to a file.

#     Args:
#         path (Path): Destination file path.
#         text (str): Text to save.
#     """

#     with open(path, "w", encoding="utf-8") as file:
#         file.write(text)

#     logger.info(f"Text saved at {path}")






# @ensure_annotations
# def save_bin(data: Any, path: Path):
#     """save binary file

#     Args:
#         data (Any): data to be saved as binary
#         path (Path): path to binary file
#     """
#     joblib.dump(value=data, filename=path)
#     logger.info(f"binary file saved at: {path}")


# @ensure_annotations
# def load_bin(path: Path) -> Any:
#     """load binary data

#     Args:
#         path (Path): path to binary file

#     Returns:
#         Any: object stored in the file
#     """
#     data = joblib.load(path)
#     logger.info(f"binary file loaded from: {path}")
#     return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"