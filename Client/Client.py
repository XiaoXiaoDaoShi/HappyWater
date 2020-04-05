"""
客户端，向服务器交互信息
"""

from socket import socket, AF_INET, SOCK_STREAM


BUFFER_SIZE = 2048

class Client:

    def __init__(self,_host, _port):
        self.host = _host
        self.port = _port
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect((self.host,self.port))


    def query_all(self):
        """
        查找所有
        :return:  list
        """
        data = '{"type":1}'

        response = self.send_data_and_receive(data)

        return list(eval(response))

    def query_one(self,_account):
        """
        查找一个
        :param _account:
        :return: tuple
        """
        data = '{' + '"type":2,"account":"{}"'.format(_account) + '}'
        response = response = self.send_data_and_receive(data)
        return eval(response)

    def insert_one(self, _account, _name):
        """
        插入一个user
        :param _account:
        :param _name:
        :return:
        """
        data = '{' + '"type":3,"account":"{}","name":"{}"'.format(_account,_name) + '}'
        response = response = self.send_data_and_receive(data)
        return eval(response)

    def update_force(self, _account, _force):
        """
        上传force
        :param _account:
        :param _force:
        :return:
        """
        data = '{' + '"type":4,"account":"{}","force":{}'.format(_account, _force) + '}'
        response = response = self.send_data_and_receive(data)
        return eval(response)

    def send_data_and_receive(self, _data):

        self.client_socket.send(_data.encode())

        response = self.client_socket.recv(BUFFER_SIZE)

        response = response.decode()

        return response

    def close(self):
        data = '{"type":0}'
        self.client_socket.send(data.encode())
        self.client_socket.close()

    def connect(self):
        self.client_socket.connect((self.host, self.port))


