#04/13/23
#Khadija Abdi 144359
#Procedure I: Simply detects the existence of a Cycle:

def find(vertex, graph):
    visited = set()
    stack = [vertex]
    while stack:
        current = stack.pop()
        visited.add(current)
        neighbors = graph[current]
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
            else:
                #if a cycle is found
                return True
    # if there is no cycle found
    return False

graph = {
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: [1]
}

# it starts exploring at vertex 1
has_cycle = find(1, graph)

if has_cycle:
    print("a cycle is found")
else:
    print("there is no cycle found.")



#Procedure II
def detect_deadlock(allocation, maximum, available):
    num_processes = len(allocation)
    num_resources = len(available)

    # find the need matrix
    need = [[maximum[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # creating the work and finsish arrays
    work = available[:]
    finish = [False] * num_processes

    # if when the need of process p is less than or equal to work
    while True:
        p = None
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                p = i
                break

        if p is None:
            # deadlock detected there is no pocess in the iteration
            deadlock_processes = set(i for i in range(num_processes) if not finish[i])
            print("System is in deadlock and deadlock process are: ", deadlock_processes)
            return deadlock_processes
        else:
            # mark it as finsihed and release the recources
            for j in range(num_resources):
                work[j] += allocation[p][j]
            finish[p] = True

        if all(finish):
            # no deadlock found
            print("there is no deadlock ")
            return set()

def max_matrix():
    print("Enter the max matrix: ")
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))

    # Initialize matrix
    max_matrix = []
    print("Enter the entries ROW-wise:")

    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
             a.append(int(input()))
        max_matrix.append(a)

    # For printing the matrix
    for i in range(R):
        for j in range(C):
            print(max_matrix[i][j], end = " ")
        print()
    return max_matrix
def allocation_matrix():
    print("Enter the allocation matrix: ")
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))

    # Initialize matrix
    allocation_matrix = []
    print("Enter the entries ROW-wise: ")

    # For user input
    for i in range(R):          # A for loop for row entries
        a =[]
        for j in range(C):      # A for loop for column entries
             a.append(int(input()))
        allocation_matrix.append(a)

    # For printing the matrix
    for i in range(R):
        for j in range(C):
            print(allocation_matrix[i][j], end = " ")
        print()
    return allocation_matrix

maximum = max_matrix()
allocation = allocation_matrix()
available = [1,2,0]

detect_deadlock(allocation, maximum, available)
