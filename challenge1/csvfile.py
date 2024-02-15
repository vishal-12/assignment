
import os
import ntpath
import csv
from challenge1.exception import (_CommonFileError,
                                  _CommonPermissionError,
                                  _CommonOSError,
                                  _CommonTypeError,
                                  _CommonUnicodeDecodeError,
                                  _CommonBaseException)

from helper.helper import loadJson

__author__='Vishal Sharma'
__package__='challenge1'
__name__='CSV'

class CSV:
    def __init__(self,csvFilePath,logging,config=None):
        self.csvFilePath = csvFilePath
        self.logging = logging
        self.csvfileName = ntpath.basename(csvFilePath)
        self.config = config

        #Verify Headers
        json_load = loadJson(self.config)
        csv = json_load.get("csv")["headers"]
        self.verifyHeaders(csv)

    @property
    def csvFilePath(self):
        """
            Get CSV File Path
        :return:
        """
        return self._csvFilePath

    @csvFilePath.setter
    def csvFilePath(self,csvFilePath):
        """
            Validate CSV File
        :param csvFilePath:
        :return:
        """
        try:
            #Check File Path
            if not os.path.exists(csvFilePath) :
                self.logging.error('Error - csvFilePath does not exists, FilePath %s'%csvFilePath,100,ex=True)

            #Check csv file exists or not
            if not ntpath.basename(csvFilePath).endswith(".csv"):
                self.logging.error('Error - File does not contains csv', 100, ex=True)

        except PermissionError as error:
            _CommonPermissionError(error)
        except OSError as error:
            _CommonOSError(error)
        except TypeError as error:
            _CommonTypeError(error)
        except Exception as error:
            _CommonBaseException(error)

        self._csvFilePath = csvFilePath

    def verifyHeaders(self,expectedHeaders):
        """
        Verify File Headers
        :return:
        """
        with open(self.csvFilePath, 'r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the first row (headers)

        if (headers == expectedHeaders) is False:
            self.logging.error(f'CSV file {self.csvFilePath} headers mismatch {headers}',100,ex=True)

    def parseCsvFile(self):
        """
        Parse the CSV file and yield product information as dictionaries.
        """
        try:
            with open(self.csvFilePath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    yield row
        except UnicodeDecodeError as error:
            _CommonUnicodeDecodeError(error)
        except Exception as error:
            _CommonBaseException(error)






