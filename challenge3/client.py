import socket
import json
from challenge3.message import Message, User
from logger.logger import logging

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def register_user(self, name, surname, email, phone):
        user = User(name, surname, email, phone)
        message = Message("register", user)
        return message

    def get_users(self):
        return Message("get_users")

    def delete_user(self,email):
        user = User(name=None, surname=None, email=email, phone=None)
        return Message("delete",user)
