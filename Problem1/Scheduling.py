#Importing from Problem1.py for the defined functions
from Problem1 import Scheduling

class Scheduler:
    def __init__(sched):
        sched.Scheduling = Scheduling()

    def run(sched):
        while True:
            print("\nWhich Scheduling Algorithm would you like to call?\n")
            print("1: First Come First Serve.")
            print("2: Shortest Job Next.")
            print("3: Round Robin Scheduling.")
            print("4: Priority Scheduling.")
            print("5: Exit. \n")
            choice = int(input("Enter choice here: "))

            if choice == 1:
                print("\n")
                sched.Scheduling.DATA()
                sched.Scheduling.FirstCome()
            elif choice == 2:
                print("\n")
                sched.Scheduling.DATA()
                sched.Scheduling.SJN()
            elif choice == 3:
                print("\n")
                sched.Scheduling.DATA()
                sched.Scheduling.RRB()
            elif choice == 4:
                print("\n")
                sched.Scheduling.DATA()
                sched.Scheduling.Prio()
            elif choice == 5:
                break
            else:
                print("\nNot an available choice.")
                break

Scheduler().run()
