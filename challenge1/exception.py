
import traceback
from logger.logger import logging
import json

class _CommonFileError(FileNotFoundError):
    def __init__(self, message="Error: File not found or cannot be opened."):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)
        logging.error(f'{self.message},{self.traceback}', 100, ex=True)

class _CommonPermissionError(PermissionError):
    def __init__(self, message="Error: Permission denied to write to the file."):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)

class _CommonOSError(OSError):
    def __init__(self, message='Error: An error occurred while writing to the file'):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)

class _CommonTypeError(TypeError):
    def __init__(self, message="Error: Data cannot be serialized to JSON."):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)

class _CommonUnicodeDecodeError(UnicodeDecodeError):
    def __init__(self, message="Error: Data cannot be serialized to JSON."):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)

class _CommonBaseException(Exception):
    def __init__(self, message="Error: Data cannot be serialized to JSON."):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)

class _jsonDecodeError(json.JSONDecodeError):
    def __init__(self, message="Error: JSON Decoding Error"):
        self.traceback = traceback.format_exc()
        self.message = f"{message}\n{self.traceback}"
        super().__init__(self.message)





