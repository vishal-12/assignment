# Challenge -1
'''
    Script name - main_challenge1.py
    PARAM --text_file_path
    Provide text file path ortherwise it will use staging files located on the src folders

    PARAM --csv_file_path
    Provide text file path ortherwise it will use the staging file located on the src folders

    PARAM --only_txt
    If only txt file processing is required

    PARAM --only_csv
    If only csv file processing is required

    PARMA --csv_out_to_console
    Show the csv output of each line on the console

    PARMA --csv_out_to_console
    Show the txt output of each line on the console

    Update the token manually in config file that token will be used for calling all methods and you can prepare your data to test the test cases like name token email etc.

    Command - python main_challenge1.py --text_file_path "<>" --csv_file_path "<path>"  --only_txt --only_csv --csv_out_to_console --txt_out_to_console



# Challenge -2 
Script name - main_challenge1.py
This is the data driven script. It supports all REST Methods [PUT,PATCH,DELETE,GET]
Website https://gorest.co.in/   does not have API for refreshing or creating the tokens. Create your token from https://gorest.co.in/ and add in the config file for testing.
This will create the log file in the log directory with latest date and time

Command - python main_challenge2.py

# Challenge -3
Once the server is up and running locally use command - python main_chanllenge3_server.py. Execute below commands for sending request from clinet to server

    Register User -
    python main_challenge3_client.py --json_data '{"name": "Aman", "surname": "Sharma", "email": "aman.sharma@example.com", "phone": "1234567890"}' --task_identifier 'register'

    Fetch User -
    python main_challenge3_client.py --json_data '{"name": "Aman", "surname": "Sharma", "email": "aman.sharma@example.com", "phone": "1234567890"}' --task_identifier 'fetch'

    Delete User -
    python main_challenge3_client.py --json_data '{"name": "Aman", "surname": "Sharma", "email": "aman.sharma@example.com", "phone": "1234567890"}' --task_identifier 'delete'

    PARMAS
    name, surname, email,phone,task_identifier

    Steps-

        1. Run command python main_challenge3_server.py
        2. Verify the server is up and running  for example- Server listening on 127.0.0.1:12345
        3. Execute the four commands for interacting with the server
