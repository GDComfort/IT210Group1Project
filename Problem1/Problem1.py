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
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]  # Step 1&2&3&4: Create number of processes, with ID & service time for each process and their processing times.
        schedlen = len(scheddata)
        WaitingTime = 0.00  # Step 3: Waiting Time of first process is zero
        Totalwait = 0.00
        TAT = 0.00
        AvgTAT = 0.00

        for i in range(schedlen): # For all values in Scheddata, starting at index 0 in FCFS
            num = scheddata[i] # The index value is the process to be completed, all rest are after it in FCFS
            print("Starting process "+str(i+1)+".")
            while num >= 1: # Until the index value is reduced to 0.
                print(num)
                num -= 1 
                Totalwait += 1   # Step 4&5&6&7: Calculating Total time&Totalwait of one process. Waiting time of one process total time of previous
                WaitingTime += 1
            print("Process finished, waiting time to finish process was:"+str(WaitingTime)) # Step 11: Displaying Waiting time of one process seperate from the rest.
            print("The total time waiting to finish process was:"+str(Totalwait)+"\n") # Step 11: Displaying the Waiting time of one process, in relation to all the rest.
            TAT = TAT + (Totalwait - WaitingTime) # Step 8: Turnaround time is calculated by all the total times of each process.
            WaitingTime = 0.00 # Resetting Waiting Time for next process. 
        Avgwait = (Totalwait / schedlen) # Step 9: Calculating Average wait time by dividing total time by the amount of processes.
        AvgTAT = (TAT / schedlen) # Step 10: Calculating Average Turnaround time by dividing the Turnaround time by the amount of processes.
        print("\nProcesses Finished. Total Waiting time was:"+str(Totalwait)) # Step 11: Displaying Total waiting time of all processes.
        print("Average Wait Time:"+str(Avgwait)) # Step 11: Displaying the Average time of all processes.
        print("Turnaround time:"+str(TAT)) # Step 11: Displaying the Turnaround time of all processes.
        print("Average turnaround time:"+str(AvgTAT)) # Step 11: Displaying the Average turnaround time of all processes.

#Shortest Job First: 
    def SJN():
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1] # Step 1&2&3&4: Create number of processes, with ID & service time for each process and their processing times.
        Schd = list(scheddata)
        schedlen = len(scheddata)
        WaitingTime = 0.00 # Step 3: Waiting Time of first process is zero.
        Totalwait = 0.00
        Turnaround = 0.00

        
    # Will go throughout the entire list scheddata and if the process is smaller than another one, they will swap places, until the shortest process is at the front.
        for i in range(schedlen, 0, -1): 
            for j in range(1, schedlen):
                    if Schd[j - 1] > Schd[j]:
                        Schd[j - 1], Schd[j] = Schd[j], Schd[j - 1]
        
        for i in range(schedlen): #For all values in Scheddata, starting at index 0 after swapping list around in first loop
            num = Schd[i] # The index value is the process to be completed, all rest are after it.
            print("Starting process "+str(i+1)+".")
            while num >= 1: # Until the index value is reduced to 0.
                print(num)
                num -= 1
                Totalwait += 1 # Step 4&5&6&7: Calculating Total time&Totalwait of one process. Waiting time of one process is the total time of previous process.
                WaitingTime += 1
            print("Process finished, waiting time was:"+str(WaitingTime)) # Step 11: Displaying result
            print("The total time waiting to finish process was:"+str(Totalwait)+"\n") # Step 11: Displaying result
            Turnaround = Turnaround + (Totalwait - WaitingTime) # Step 8: Total turnaround time calculated by adding all total time of each process.
            WaitingTime=0.00 # Resetting Waiting Time for next Process
        Avgwait = (Totalwait / schedlen) # Step 9: Calculate average waiting time by dividing the total waiting time by total number of processes.
        AvgTAT = (Turnaround / schedlen) # Step 10: Calculate average turnaround time by dividing the total waiting time by total number of process.
        print("\nProcesses Finished. Total Waiting time was:"+str(Totalwait)) # Step 11: Displaying result
        print("Average Wait Time:"+str(Avgwait)) # Step 11: Displaying result
        print("Turnaround time:"+str(Turnaround)) # Step 11: Displaying result
        print("Average turnaround time:"+str(AvgTAT)) # Step 11: Displaying result

#Round Robin Scheduling:
    def RRB():
        scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
        Schd = list(scheddata)
        schedlen = len(scheddata)
        WaitingTime = [0, 0]
        WT = list(WaitingTime)
        Totalwait = [0]
        Turnaround = [0]
        roundcounter = 0
    
        while len(Schd) and len(WT) and max(Schd) >= 0:
            print("Round "+str(roundcounter+1)+" starting.")
            for i in range(0, schedlen, 1):
                num = Schd[i]
                print(str(num)+" - 1 = "+str(num-1))
                Schd[i] -= 1
                Totalwait = [x + 1 for x in Totalwait]
                WaitingTime = [x + 1 for x in WaitingTime]
            roundcounter += 1
            #Turnaround = [x + (Totalwait[0] - WaitingTime[1]) for x in Turnaround]
            if 0 in Schd:
                print("One process was finished. The total waiting time for that process was "+str(WaitingTime[0]))
                Schd.remove(0)
                WaitingTime[1] == 0
                schedlen = len(Schd)
            print("Round "+str(roundcounter)+" done.\n")
        TW = [x / 10 for x in Totalwait]
        print("No more processes. "+str(roundcounter)+" processes were finished. Total waiting time was:"+str(Totalwait))
        print("Average waiting time was:"+str(TW))
        #print("The turnaround time was:"+str(Turnaround))

'''
    def RRB():
        
'''



    
