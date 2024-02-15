import os
import sys
import ntpath
from challenge1.exception import (_CommonPermissionError,
                                  _CommonOSError,
                                  _CommonTypeError,
                                  _CommonUnicodeDecodeError,
                                  _CommonBaseException)

__author__='Vishal Sharma'
__package__='challenge1'
__name__='TextFile'

class TextFile:
    def __init__(self, textFilePath,logging):
        self.textFilePath = textFilePath
        self.logging = logging
        self.txtfileName = ntpath.basename(textFilePath)

    @property
    def textFilePath(self):
        """
         Get Text File Path
        :return:
        """
        return self._textFilePath

    @textFilePath.setter
    def textFilePath(self, textFilePath):
        """
        Validate Text File
        :param textFilePath:
        :return:
        """

        # Check File Path
        try:
            if not os.path.exists(textFilePath):
                self.logging.error('Error - csvFilePath does not exists, FilePath %s'%textFilePath,100,ex=True)

            # Check csv file exists or not
            if not ntpath.basename(textFilePath).endswith(".txt"):
                self.logging.error('Error - File does not contains csv',100,ex=True)

        except PermissionError as error:
            _CommonPermissionError(error)
        except OSError as error:
            _CommonOSError(error)
        except TypeError as error:
            _CommonTypeError(error)
        except Exception as error:
            _CommonBaseException(error)

        self._textFilePath = textFilePath

    def parseTextFile(self,show=False):
        """
        Parse the text file and yield product information as dictionaries.
        """
        if show is True:
            print("Extract TXT :")
        try:
            with open(self.textFilePath, 'r') as file:
                product_info = {}
                for line in file:
                    if line.strip():
                        key, value = line.strip().split(': ')
                        product_info[key] = value
                        if show is True:
                            print (key,":",value)
                    # else:
                    #     if product_info:  # Check if product_info is not empty
                    #         yield product_info
                # Yield the last product_info after reaching the end of the file
                if product_info:
                    yield product_info
        except UnicodeDecodeError as error:
            _CommonUnicodeDecodeError(error)
        except Exception as error:
            _CommonBaseException(error)





