from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
import os

# TODO: Add Logger


class MyHandler(FTPHandler):
    def on_connect(self):
        print(f"{self.remote_ip}, {self.remote_port} connected")

    def on_disconnect(self):
        # do something when client disconnects
        pass

    def on_login(self, username):
        # do something when user login
        pass

    def on_logout(self, username):
        # do something when user logs out
        pass

    def on_file_sent(self, file):
        # do something when a file has been sent
        pass

    def on_file_received(self, file):
        # do something when a file has been received
        pass

    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        pass

    def on_incomplete_file_received(self, file):
        # remove partially uploaded files
        os.remove(file)


def ftp(ip, port):
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', r'G:\School\Python - Homework\Projects\MekifAdmin\Setup')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((f'{ip}', f'{int(port)}'), handler)
    server.serve_forever()


if __name__ == "__main__":
    ftp('', 2121)
