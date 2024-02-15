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

    def __init__(self, text_file_path=None, csv_file_path=None,logging=None,config=None):
        self.logging = logging
        self.config = config

        if csv_file_path:
            CSV.__init__(self, csv_file_path, self.logging, config=self.config)
        if text_file_path:
            TextFile.__init__(self, text_file_path, self.logging,)

    def outputToConsole(self, products,show=False):
        """
        Output product information to the console.
        """
        self.logging.info("Extracted products:")
        for product in products:
            print(product)
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

    def processCsvFile(self,show=False):
        """
        Parse and Extract Data
        :param product:
        :return:
        """
        #If files are coming from src
        csv_file = self.parseCsvFile(show)
        self.saveToFile(csv_file, self.csvfileName)

    def processTxtFile(self, show=False):
        """
        Parse and Extract Data
        :param product:
        :return:
        """
        txt_file = self.parseTextFile(show)
        self.saveToFile(txt_file,self.txtfileName)







