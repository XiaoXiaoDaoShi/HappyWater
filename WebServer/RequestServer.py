"""
服务器端，与客户端交互
"""
from datetime import datetime
from UserDao import UserDao
from User import User
from socketserver import StreamRequestHandler, ThreadingTCPServer
import json
import time
BUFFER_SIZE= 2048

class RequestServer(StreamRequestHandler):



    def handle(self):
        """
        客户端连接服务器后的处理方法
        :return:
        """

        while True:
            data = self.request.recv(BUFFER_SIZE)

            decode_data = data.decode()

            data_dict = json.loads(decode_data)
            control_infomation = "无信息内容"
            result = None
            if data_dict['type'] == 1:
                #查询所有
                result = self.query_all()
                control_infomation = "查询所有信息"

            elif data_dict['type'] == 2:
                # 查询单个
                account = data_dict['account']
                result = self.query_one(account)
                control_infomation = "查询账户:{}的信息".format(account)

            elif data_dict['type'] == 3:
                # 插入单个
                account = data_dict['account']
                name = data_dict['name']
                host, port = self.client_address
                result = self.insert_one(account, name, host)
                control_infomation = "插入账户:{},名字:{}".format(account, name)

            elif data_dict['type'] == 4:
                # 跟新 force
                account = data_dict['account']
                force = data_dict['force']
                result = self.update_force(account, force)
                control_infomation = "更新账户:{},force:{}".format(account,force)
            elif data_dict['type'] == 0:
                control_infomation = "退出"
                print("来自{}的操作: {}".format(host, control_infomation))
                break

            self.request.sendall(str(result).encode())
            now = datetime.now()
            host, port = self.client_address
            print("来自{}的操作: {}".format(host,control_infomation), "  ",now)
        self.request.close()


    def query_all(self):
        userDao = UserDao()
        result = userDao.query_all()
        userDao.close()
        return result

    def query_one(self,_account):
        userDao = UserDao()
        result = userDao.query_one_by_account(_account)
        userDao.close()
        return result

    def insert_one(self,_account,_name,_ip):
        userDao = UserDao()
        user = User(_account, _name, _ip=_ip)
        result = userDao.insert_one(user)
        userDao.close()
        return result

    def update_force(self,_account, _force):
        userDao = UserDao()
        result = userDao.update_force(_account, _force)
        userDao.close()
        return result


if __name__ == '__main__':
    server = ThreadingTCPServer(("localhost",6666), RequestServer)
    print("start server")
    server.serve_forever()