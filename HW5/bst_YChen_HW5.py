import random


class Node:
    # simple BST node with value and two children
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class BST:
    # basic BST with add, delete, find, and print
    def __init__(self):
        self.root = None
        self.size = 0

    def add_node(self, value: int) -> None:
        # insert value into BST, ignore duplicates
        if self.root is None:
            self.root = Node(value)
            self.size = 1
            return
        cur = self.root
        while True:
            if value == cur.value:
                return  # ignore duplicate
            elif value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    self.size += 1
                    return
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = Node(value)
                    self.size += 1
                    return
                cur = cur.right

    def find_node(self, value: int):
        # find node by value, return Node or None
        cur = self.root
        while cur is not None:
            if value == cur.value:
                return cur
            cur = cur.left if value < cur.value else cur.right
        return None

    def delete_node(self, value: int) -> None:
        # delete node by value, do nothing if not found
        def _min_value_node(node: Node) -> Node:
            # find the left-most node in subtree
            cur = node
            while cur.left is not None:
                cur = cur.left
            return cur

        def _delete(node: Node, value: int):
            if node is None:
                return None, False
            if value < node.value:
                node.left, removed = _delete(node.left, value)
                return node, removed
            if value > node.value:
                node.right, removed = _delete(node.right, value)
                return node, removed

            # node.value == value: remove this node
            if node.left is None and node.right is None:
                return None, True  # leaf
            if node.left is None:
                return node.right, True  # only right child
            if node.right is None:
                return node.left, True  # only left child
            # two children: replace with inorder successor
            successor = _min_value_node(node.right)
            node.value = successor.value
            node.right, _ = _delete(node.right, successor.value)
            return node, True

        self.root, removed_flag = _delete(self.root, value)
        if removed_flag:
            self.size -= 1

    def print_tree(self) -> None:
        # pretty print the tree sideways (right -> root -> left)
        def _print(node: Node, level: int) -> None:
            if node is None:
                return
            _print(node.right, level + 1)
            print("    " * level + f"[{node.value}]")
            _print(node.left, level + 1)

        print("\n=== BST ===")
        if self.root is None:
            print("(empty)")
        else:
            _print(self.root, 0)
        print("============\n")


def demo() -> None:
    # generate random input set size 5..50, values 1..1000
    size = random.randint(5, 50)
    values = random.sample(range(1, 1001), size)

    print("Input set:", values)

    bst = BST()
    for v in values:
        bst.add_node(v)

    print("Initial tree:")
    bst.print_tree()

    # exercise add: add 5 new values not in current tree
    current_set = set(values)
    candidates = [x for x in range(1, 1001) if x not in current_set]
    add_values = random.sample(candidates, k=min(5, len(candidates)))
    for val in add_values:
        print(f"Add {val}")
        bst.add_node(val)
        current_set.add(val)
        bst.print_tree()

    # exercise delete: delete 5 values from current tree if possible
    if len(current_set) > 0:
        delete_values = random.sample(list(current_set), k=min(5, len(current_set)))
    else:
        delete_values = []
    for val in delete_values:
        print(f"Delete {val}")
        bst.delete_node(val)
        current_set.discard(val)
        bst.print_tree()

    # exercise findNode positive and negative cases
    if len(current_set) > 0:
        pos_val = random.choice(list(current_set))
    else:
        pos_val = None
    neg_candidates = [x for x in range(1, 1001) if x not in current_set]
    neg_val = random.choice(neg_candidates) if neg_candidates else None

    if pos_val is not None:
        print(f"Find {pos_val}:", "FOUND" if bst.find_node(pos_val) else "NOT FOUND")
    else:
        print("Find positive case skipped: tree is empty")
    if neg_val is not None:
        print(f"Find {neg_val}:", "FOUND" if bst.find_node(neg_val) else "NOT FOUND")
    else:
        print("Find negative case skipped: no candidate")


if __name__ == "__main__":
    # you can set a seed here for reproducible runs (optional)
    # random.seed(42)
    demo()

