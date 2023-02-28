# PROBLEM 1: Implement the Various CPU Scheduling Algorithms.
#Done by Guillaume Comfort.

class Scheduling:
    #scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
    #schednum = len(scheddata) 

# FCFS
    def FirstCome():
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        schednum = len(scheddata)
        WaitingTime = 0.00
        Totalwait = 0.00
        AvgWait = 0.00
        TAT = 0.00

        for i in range(schednum):
            num = scheddata[i]
            while num >= 0:
                print(num)
                num -= 1
                Totalwait += 1
                WaitingTime += 1
            print("Waiting Time:"+str(WaitingTime - 1))
            WaitingTime = 0.00
        Avgwait = (Totalwait / schednum)
        print("Total Wait Time:"+str(Totalwait - schednum))
        print("Average Wait Time:"+str(Avgwait))

        
