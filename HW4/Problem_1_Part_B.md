# Problem 1 Part B. AI Assisted MD Format

```
        A
       / \
      B   C
     / \   \
    D   E   F
   /       / \
  G       H   I
```
(AI Generated markdown friendly format)

## In-Order Traversal

### Rule:
- Recursively traverse the left sub. (Will jump over current node!)
- Visit the current node.
- Recursively traverse the right sub.

Notice that it most for BINARY tree only.

### Step-by-step process:
1. A, but jump over A, no visit
2. B. A's left sub, Visit
3. D. B's left sub, Visit
4. G. Visit. Keep doing as D's left sub is G. Then find G is the terminal. Go back to D. Then go back to B.
5. Visit B, as the current root.
6. Visit E, as B's right sub.
7. Go back to A, the current root node. Visit A
8. Visit C, as A's right sub.
9. Go to F. Now F is the current root. F have right sub. Skip F itself and visit F's left node.
10. Visit H. Then Visit F, then I

Hence, the in order traversal of the tree is:
`G -> D -> B -> E -> A -> C -> H -> F -> I`