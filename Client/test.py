
import subprocess
import os



if __name__ == '__main__':
    os.chdir("G:\Program Files\Geth")
    order = 'geth --dev --datadir "./dev" --ethash.dagdir "./dev" --networkid 15 --ws --wsport 6666 console'
    t = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    x = str(input("input:\n"))
    while x != "0000":
        print(x)
        out = t.communicate(x)
        print("out:",out)
        print(t.stdout.read())
        x = str(input("input:\n"))
