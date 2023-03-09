# PROBLEM 1: Implement the Various CPU Scheduling Algorithms.
# Done by Guillaume Comfort.
# Scheduling.py is meant to be ran, not this one.

class Scheduling:
    #scheddata = [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
    #schedlen = len(scheddata) 

    def __init__(sched):
        sched.data = []
        sched.len = 0

    def DATA(sched):
        sched.data = []
        sched.len = int(input("Enter the number of processes: ")) # Allows user to input a number for processes
        for i in range(int(sched.len)):
            T = int(input(f"Enter a time for Process {i+1}: ")) # Allows user to set burst time for processes
            sched.data.append(T)

# FCFS
# Control data: [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
# Expected order: ^^^^^^^^^^^^^^^^^^^^^^^^^^
    def FirstCome(sched):
        print("\n")
        Schd = list(sched.data)  # Step 1&2&3&4: Create number of processes, with ID & service time for each process and their processing times.
        ServiceTime = 0.00  
        Totalwait = 0.00 # Step 3: Waiting Time of first process is zero
        TAT = 0.00
        AvgTAT = 0.00

        for i in range(int(sched.len)): # For all values in Scheddata, starting at index 0 in FCFS
            num = int(Schd[i]) # The index value is the process to be completed, all rest are after it in FCFS
            print(f"Starting process {i+1}.")
            while num >= 1: # Until the index value is reduced to 0. Yields expected order with control data.
                print(num)
                num -= 1 
                ServiceTime += 1
            print(f"Process finished, service time required to finish process was: {ServiceTime}") # Step 11: Displaying Waiting time of one process seperate from the rest.
            Totalwait += ServiceTime  # Step 4&5&6&7: Calculating Total time&Totalwait of one process by adding the waiting time of the previously completed process to it.
            print(f"The total time waiting to finish process was: {Totalwait}.\n") # Step 11: Displaying the Waiting time of one process, in relation to all the rest.
            TAT = TAT + (Totalwait - ServiceTime) # Step 8: Turnaround time is calculated by all the total times of each process.
            ServiceTime = 0.00 # Resetting Waiting Time for next process. 
        Avgwait = (Totalwait / sched.len) # Step 9: Calculating Average wait time by dividing total time by the amount of processes.
        AvgTAT = (TAT / sched.len) # Step 10: Calculating Average Turnaround time by dividing the Turnaround time by the amount of processes.

        print(f"\nProcesses Finished. Total Waiting time was: {Totalwait}") # Step 11: Displaying Total waiting time of all processes.
        print(f"Average Wait Time: {Avgwait}") # Step 11: Displaying the Average time of all processes.
        print(f"Turnaround time: {TAT}") # Step 11: Displaying the Turnaround time of all processes.
        print(f"Average turnaround time: {AvgTAT}") # Step 11: Displaying the Average turnaround time of all processes.

#Shortest Job First: 
# Control data: [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
# Expected order: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def SJN(sched): 
        print("\n")
        Schd = list(sched.data) # Step 1&2&3&4: Create number of processes, with ID & service time for each process and their processing times.
        ServiceTime = 0.00 
        Totalwait = 0.00 # Step 3: Waiting Time of first process is zero
        TAT = 0.00

    # Will go throughout the entire list scheddata and if the process is smaller than another one, they will swap places, until the shortest process is at the front.
        for i in range(int(sched.len), 0, -1): 
            for j in range(1, int(sched.len)):
                    while int(Schd[j - 1]) > int(Schd[j]):
                        Schd[j - 1], Schd[j] = Schd[j], Schd[j - 1]
                        #Yields expected order of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] with Control data. Assumed for all cases.
        
        for i in range(int(sched.len)): #For all values in Scheddata, starting at index 0 after swapping list around in first loop
            num = int(Schd[i]) # The index value is the process to be completed, all rest are after it.
            print(f"Starting process {i+1}.")
            while num >= 1: # Until the index value is reduced to 0.
                print(num)
                num -= 1
                ServiceTime += 1
            print(f"Process finished, service time required to finish process was: {ServiceTime}.") # Step 11: Displaying result
            Totalwait += ServiceTime # Step 4&5&6&7: Calculating Total time&Totalwait of one process. Waiting time of one process is the total time of previous process.
            print(f"The total time waiting to finish process was: {Totalwait}.\n") # Step 11: Displaying result
            TAT = TAT + (Totalwait - ServiceTime) # Step 8: Total turnaround time calculated by adding all total time of each process.
            ServiceTime=0.00 # Resetting Waiting Time for next Process
        Avgwait = (Totalwait / sched.len) # Step 9: Calculate average waiting time by dividing the total waiting time by total number of processes.
        AvgTAT = (TAT / sched.len) # Step 10: Calculate average turnaround time by dividing the total waiting time by total number of process.

        print(f"\nProcesses Finished. Total Waiting time was: {Totalwait}.") # Step 11: Displaying result
        print(f"Average Wait Time: {Avgwait}.") # Step 11: Displaying result
        print(f"Turnaround time: {TAT}.") # Step 11: Displaying result
        print(f"Average turnaround time: {AvgTAT}.") # Step 11: Displaying result

