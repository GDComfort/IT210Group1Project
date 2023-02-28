#Importing from Problem1.py for the defined functions
from Problem1 import Scheduling

print("Which Scheduling Algorithm would you like to call?")
print("A. First Come First Serve")
#Rest not available, will add them here eventually
choice = input("Enter choice here (Capitalization matters.): ")

if choice == 'A':
    Scheduling.FirstCome()
else:
    print("Not an available choice.")
