class ListNode:
    def __init__(self,value):
        # pass
        self.value = value
        self.next = None

def doIt(node):
    if node is None:    # End!
        return
                        # Continue
    doIt(node.next)     # first to next node
    print(node.value)  # then print value @ current node

# Create linked list 12 - 3 - 5 - 2
head = ListNode(12)
head.next = ListNode(3)
head.next.next = ListNode(5)
head.next.next.next = ListNode(2)

print("linked list seq：12 -> 3 -> 5 -> 2")
print("doIt fn output：")
doIt(head)