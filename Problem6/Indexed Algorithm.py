# Step 1: Start
import time

# Step 2: Let n be the size of the buffer
n = 5
buffer = []

# Step 3: Check if there are any producers
producers = True

# Step 7: Check if there are any consumers
consumers = True

# Step 10: Repeat checking for producers and consumers until required
while producers or consumers:
    # Step 4: If there are producers, check whether the buffer is full
    if producers and len(buffer) == n:
        print("Buffer is full. Producer has to wait.")
        time.sleep(1)
    # Step 5: If the buffer is not full, store the producer item in the buffer
    elif producers:
        item = input("Enter the producer item: ")
        buffer.append(item)
        print(f"Producer stored item '{item}' in buffer.")
        time.sleep(1)
    
    # Step 8: If there are consumers, check whether the buffer is empty
    if consumers and len(buffer) == 0:
        print("Buffer is empty. Consumer has to wait.")
        time.sleep(1)
    # Step 9: If the buffer is not empty, consume the item from the buffer
    elif consumers:
        item = buffer.pop(0)
        print(f"Consumer consumed item '{item}' from buffer.")
        time.sleep(1)
    
    # Step 3 and 7: Check if there are any producers or consumers left
    producers = input("Are there any more producers? (Y/N): ").lower() == "y"
    consumers = input("Are there any more consumers? (Y/N): ").lower() == "y"

# Step 11: Terminate the process
print("All producers and consumers have finished.")
