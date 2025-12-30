# Pattern 1: Reverse entire list
prev, curr = None, head
while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

# Pattern 2: Reverse first k nodes
prev, curr = None, head
for _ in range(k):
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

# Pattern 3: Reverse between two nodes
prev, curr = stop_node, start_node
while curr != stop_node:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
