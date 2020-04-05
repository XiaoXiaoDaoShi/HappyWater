"""
控制与gethd 交互
"""
from web3 import Web3



class Control:
    def __init__(self,_access_tool, _contract, _uri, _account=None,_passwd=None):
        self.access_tool = _access_tool
        self.uri = _uri
        self.web3 = Web3(Web3.IPCProvider(_uri))
        self.passwd = _passwd
        self.account = _account
        self.contract = _contract

    def unlock_account(self):
        result = False
        if self.passwd !=None and self.account !=None:
            try:

                result = self.web3.geth.personal.unlockAccount(self.account, self.passwd)
            except:
                result = False
        return result

    def new_account(self,_passwd):
        """
        申请一个账户
        :param _passwd:
        :return:
        """
        return self.web3.geth.personal.newAccount(_passwd)

    def start_work(self, _thread_number):
        """
        开始 挖
        :return:
        """
        self.web3.geth.miner.start(_thread_number)

    def stop_work(self):
        """
        结束挖
        :return:
        """
        self.web3.geth.miner.stop()

    def get_balacne(self):
        result = self.web3.eth.getBalance(self.account)
        return result

    def is_connected(self):
        """
        查看是否连接上
        连接成功才创建合约对象
        :return: bool
        """
        result = self.web3.isConnected()
        if result:
            self.contract.create_contract(self.web3)
        return result


    def show_accounts(self):
        return self.web3.eth.accounts

    def get_account(self):
        return self.account

    def set_account(self,_account):
        self.account = _account

    def set_passwd(self, _passwd):
        self.passwd = _passwd

    def set_coinbase(self, _account):
        self.web3.geth.miner.set_etherbase(_account)

    def geth_stop(self):
        self.access_tool.stop()

    def geth_stop_2(self):
        self.access_tool.stop_2()

    def geth_start(self):
        self.access_tool.start()

    def flush_connect(self):
        # 刷新 web3 连接
        self.web3 = Web3(Web3.IPCProvider(self.uri))