# Round Robin Scheduling:
# Control data: [9, 8, 6, 2, 3, 4, 5, 7, 10, 1]
# Not entirely sure about this, but it works and fulfills the steps. 
    def RRB(sched): 
        print("\n")
        Schd = list(sched.data)  # Step 1 and 2: Initializing structure elements and getting the received input from user for burst/etc.
        Schd2 = list(sched.data)
        WaitingTime = [0]
        Totalwait = sum(Schd)
        TAT = [0]
        TTAT = 0
        quantum = 5 # Time Quantum
        Time = 0 # Current time
        while(1):
            done = True
            for i in range(int(sched.len)):
                if int(Schd[i]) > 0: 
                    done = False
                    if int(Schd[i]) > quantum: #Else:
                        Time += quantum
                        Schd[i] = int(Schd[i]) - quantum
                    else: # Step 3: If the time quantum is greater than the burst time.
                        Time = Time + int(Schd[i])
                        WaitingTime.append(Time - int(Schd2[i]))
                        Schd[i] = 0
 
            if done == True: 
                break


        for i in range(int(sched.len)):
            T = int(Schd2[i]) + int(WaitingTime[i])
            TAT.append(T)
            TTAT = TTAT + TAT[i]

        print(f"\nThe total waiting Time for all processes was: {Totalwait}.")
        print(f"The average waiting time was: {Totalwait / sched.len}.") # Step 4&5: Average wait Time
        print(f"The total turnaround time was: {TTAT}") 
        print(f"The average turnaround time was: {TTAT / sched.len}") # Step 4&5


# Priority Scheduling:
# Control data: [5, 3, 7, 9, 6] sched.len = 5 
# Control priority: [1, 6, 3, 9, 4]
# Expected order: [9, 3, 6, 7, 5] -> [9, 6, 4, 3, 1]      
# Expected wait times for each element, total swaps needed: 1+1+3+2 = pseudowait = 7
# 9p9: 9(0+9) ;  3p6: 10(7+3) ; 6p4: 13(7+6) ; 7p3: 14(7+7) ; 5p1: 12(7+5)
# Expected Total wait times for each element.
# 9p9: 9(0+9) ; 3p6: 19(10+9) ; 6p4: 25(19+6) ; etcetc
    def Prio(sched):
        print("\n")
        Schd = list(sched.data) # Step 1&2 Getting the number of processes from user input/burst time/etc
        Prio = []
        priomax = int(input("Enter the maximum priority: "))
        pseudowait = 0.00
        pseudototal = 0.00
        ServiceTime = 0 # Step 3: initially, wait time and totalwait is 0 for first element
        Totalwait = 0.00
        TAT = 0.00

        for i in range(int(sched.len)): # Step 1&2: Getting the priority of processes from user input.
            T = int(input(f"Enter priority for process {i+1}: "))
            Prio.append(T)
            if priomax < int(T):
                priomax = int(T)

        print("\n")
        print(f"Processes: {Schd}") # Step 9: Displaying the result.
        print(f"Priority: {Prio}") # Step 9: Displaying the result.
        print(f"Max Priority: {priomax}\n") # Step 9: Displaying the result.

        for i in range(int(sched.len)):
            for j in range(1, int(len(Prio))):
                while int(Prio[j - 1]) < int(Prio[j]):  # Arranging processes in order of priority, until highest priorities and it's elements are at top.
                    Prio[j-1], Prio[j] = Prio[j], Prio[j-1]
                    Schd[j-1], Schd[j] = Schd[j], Schd[j-1]
                    # Yields expected order of [9, 3, 6, 7, 5] -> [9, 6, 4, 3, 1] with Control data. Assumed for all cases.
                    pseudowait += 1 #Step 4: all other elements total wait will be pseudototal and wait time pseudowait.
                    pseudototal += 1 #Step 5: TWT is calculated by adding the waiting time for lack processes.

        print(f"Sorted processes: {Schd}") # Step 9: Displaying the result.
        print(f"Sorted priority: {Prio}\n") # Step 9: Displaying the result.
        
        for i in range(int(sched.len)):
            num = int(Schd[i])
            print(f"Starting process {i+1}.")
            while num >= 1:
                print(num)
                num -= 1
                Totalwait += 1 # Step 5: TWT is calculated by adding the waiting time for lack processes.
                ServiceTime += 1 
                pseudototal += 1
            print(f"Process finished, service time required to finish process was: {ServiceTime}.") # Step 9: Displaying the result.
            print(f"The total time waiting to finish process was: {Totalwait}.\n") # Step 9: Displaying the result.
            ServiceTime = pseudowait # Step 4: all other elements total wait will be pseudototal and wait time pseudowait.
            # This yields expected wait time for each element individually, taking into account i[0] = Waitingtime = t0 = burst
            Totalwait = pseudototal # Step 4&5: all other elements total wait will be pseudototal and wait time pseudowait. Totalwait is calculated by adding waiting time for lack processes
            # This yields expected Total wait time for all elements
            TAT = TAT + (Totalwait - ServiceTime) #Step 5: Turnaround is calculated by adding all total times of processes.
        Avgwait = (Totalwait / sched.len) # Step 7: Average wait time is calculated by dividing total with number of processes.
        AvgTAT = (TAT / sched.len) # Step 8: Average turnaround time is calculated by dividing Turnaround with number of processes.

        print(f"\nProcesses Finished. Total Waiting time was: {Totalwait}.") # Step 9: Displaying the result.
        print(f"Average Wait Time: {Avgwait}.") # Step 9: Displaying the result.
        print(f"Turnaround time: {TAT}.") # Step 9: Displaying the result.
        print(f"Average turnaround time: {AvgTAT}.") # Step 9: Displaying the result.