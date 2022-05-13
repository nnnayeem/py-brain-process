import time
import serial
from scope import Scope
import matplotlib.pyplot as plt
import threading


class Main:

    def __init__(self):
        print("initiated")
       
    def run(self, scp):
        # i = 0
        # while 1:
        #     time.sleep(0.01)
        #     i = i + 1
        #     scp.set(i*0.1)
        #     if i > 10: i = 0

        with serial.Serial('COM4', 115200, timeout=1) as ser:    
            print("Found serial port com1")
            attempt = 0
            while 1:
                if attempt == 5: break
                fileIndex = input("Enter data save index (1-5) To initiate compair mode press c:")
                filename = "data.{findex}.txt".format(findex = fileIndex)

                i = 0
                while 1:
                    if ser.in_waiting > 0:
                        data = ser.read(5)
                        data = data.decode('utf-8')
                        with open(filename, 'a') as out:
                            out.write(data)
                        i = i + 1
                        print(i)
                        if i == 200: break
                    time.sleep(0.01)
                attempt = attempt + 1


if __name__ == "__main__":
    fig, ax = plt.subplots()
    scope = Scope(ax)
    application = Main()

    s2 = threading.Thread(target=application.run, daemon=True, args=(scope,))
    s2.start()

    scope.start(fig)
    print('Program Exited')
