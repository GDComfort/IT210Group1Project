# Step 1: Start the program.
# Step 2: Get the number of memory partition and their sizes.
num_partitions = int(input("Enter the number of memory partitions: "))
partition_sizes = []
for i in range(num_partitions):
    partition_size = int(input(f"Enter the size of partition {i+1}: "))
    partition_sizes.append(partition_size)

# Step 3: Get the number of processes and values of block size for each process.
num_processes = int(input("Enter the number of processes: "))
processes = []
for i in range(num_processes):
    process_name = input(f"Enter the name of process {i+1}: ")
    process_size = int(input(f"Enter the size of process {i+1} (in bytes): "))
    processes.append((process_name, process_size))

# Step 4: First fit algorithm searches all the entire memory block until a hole which is big enough is encountered. It allocates that memory block for the requesting process.
def first_fit():
    allocation = [-1] * num_processes
    for i in range(num_processes):
        for j in range(num_partitions):
            if partition_sizes[j] >= processes[i][1]:
                partition_sizes[j] -= processes[i][1]
                allocation[i] = j
                break
    return allocation

# Step 5: Best-fit algorithm searches the memory blocks for the smallest hole which can be allocated to requesting process and allocates if.
def best_fit():
    allocation = [-1] * num_processes
    for i in range(num_processes):
        best_partition = -1
        for j in range(num_partitions):
            if partition_sizes[j] >= processes[i][1]:
                if best_partition == -1 or partition_sizes[j] < partition_sizes[best_partition]:
                    best_partition = j
        if best_partition != -1:
            partition_sizes[best_partition] -= processes[i][1]
            allocation[i] = best_partition
    return allocation

# Step 6: Worst fit algorithm searches the memory blocks for the largest hole and allocates it to the process.
def worst_fit():
    allocation = [-1] * num_processes
    for i in range(num_processes):
        worst_partition = -1
        for j in range(num_partitions):
            if partition_sizes[j] >= processes[i][1]:
                if worst_partition == -1 or partition_sizes[j] > partition_sizes[worst_partition]:
                    worst_partition = j
        if worst_partition != -1:
            partition_sizes[worst_partition] -= processes[i][1]
            allocation[i] = worst_partition
    return allocation

# Step 7: Analyses all the three memory management techniques and display the best algorithm which utilizes the memory resources effectively and efficiently.
print("Choose a memory allocation algorithm:")
print("1. First fit")
print("2. Best fit")
print("3. Worst fit")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    allocation = first_fit()
elif choice == 2:
    allocation = best_fit()
elif choice == 3:
    allocation = worst_fit()
else:
    print("Invalid choice")
    exit()

# Step 8: Stop the program.
print("Memory allocation:")
for i in range(num_processes):
    print(f"{processes[i][0]}: {allocation[i]+1}")  # +1 because partitions are numbered from 1
