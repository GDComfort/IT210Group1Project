# PROBLEM 1: Implement the Various CPU Scheduling Algorithms.
# Done by Guillaume Comfort.
# Scheduling.py is meant to be ran, not this one.

class Scheduling:
 #scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
    #schedlen = len(scheddata) 

    def __init__(self):
        scheddata = []
        schednum = len(scheddata)

# FCFS
    def FirstCome():
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        schedlen = len(scheddata)
        WaitingTime = 0.00
        Totalwait = 0.00
        AvgWait = 0.00
        TAT = 0.00

        for i in range(schedlen):
            num = scheddata[i]
            while num >= 1:
                print(num)
                num -= 1
                Totalwait += 1
                WaitingTime += 1
            print("Process finished, waiting time was:"+str(WaitingTime))
            WaitingTime = 0.00
        Avgwait = (Totalwait / schedlen)
        print("Processes Finished. Total Waiting time was:"+str(Totalwait))
        print("Average Wait Time:"+str(Avgwait))

#Shortest Job First: 

    def SJN():

        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        schedwait = [0, 3, 5, 8, 11, 14, 15, 18, 19, 22]
        schedlen = len(scheddata)
        WaitingTime = 0.00
        Totalwait = 0.00
        AvgWait = 0.00
        TAT = 0.00


        for i in range(schedlen):
            wait = schedwait[i]
            num = scheddata[i]
            if schedwait[i+1] <= 0 and scheddata[i+1] < scheddata[i]:
                scheddata[i], scheddata[i+1] = scheddata[i+1], scheddata[i]     
                while num >= 1:
                    print(num)
                    num -= 1
                    Totalwait += 1
                    WaitingTime += 1
                    schedwait = [x - 1 for x in schedwait]
                print("Process finished, waiting time was:"+str(WaitingTime))
                WaitingTime = 0.00
        
            else:
                while num >= 1:
                    print(num)
                    num -= 1
                    Totalwait += 1
                    WaitingTime += 1
                    schedwait = [x - 1 for x in schedwait]
                print("Process finished, waiting time was:"+str(WaitingTime))
                WaitingTime = 0.00
        Avgwait = (Totalwait / schedlen)
        print("Processes Finished. Total Waiting time was:"+str(Totalwait))
        print("Average Wait Time:"+str(Avgwait))
