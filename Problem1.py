# PROBLEM 1: Implement the Various CPU Scheduling Algorithms.
#Done by Guillaume Comfort.

class Scheduling:
    #self.data = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1] Data Set
    #self.num = 10 Number of processes to complete.

# FCFS
    def FirstCome():
        selfdata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        WaitingTime = 0.00
        Totalwait = 0.00
        AvgWait = 0.00
        TAT = 0.00

        for i in range(len(selfdata)):
            num = selfdata[i]
            while num >= 0:
                print(num)
                num -= 1
                Totalwait += 1
                WaitingTime += 1
            print(WaitingTime - 1)
            WaitingTime = 0.00
        print(Totalwait - len(selfdata))

    FirstCome()