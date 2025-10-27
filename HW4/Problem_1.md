Part_A:
Pre Order Tree Traversal
 
 First visit the root node.
 Then traverse the left subtree.
 Then traverse the right subtree.

        A
      / | \
     B  C  D
    / \     \
   E   F     G
  /   /
 H   I
AI Generated Tree based on prof's picture

A   // the root
B   // A's left sub
E   // B's left sub
H   // E's left sub
Return to B as End of E's sub
F   // B's right sub
I   // F's left sub
Return to F as End of I's sub
Return to A as End of B's sub
C   // A's 2nd middle sub
Return back to A as C dont have child
D   // A's last sub
G
END

Hence, the pre order traversal of the tree is:
A → B → E → H → F → I → C → D → G


Part B:
BFS: Level Order
Based on level order(layer). Each layer left to right.
Start from the root.

        A
      / | \
     B  C  D
    / \     \
   E   F     G
  /   /
 H   I

L1: A
L2: B C D
L3: E F G
L4: H I

Hence, the level order traversal of the tree is:
A → B → C → D → E → F → G → H → I

PostOrder Traversal
