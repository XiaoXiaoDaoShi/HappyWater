"""
账户 - 昵称 映射
"""

class User:

    def __init__(self, _account, _name, _force=0, _ip='0.0.0.0'):
        self.account = _account
        self.name = _name
        self.force = _force
        self.ip = _ip


