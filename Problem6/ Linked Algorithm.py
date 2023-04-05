# Step 1: Create a queue to hold all pages in memory
queue = []

# Step 2: When the page is required replace the page at the head of the queue
# Step 3: Now the new page is inserted at the tail of the queue
while True:
    page = input("Enter the page required: ")
    if page in queue:
        queue.remove(page)
    queue.append(page)
    print("Queue:", queue)

    # Step 4: Create a stack
    stack = list(reversed(queue))

    # Step 5: When the page fault occurs replace page present at the bottom of the stack
    if len(stack) > 5:
        stack.pop()

    # Step 6: Stop the allocation
    if page == "stop":
        break

    print("Stack:", stack)
