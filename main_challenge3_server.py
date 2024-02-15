
from challenge3.server import Server

if __name__ == "__main__":
    server = Server('127.0.0.1', 12345)
    server.run()