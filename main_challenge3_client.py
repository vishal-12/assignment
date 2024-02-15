
'''
    Once the server is up and running locally. Execute below commands for sending the request from clinet to server

    Register User -
    python main_challenge3_client.py --json_data '{"name": "Aman", "surname": "Sharma", "email": "aman.sharma@example.com", "phone": "1234567890"}' --task_identifier 'register'

    Fetch User -
    python main_challenge3_client.py --task_identifier 'fetch'

    Delete User -
    python main_challenge3_client.py --json_data '{"name": "Aman", "surname": "Sharma", "email": "aman.sharma@example.com", "phone": "1234567890"}' --task_identifier 'delete'

    PARMAS
    name, surname, email,phone,task_identifier

    Steps-

        1. Run command python main_challenge3_server.py
        2. Verify the server is up and running  for example- Server listening on 127.0.0.1:12345
        3. Execute the four commands for interacting with the server

'''

from challenge3.client import (Client, socket)
import argparse
import json
from logger.logger import logging

if __name__ == "__main__":
    logger = logging()
    logger.set_log_file("")
    parser = argparse.ArgumentParser(description="Client to Server")
    parser.add_argument("--json_data", help="json_data", required=False)
    parser.add_argument("--task_identifier", help="Path to the CSV file", required=True)

    args = parser.parse_args()
    task_identifier = args.task_identifier

    client = Client('127.0.0.1', 12345)

    #load json
    if task_identifier!="fetch":
        if args.json_data =="":
            logging.error("Please Provide correct, --help --json_data ",100,ex=True)
        data = json.loads(args.json_data)
        name = data.get("name",None)
        if name is None:
            logging.error("Name field can't be None, --help --json_data ", 100, ex=True)
        surname = data.get("surname", None)
        if surname is None:
            logging.error("Surname field can't be None, --help --json_data ", 100, ex=True)

        email = data.get("email", None)
        if email is None:
            logging.error("Email field can't be None, --help --json_data ", 100, ex=True)

        phone = data.get("phone", None)
        if phone is None:
            logging.error("phone field can't be None, --help --json_data ", 100, ex=True)

    if task_identifier is None:
        logging.error("task_identifier field can't be None, --help --json_data ", 100, ex=True)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        if task_identifier.lower() =="register":
            # Register a user
            logging.info("=========================Registration Process Started========================".upper())
            register_message = client.register_user(name, surname, email, phone)
            s.sendto(register_message.to_json().encode(), (client.host, client.port))
            data, addr = s.recvfrom(1024)
            response = data.decode('utf-8')
            logging.info("Response from Client - {}".format( data))
            logging.info("===========================Registration Process Completed=====================".upper())
        elif task_identifier.lower() =="fetch":
            print("=======================================Fetching Users==========================".upper())
            get_users_message = client.get_users()
            s.sendto(get_users_message.to_json().encode(), (client.host, client.port))
            data, addr = s.recvfrom(1024)
            logging.info("Response from Client - {}".format( data))
            print("=======================================Script Completed==========================".upper())
        elif task_identifier.lower() == "delete":
            print("======================================Deleting Users===========================".upper())
            get_users_message = client.delete_user(email)
            s.sendto(get_users_message.to_json().encode(), (client.host, client.port))
            data, addr = s.recvfrom(1024)
            logging.info("Response from Client - {}".format( data))
            print("======================================Deleting Completed===========================".upper())
        else:
            logging.error("Failed - Available Options - [register,fetch,delete]",100,ex=True)
    logging.exit_log()


