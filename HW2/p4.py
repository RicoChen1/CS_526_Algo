class Node:
    def __init__(self, val):
        self.val = val      # current node
        self.next = None    # chain next node
        self.prev = None    # chain previous node(Double Linked)

def sum_3_middle(head):
    # find list length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # middle index
    mid = length // 2  # 3 for 7 nodes
    
    # Move to middle node, Sum 3 middle nodes
    current = head
    for _ in range(mid):
        current = current.next
    total = current.prev.val + current.val + current.next.val
    return total

# list: 2<->4<->8<->10<->15<->29<->41
def create_double_linked_list(values):

    head = Node(values[0])
    current = head          # assign init node
    
    for i in range(1, len(values)):
        new_node = Node(values[i])
        current.next = new_node
        new_node.prev = current
        current = new_node
    
    return head

# Test
values = [2, 4, 8, 10, 15, 29, 41]
head = create_double_linked_list(values)
result = sum_3_middle(head)
print(result)