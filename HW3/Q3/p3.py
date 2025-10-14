"""

function reverse(stack):
    if stack is empty:
        return
    temp = pop(stack)        // 移除顶部元素
    reverse(stack)           // 反转剩余栈,递归
    insertAtBottom(stack, temp)  // 将元素插入到底部(也是递归)

其中 insertAtBottom 也是递归的：
function insertAtBottom(stack, item):
    if stack is empty:
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)

Idea Source: csdn
"""

# pscode:
"""ARRAY STACK"""
"""
# 假设栈用数组实现，有top指针指向栈顶
# function reverseArrayStack(stack, top):
#     if top < 0:  // 栈空
#         return
    
#     保存当前栈顶元素
#     temp = stack[top]
#     top = top - 1  // pop操作
    
#     递归反转剩余栈
#     reverseArrayStack(stack, top)
    
#     元素插入到底部
#     insertAtBottomArray(stack, top, temp)

# function insertAtBottomArray(stack, top, item):
#     if top < 0:  栈空!
#         top = top + 1
#         stack[top] = item
#     else:
#         temp = stack[top]
#         top = top - 1
#         insertAtBottomArray(stack, top, item)
#         top = top + 1
#         stack[top] = temp

# class Node:
#     data
#     next

# function reverseLinkedListStack(top):
#     if top == null:
#         return null
    
#     保存当前节点
#     current = top
#     top = top.next
#     current.next = null
    
#     递归反转剩余栈
#     top = reverseLinkedListStack(top)
    
#     将原栈顶插入到底部
#     return insertAtBottomLinkedList(top, current)

# function insertAtBottomLinkedList(top, node):
#     if top == null:
#         return node
#     else:
#         temp = top
#         top = top.next
#         temp.next = null
        
#         newTop = insertAtBottomLinkedList(top, node)
#         重新连接
#         node = newTop
#         while node.next != null:
#             node = node.next
#         node.next = temp
#         return newTop
"""

def reverse_array_stack(stack):
    """
    Reverse a stack implemented as array using recursion
    Input: stack as list (top at the end)
    Output: reversed stack
    """
    # Base case: if stack is empty, return
    if not stack:
        return stack
    
    # Remove top element
    top_element = stack.pop()
    
    # Reverse remaining stack
    reverse_array_stack(stack)
    
    # Insert element at bottom
    insert_at_bottom_array(stack, top_element)
    
    return stack

def insert_at_bottom_array(stack, item):
    """
    Insert an element at the bottom of array stack using recursion
    """
    # If stack empty, just append item
    if not stack:
        stack.append(item)
        return
    
    # Remove top element temporarily
    top = stack.pop()
    
    # Recursively insert at bottom
    insert_at_bottom_array(stack, item)
    
    # Put the top element back
    stack.append(top)


class ListNode:
    """Node for singly linked list"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list_stack(head):
    """
    Reverse a stack implemented as singly linked list using recursion
    Input: head of the linked list (top of stack)
    Output: new head of reversed linked list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the stack
    new_head = reverse_linked_list_stack(head.next)
    
    # Make the next node point to current node
    head.next.next = head
    head.next = None
    
    return new_head

# Alternative approach for linked list stack (more explicit stack operations)
def reverse_linked_list_stack_alt(head):
    """
    Alternative approach: explicit stack reversal using two recursive functions
    """
    if not head:
        return None
    
    # Remove top element
    current = head
    rest = head.next
    current.next = None
    
    # Reverse the rest
    reversed_rest = reverse_linked_list_stack_alt(rest)
    
    # Insert current node at bottom
    return insert_at_bottom_linked_list(reversed_rest, current)

def insert_at_bottom_linked_list(head, node):
    """
    Insert node at bottom of linked list stack
    """
    if not head:
        return node
    
    # Recursively insert at bottom of rest
    head.next = insert_at_bottom_linked_list(head.next, node)
    return head


class DoublyListNode:
    """Node for doubly linked list"""
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def reverse_doubly_linked_list_stack(head):
    """
    Reverse a stack implemented as doubly linked list using recursion
    Input: head of doubly linked list (top of stack)
    Output: new head of reversed list
    """
    # Base case: empty list
    if not head:
        return None
    
    # Save current node and disconnect it
    current = head
    rest = head.next
    
    # Disconnect current node
    if rest:
        rest.prev = None
    current.next = None
    current.prev = None
    
    # Recursively reverse the rest
    reversed_rest = reverse_doubly_linked_list_stack(rest)
    
    # Insert current node at bottom of reversed rest
    return insert_at_bottom_doubly_linked_list(reversed_rest, current)

def insert_at_bottom_doubly_linked_list(head, node):
    """
    Insert node at bottom of doubly linked list stack
    Maintains both next and prev pointers
    """
    if not head:
        return node
    
    # Find the last node in the list
    last = head
    while last.next:
        last = last.next
    
    # Insert node after last node
    last.next = node
    node.prev = last
    node.next = None
    
    return head


# AI Assisted more efficient version for doubly linked list
def reverse_doubly_linked_list_stack_efficient(head):
    """
    More efficient recursive reversal for doubly linked list
    Uses single recursive function
    """
    if not head:
        return None
    
    # Recursively reverse the rest
    new_head = reverse_doubly_linked_list_stack_efficient(head.next)
    
    if not new_head:
        # This is the last node, make it the new head
        head.next = None
        head.prev = None
        return head
    
    # Find the last node in the reversed list
    last = new_head
    while last.next:
        last = last.next
    
    # Attach current node to the end
    last.next = head
    head.prev = last
    head.next = None
    
    return new_head








"""--- AI Generated Tesing Code ---"""
def test_all_reversals():
    """Test all three stack reversal implementations"""
    
    # Test data
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Input: {test_data}")
    
    # 1. Test array stack reversal
    array_stack = test_data.copy()
    reversed_array = reverse_array_stack(array_stack)
    print(f"Array stack reversed: {reversed_array}")
    
    # 2. Test linked list stack reversal
    # Create linked list from test data
    head = None
    for val in reversed(test_data):  # Push elements in reverse to maintain stack order
        head = ListNode(val, head)
    
    reversed_head = reverse_linked_list_stack(head)
    
    # Convert back to list for display
    linked_list_result = []
    current = reversed_head
    while current:
        linked_list_result.append(current.val)
        current = current.next
    print(f"Linked list stack reversed: {linked_list_result}")
    
    # 3. Test doubly linked list stack reversal
    # Create doubly linked list from test data
    dhead = None
    for val in reversed(test_data):
        new_node = DoublyListNode(val)
        new_node.next = dhead
        if dhead:
            dhead.prev = new_node
        dhead = new_node
    
    reversed_dhead = reverse_doubly_linked_list_stack_efficient(dhead)
    
    # Convert back to list for display
    doubly_linked_result = []
    current = reversed_dhead
    while current:
        doubly_linked_result.append(current.val)
        current = current.next
    print(f"Doubly linked list stack reversed: {doubly_linked_result}")

if __name__ == "__main__":
    test_all_reversals()