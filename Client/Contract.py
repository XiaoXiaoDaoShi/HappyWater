"""
创建一个合约内容
"""
import json

class ContractHappyWater:
    def __init__(self,_abi, _address):
        self.abi = _abi
        self.address = _address
        self.deployed_contract = None
        self.CHANGE_POWER = 10**18

    def create_transaction(self,_from,_gas_price = 1, _gas = 3000000):
        """
        创建交易数据
        :param _from:
        :param _gas_price:
        :param _gas:
        :return:
        """
        base_tx = {}
        base_tx["from"] = _from
        base_tx["gasPrice"] = _gas_price
        base_tx["gas"] = _gas
        return base_tx

    def create_contract(self, web3):
        """
        创建合约对象
        :param web3: web3 对象
        :return:
        """
        self.deployed_contract = web3.eth.contract(address=self.address,abi=self.abi)

    def get_contract(self):
        return  self.deployed_contract

    def get_my_force(self,_account):
        """
        查看你原力值
        :param _account:
        :return:
        """
        return self.deployed_contract.functions.get_my_force(_account).call()

    def get_guess_cost(self, _account):
        """
        查看猜测幸运数字的花费
        :param _account:
        :return:
        """
        return self.deployed_contract.functions.get_guess_cost(_account).call()

    def gain_force(self,_account,_value):
        """
        碎片换取原力
        :param _account:
        :return:
        """

        if _value >= self.CHANGE_POWER:
            if _value >= (10**18) * 5:
                rates = 5
            else:
                rates = _value // self.CHANGE_POWER             #取整数倍转换
            real_value = rates * self.CHANGE_POWER
            txarg0 = {
                "from":_account,
                "value":real_value,
                "gasPrice":1000000,
                "gas":3000000
            }
            self.deployed_contract.functions.gain_force().transact(txarg0)
        return real_value

    def gues_fortune_number(self, _account, _number):
        """
        猜测幸运数字
        :param _account:
        :param _number:
        :return:
        """
        need_value = self.get_guess_cost(_account)
        txarg0 = {
            "from": _account,
            "value": need_value,
            "gasPrice": 1,
            "gas": 3000000
        }
        self.deployed_contract.functions.guess_fortune_number(_number).transact(txarg0)

