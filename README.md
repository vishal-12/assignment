# Download Python:
Go to the official Python website at https://www.python.org/downloads/ and download the latest version of Python for your operating system. Make sure to select the appropriate installer for your system (Windows, macOS, or Linux).

# Run the Installer:
Once the download is complete, run the installer program that you downloaded in the previous step. Follow the on-screen instructions to install Python on your system. During the installation process, you may have the option to customize the installation directory. Note down this directory if you choose to customize it.

# Check "Add Python to PATH" (For Windows Users):
If you're using Windows, make sure to check the option that says "Add Python to PATH" during the installation process. This will automatically add Python to your system's PATH environment variable, making it easier to run Python from the command prompt or terminal.
Verify Installation:

# After the installation is complete, open a command prompt (Windows) or terminal (macOS/Linux) and type the following command to verify that Python has been installed successfully:
bash
Copy code
python --version
This command should display the installed Python version.
Add Python to PATH (Optional):
If you didn't check the option to add Python to the PATH during installation (Windows), or if you customized the installation directory on any operating system, you'll need to manually add Python to the system # 

# PATH Windows:
Search for "Environment Variables" in the Start menu and open "Edit the system environment variables."
In the System Properties window, click on the "Environment Variables" button.
In the Environment Variables window, under "System variables," select the "Path" variable and click "Edit."
Click "New" and add the path to the directory where Python was installed (e.g., C:\Python39 or whatever path you selected during installation).
Click "OK" to save the changes.

# macOS/Linux:
Open your shell configuration file (e.g., ~/.bash_profile, ~/.bashrc, ~/.zshrc, etc.) in a text editor.
Add the following line at the end of the file, replacing /path/to/python with the actual path where Python is installed (usually /usr/local/bin/python or similar):
bash
Copy code
export PATH="/path/to/python:$PATH"
Save the file and exit the text editor.
# Install modules for using the functionality 
pip install -r requirement.txt

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

    PARAM --csv_out_to_console
    Show the csv output of each line on the console

    PARAM --csv_out_to_console
    Show the txt output of each line on the console

    Update the token manually in config file that token will be used for calling all methods and you can prepare your data to test the test cases like name token email etc.

    Command - python main_challenge1.py --text_file_path "<>" --csv_file_path "<path>"  --only_txt --only_csv --csv_out_to_console --txt_out_to_console


# Challenge -2 
Script name - main_challenge2.py
This is the data driven script. It supports all REST Methods [PUT,PATCH,DELETE,GET]
Website https://gorest.co.in/   does not have API for refreshing or creating the tokens. Create your token from https://gorest.co.in/ and add in the config file for testing.
This will create the log file in the log directory with latest date and time

Command - python main_challenge2.py

Run the test cases -
command pytest

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
