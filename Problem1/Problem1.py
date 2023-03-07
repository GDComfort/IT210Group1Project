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
        Schd = list(scheddata)
        schedlen = len(scheddata)
        WaitingTime = 0.00
        Totalwait = 0.00
        Turnaround = 0.00
        schedwaithusfar = 0.00

        for i in range(schedlen, 0, -1):
            for j in range(1, schedlen):
                if Schd[j - 1] > Schd[j]:
                    Schd[j - 1], Schd[j] = Schd[j], Schd[j - 1]
        
        for i in range(schedlen):
            num = Schd[i]
            while num >= 1:
                print(num)
                num -= 1
                Totalwait += 1
                WaitingTime += 1
            print("Process finished, waiting time was:"+str(WaitingTime))
            Turnaround = Turnaround + (Totalwait - WaitingTime)
            WaitingTime=0.00
        Avgwait = (Totalwait / schedlen)
        print("Processes Finished. Total Waiting time was:"+str(Totalwait))
        print("Average Wait Time:"+str(Avgwait))   
        print("Turnaround time:"+str(Turnaround))

#Round Robin Scheduling:
    def RRB():
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        Schd = list(scheddata)
        schedlen = len(scheddata)
        WaitingTime = [0]
        Totalwait = [0]
        Turnaround = [0]
        schedwaithusfar = 0.00
        roundcounter = 0
    
        while len(Schd) and max(Schd) >= 0:
            for i in range(0, schedlen, 1):
                num = Schd[i]
                print(num)
                Schd[i] -= 1
                Totalwait = [x + 1 for x in Totalwait]
                WaitingTime = [x + 1 for x in WaitingTime]
            roundcounter += 1
            if 0 in Schd:
                print("Process Finished. waiting time was "+str(WaitingTime))
                Schd.remove(0)
                schedlen = len(Schd)
            print("Round "+str(roundcounter)+" done.")
            print("Round "+str(roundcounter+1)+" starting.")
        TW = [x / 10 for x in Totalwait]
        print("Aborting round "+str(roundcounter+1)+", processes finished. Total waiting time was:"+str(Totalwait))
        print("Average waiting time was:"+str(TW))
                    

            


