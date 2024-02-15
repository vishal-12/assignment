'''
    PARAM --text_file_path
    Provide text file path ortherwise it will use tstaging files located on the src folders

    PARAM --csv_file_path
    Provide text file path ortherwise it will use the staging file located on the src folders

    PARMA --csv_out_to_console
    Show the csv output of each line on the console

    PARMA --csv_out_to_console
    Show the txt output of each line on the console

    Please note that this will create the log file in the log directory with latest date and time

    Example - python main_challenge1.py --text_file_path "<>" --csv_file_path "<path>"  --csv_out_to_console --txt_out_to_console
'''

import argparse
import os
from challenge1.extractor import Extractor
from logger.logger import logging

##############
#   LOGGING
############

logging = logging()
logging.set_log_file("")

def getCsvPath():
    global csv_file_path,text_file_path
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    csv_file_path = os.path.join(current_dir, "src", "products.csv")
    text_file_path = os.path.join(current_dir, "src", "products.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract data from text and CSV files.")
    parser.add_argument("--text_file_path", help="Path to the text file",required=False)
    parser.add_argument("--csv_file_path", help="Path to the CSV file",required=False)
    parser.add_argument("--csv_out_to_console", help="Show Output to Console", action="store_true",default=False)
    parser.add_argument("--txt_out_to_console", help="Show Output to Console",  action="store_true",default=False)
    args = parser.parse_args()


    logging.info("Challenge 01 Started")
    if args.text_file_path:
        text_file_path = args.text_file_path
    else:
        text_file_path = None

    if args.csv_file_path:
        csv_file_path = args.csv_file_path
    else:
        csv_file_path=None

    #Get Config FILE
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "config", "config.json")

    if (args.text_file_path == "" or args.text_file_path is None) and (args.csv_file_path == "" or args.csv_file_path is None):
        logging.info("text_file_path and csv_file_path is empty, taking files from src")

        # Get Default sorurce file path
        getCsvPath()
        text_file_path = text_file_path
        csv_file_path = csv_file_path

    # Create Object
    extractor = Extractor(csv_file_path=csv_file_path,text_file_path=text_file_path,logging=logging,config=config_file)

    if args.csv_out_to_console is True:
        extractor.processCsvFile(show=True)
    else:
        extractor.processCsvFile()
    if args.txt_out_to_console is True:
        extractor.processTxtFile(show=True)
    else:
        extractor.processTxtFile()
    logging.info("Challenge 01 Completed")
    logging.exit_log()


