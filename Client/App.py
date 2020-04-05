import sys
from Happy.Client.Client import Client
from Happy.Client.AccessMainWorkTool import AccessMainWorkTool
from Happy.Client.Contract import ContractHappyWater
from Happy.Client.Control import Control
import time
from Happy.Client.OriginalWidget import OriginalWidget
from PyQt5 import QtWidgets
from Happy.Client.loginUI import LoingUI
import os
class App:

    def __init__(self):

        self.abi = [{'outputs': [],
        'inputs': [{'type': 'address', 'name': '_address'}],
        'constant': False,
        'payable': False,
        'type': 'constructor'},
       {'name': 'set_fortune_number',
        'outputs': [],
        'inputs': [{'type': 'uint256', 'name': '_number'}],
        'constant': False,
        'payable': False,
        'type': 'function',
        'gas': 36172},
       {'name': 'gain_force',
        'outputs': [],
        'inputs': [],
        'constant': False,
        'payable': True,
        'type': 'function',
        'gas': 72349},
       {'name': 'get_my_force',
        'outputs': [{'type': 'uint256', 'unit': 'wei', 'name': ''}],
        'inputs': [{'type': 'address', 'name': '_address'}],
        'constant': False,
        'payable': False,
        'type': 'function',
        'gas': 1365},
       {'name': 'guess_fortune_number',
        'outputs': [],
        'inputs': [{'type': 'uint256', 'name': '_number'}],
        'constant': False,
        'payable': True,
        'type': 'function',
        'gas': 111111},
       {'name': 'get_guess_cost',
        'outputs': [{'type': 'uint256', 'unit': 'wei', 'name': ''}],
        'inputs': [{'type': 'address', 'name': '_address'}],
        'constant': False,
        'payable': False,
        'type': 'function',
        'gas': 1649},
       {'name': 'guest_list',
        'outputs': [{'type': 'uint256', 'unit': 'wei', 'name': ''}],
        'inputs': [{'type': 'address', 'name': 'arg0'}],
        'constant': True,
        'payable': False,
        'type': 'function',
        'gas': 1455},
       {'name': 'guest_guess_rate',
        'outputs': [{'type': 'uint256', 'unit': 'wei', 'name': ''}],
        'inputs': [{'type': 'address', 'name': 'arg0'}],
        'constant': True,
        'payable': False,
        'type': 'function',
        'gas': 1485}]


        self.address = "0xa2ce6Bd34750f4858CF7B09B2B4f5f9995530A50"
        self.contract = ContractHappyWater(self.abi, self.address)

        self.access = AccessMainWorkTool("config/privatenet.toml", "./data")
        try:
            self.client = Client("139.196.158.42",6666)
        except:
            print("服务器fail")
            sys.exit(0)
        self.control = Control(self.access, self.contract, None)

    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        try:
            try:
                self.control.geth_start()
            except:
                os.popen("taskkill /im hammer.exe /F /T")
                time.sleep(2)
                self.control.geth_start()
            time.sleep(1)
            original_widget = OriginalWidget()
            original_widget.show()
            is_connected = self.control.is_connected()
            while is_connected != True:
                self.control.flush_connect()
                is_connected = self.control.is_connected()
                time.sleep(0.1)

            m = LoingUI(self.control, self.client)
            time.sleep(1.2)
            original_widget.close()
            time.sleep(0.5)
            m.show()

        except:
            try:
                self.control.geth_stop()
            except:
                try:
                    self.control.geth_stop_2()
                except:
                    pass
        sys.exit(app.exec_())

if __name__ == '__main__':
    try:
        app = App()
        app.start()
    except:
        sys.exit(0)
