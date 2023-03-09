<h1>Problem 1 for the Group Project for IT210.</h1>
<br>Done by Guillaume Comfort, using Python

Objective: To implement the following CPU scheduling algorithm using any programming language
1. First Come First Serve, - DONE (?)
2. Shortest Job First, - DONE (?)
3. Round Robin Scheduling, - DONE (?)
4. Priority Scheduling, - DONE (?)

**FIRST COME FIRST SERVE**: CPU scheduler will decide which process should be given the CPU for
its execution. For this CPU uses different algorithm to choose among the process. One among that algorithm
is FCFS algorithm. In this algorithm the process which arrives first is given the CPU after finishing its
request only it will allow CPU to execute other process.

ALGORITHM:

- Step1: Create the number of processes.
- Step2: Get the ID and Service time for each process.
- Step3: Initially, waiting time of first process is zero and Total time for the first process is the starting time of that process.
- Step4: Calculate the Total time and Processing time for the remaining processes.
- Step5: Waiting time of one process is the Total time of the previous process.
- Step6: Total time of process is calculated by adding Waiting time and Service time.
- Step7: Total waiting time is calculated by adding the waiting time for lack process.
- Step8: Total turnaround time is calculated by adding all total time of each process.
- Step9: Calculate Average waiting time by dividing the total waiting time by total number of processes.
- Step10: Calculate Average turnaround time by dividing the total time by the number of processes.
- Step11: Display the result.


**SHORTEST JOB FIRST**: CPU scheduler will decide which process should be given the CPU for its
execution. For this CPU use different algorithm to choose among the process. One among that algorithm is
SJF algorithm. In this algorithm the process which has less service time given the CPU after finishing its
request only it will allow CPU to execute next other process.

ALGORITHM:
- Step1: Get the number of processes.
- Step2: Get the id and service time for each process.
- Step3: Initially the waiting time of first short process as 0 and total time of first short is process the service time of that process.
- Step4: Calculate the total time and waiting time of remaining process.
- Step5: Waiting time of one process is the total time of the previous process.
- Step6: Total time of process is calculated by adding the waiting time and service time of each process.
- Step7: Total waiting time calculated by adding the waiting time of each process.
- Step8: Total turnaround time calculated by adding all total time of each process.
- Step9: Calculate average waiting time by dividing the total waiting time by total number of processes.
- Step10: Calculate average turnaround time by dividing the total waiting time by total number of process.
- Step11: Display the result.


**ROUND ROBIN**: CPU scheduler will decide which process should be given the CPU for its execution.
For this it use different algorithm to choose among the process .one among that algorithm is Round robin
algorithm. In this algorithm we are assigning some time slice .The process is allocated according to the time slice ,if
the process service time is less than the time slice then process itself will release the CPU voluntarily .The
scheduler will then proceed to the next process in the ready queue .If the CPU burst of the currently running
process is longer than time quantum ,the timer will go off and will cause an interrupt to the operating system
.A context switch will be executed and the process will be put at the tail of the ready queue.

ALGORITHM:
- Step 1: Initialize all the structure elements.
- Step 2: Receive inputs from the user to fill process id, burst time and arrival time.
- Step 3: Calculate the waiting time for all the process id.
- The waiting time for first instance of a process is calculated as:
- a[i].waittime=count + a[i].arrivt
- The waiting time for the rest of the instances of the process is calculated as:
- If the time quantum is greater than the remaining burst time then waiting time is calculated as:
- a[i].waittime=count + tq
- Else if the time quantum is greater than the remaining burst time then waiting time is calculated as:
- a[i].waittime=count - remaining burst time
- Step 4: Calculate the average waiting time and average turnaround time.
- Step 5: Print the results of the step 4


**PRIORITY SCHEDULING**: CPU scheduler will decide which process should be given the CPU for its
execution. For this it use different algorithm to choose among the process. One among that algorithm is
Priority Scheduling algorithm. In this algorithm the process which has highest priority executed first. After
finishing its request only, it will allow CPU to execute next process which has next priority level.

ALGORITHM:
- Step1: Get the number of process, burst time and priority.
- Step2: Using for loop i=0 to n-1 do step 1 to 6.
- Step3: If i=0,wait time=0,T[0]=b[0];
- Step4: T[i]=T[i-1]+b[i] and wt[i]=T[i]-b[i].
- Step5: Total waiting time is calculated by adding the waiting time for lack process.
- Step6: Total turnaround time is calculated by adding all total time of each process.
- Step7: Calculate Average waiting time by dividing the total waiting time by total number of processes.
- Step8: Calculate Average turnaround time by dividing the total time by the number of process.
- Step9: Display the result. 
