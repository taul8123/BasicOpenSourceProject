import threading


class calculator :
    max = 0
    result = 0

    def __init__(self,max):
        self.result = 0
        self.max = max

    def total(self):
        for i in range(self.max):
            self.result += i+1
        print("1+2+3+...+%d= %d" % (self.max, self.result))



cal1 = calculator(1000)
cal2 = calculator(100000)
cal3 = calculator(10000000)

th1 = threading.Thread(target = cal1.total)
th2 = threading.Thread(target = cal2.total)
th3 = threading.Thread(target = cal3.total)

th1.start()
th2.start()
th3.start()