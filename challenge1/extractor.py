import csv
import json
import os
import sys
from challenge1.csvfile import CSV
from challenge1.textfile import TextFile
import heapq

__package__='challenge1'
__name__='Extractor'

class Extractor(CSV,TextFile):

    def __init__(self, text_file_path=None, csv_file_path=None,logging=None,config=None,fileType=None):
        self.logging = logging
        self.config = config

        self.fileType =fileType
        if self.fileType is not None:
            if fileType.lower() =="csv":
                CSV.__init__(self,csv_file_path,self.logging,config=self.config)
            elif self.fileType.lower() =="txt":
                TextFile.__init__(self,text_file_path,self.logging)
        else:
            CSV.__init__(self, csv_file_path, self.logging, config=self.config)
            TextFile.__init__(self, text_file_path, self.logging)

    def outputToConsole(self, products,filType =None):
        """
        Output product information to the console.
        """

        self.logging.info("Extracted products:")
        for product in products:
            self.logging.info(product)
        self.logging.info("Extraction Completed")

    def saveToFile(self, data,output_file):
        """
        Save data to a JSON file.
        """
        self.logging.info("Dumping to file initiated:")
        output_file = self.logging.addDateTime(output_file)
        for item in data:
            with open(output_file, 'w+') as file:
                json.dump((item), file, indent=4)
        self.logging.info("Dumping to file completed:")

    def combinedRun(self):
        """
        Parse and Extract Data
        :param product:s
        :return:
        """
        if self.fileType.lower() == "csv":
            csv_file = self.parseCsvFile()
            self.saveToFile(csv_file, self.csvfileName)
        elif self.fileType.lower() == "txt":
            txt_file = self.parseTextFile()
            self.saveToFile(txt_file,self.txtfileName)
        else:
            csv_file = self.parseCsvFile()
            self.saveToFile(csv_file, self.csvfileName)
            txt_file = self.parseTextFile()
            self.saveToFile(txt_file, self.txtfileName)






