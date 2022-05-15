import time
import serial
import numpy as np

class Main():
    cmp_data = []

    def __init__(self):
        print("initiated")
       
    def run(self):
    

        with serial.Serial('COM4', 115200, timeout=1) as ser:    
            print("Found serial port com1")
            attempt = 0
            while 1:
                if attempt == 3: break
                fileIndex = input("Enter data save index (1-5) To initiate compair mode press 6:")
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
                        if i == 300: break
                    time.sleep(0.01)
                attempt = attempt + 1

            compare_files = input("Data has been succesfuly saved!! Input file to compare comma separated way:")
            compare_files = compare_files.split(",")
            for f in compare_files:
                filename = "data.{findex}.txt".format(findex = f)
                with open(filename) as rf:
                    data = rf.read()
                    data = data.split('\n')
                    new_data = []
                    for d in data:
                        try:
                            d = int(d)
                            new_data.append(d)
                        except:
                            new_data.append(0)
                    self.cmp_data.append(new_data)
                    rf.close()
            new_cmp_data = []
            for d in self.cmp_data:
                new_cmp_data.append(d[:200])
            new_cmp_data = np.diff(new_cmp_data)
            cmp = np.diff(new_cmp_data, axis=0)
            print(cmp)

if __name__ == "__main__":
        application = Main()
        application.run()
