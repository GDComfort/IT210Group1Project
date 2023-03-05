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
        TAT = 0.00

        for i in range(schedlen):
            num = scheddata[i]
            while num >= 1:
                print(num)
                num -= 1
                Totalwait += 1
                WaitingTime += 1
            print("Process finished, waiting time was:"+str(WaitingTime))
            TAT = TAT + (Totalwait - WaitingTime)
            WaitingTime = 0.00
        Avgwait = (Totalwait / schedlen)
        print("Processes Finished. Total Waiting time was:"+str(Totalwait))
        print("Average Wait Time:"+str(Avgwait))
        print("Turnaround time:"+str(TAT))

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

'''
Possibly another form of SJN? Unsure, Idk if it does what I want.
        for i in range(int(schedlen), 0, -1):
            for j in range(1, int(schedlen)):
                if Schd[j - 1] > Schd[j]:
                    tempo = Schd[j - 1]
                    Schd[j - 1] = Schd[j]
                    Schd[j] = tempo

        for i in range(1, int(schedlen)):
            tempo = int(Schd[i - 1]) + int(WaitingTime[i-1])
            WaitingTime.append(tempo)

        for i in range(0, int(schedlen)):
            Totalwait = Totalwait + WaitingTime[i]
            Avgwait = Totalwait / int(schedlen)
            Turnaround = WaitingTime[i] + int(Schd[i])
        
        print("Processes Finished. Total Waiting time was:"+str(Totalwait))
        print("The average wait time was:"+str(Avgwait))
        print("The turnaround time was:"+str(Turnaround))
'''



    
