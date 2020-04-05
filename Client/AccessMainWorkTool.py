"""
    连接主要运行工具，geth
"""

import subprocess
import os
import psutil

class AccessMainWorkTool:

    def __init__(self, config, ethash_dagdir, log_path="cache"):
        """

        :param datadir: 和Init的路劲相同 否则chainId 会 出错
        :param ethash_dagdir:
        :param networkid:
        :param wsapi:
        """

        self.ethash_dagdir = ethash_dagdir
        self.log = log_path
        self.config = config
        self.process = None

    def start(self):
        command = "hammer --config {} --ethash.dagdir {}"\
            .format(self.config, self.ethash_dagdir)

        self.process = subprocess.Popen(command, shell=True, close_fds=True)
        p = psutil.Process(self.process.pid)


    def stop(self):
        os.popen("taskkill /im hammer.exe /F /T")


    def stop_2(self):
        # 根据进程名杀死
        for p in psutil.pids():
            t_p = psutil.Process(p)
            if t_p.name() == "hammer.exe":

                os.kill(p,9)


