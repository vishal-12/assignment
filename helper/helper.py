
from logger.logger import logging
from challenge1.exception import (_CommonFileError,
                                  _CommonPermissionError,
                                  _CommonOSError,
                                  _CommonTypeError,
                                  _CommonUnicodeDecodeError,
                                  _CommonBaseException,
                                  _jsonDecodeError)
import json

def loadJson(jsonFilPath):
    """
    Load JSON File
    :param jsonFilPath:
    :return:
    """
    try:
        with open(jsonFilPath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError as error:
        _CommonFileError(error)
    except json.JSONDecodeError as error:
        _jsonDecodeError(error)
    except Exception as error:
        _CommonBaseException(error)

def verifyJson(config,obj=None):
    """
    Validate Null Values
    :param config:
    :param obj:
    :return:
    """

    # Load Config File
    vjson = loadJson(config)

    # Validate Configs
    for k,v in vjson.items():
        if v is None or v =="":
            logging.error(f'Key {k} Can not be None',100)
            return -1
    return vjson
