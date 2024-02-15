import socket
from challenge3.message import Message
import json
import datetime

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.users = {}

    def process_message(self, data):
        """
        Process Messages
        :param data:
        :return:
        """
        if data.type == 'register':
            return self.register_user(data.user)
        elif data.type == 'delete':
            return self.delete_user(data.user.email)
        elif data.type == 'get_users':
            return self.get_users()

    def currentDateTime(self):
        """
            Get Current Date Time
        :return:
        """
        # Fetch current date and time
        current_datetime = datetime.datetime.now()

        # Convert current date and time to string format
        current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        return current_datetime_str

    def register_user(self, user):
        """
        Register User
        :param user:
        :return:
        """
        if user.email in self.users:
            msg = "User Already Exists"
        else:
            msg = "Registration Successful"
            self.users[user.email] = user.to_dict()
        return {
            "Message":msg,
            "createdAt" : self.currentDateTime(),
            "Result" : "Successful"
        }

    def delete_user(self, email):
        """
        Delete Users
        :param email:
        :return:
        """
        if email in self.users:
            del self.users[email]
            return {
                "Message" : "User deleted successfully",
                "createdAt": self.currentDateTime()
            }
        else:
            return {
                "Message" : "User not found",
                "createdAt": self.currentDateTime()
            }

    def get_users(self):
        """
        Get ALL Users
        :return:
        """
        return {
            "Message" : "Fetched Successfully",
            "user" : list(self.users.values()),
            "createdAt": self.currentDateTime(),
        }

    def run(self):
        """
        Run Server
        :return:
        """
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind((self.host, self.port))
            print(f"Server listening on {self.host}:{self.port}")
            while True:
                data, addr = s.recvfrom(1024)
                message = Message.from_json(data.decode())
                response = self.process_message(message)
                print ('Response from Serer -', response)
                s.sendto(json.dumps(response).encode(), addr)


