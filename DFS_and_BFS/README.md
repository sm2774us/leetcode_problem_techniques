# DFS

<ins>**D**</ins>epth-<ins>**F**</ins>irst <ins>**S**</ins>earch (**DFS**) and <ins>**B**</ins>readth-<ins>**F**</ins>irst <ins>**S**</ins>earch 
(**BFS**) are common algorithms for searching **trees** or **graphs**.

In **DFS**, you start at the root of the tree (or a selected node if it’s a graph) 
and search as far as possible along each branch before backtracking. 
DFS is great for searching trees that are deeper than they are wide. 
In technical interviews, DFS is good for solving puzzles that have 
only one solution (like mazes).

In **BFS**, on the other hand, you start at the root of the tree (or a selected node in a graph) 
and search each subsequent level of nodes before moving on to the next level. BFS is great for searching trees 
that are wider than they are deep. In an interview, BFS is a great option for problems about file system traversal, 
printing hierarchies in order, and finding the shortest path between two nodes in a graph.

DFS and BFS are both methods of searching a tree or graph for nodes with particular properties. Both methods allow the reconstruction of a path from the starting node to the solution node(s).

Because they both do the same thing, it can be difficult to decide whether DFS or BFS is the better approach. For problems where we are looking for solutions that are close to the starting node, BFS is a better choice since it searches the closest nodes first. For many problems, the approach depends on the structure of the tree or graph.

Because trees and graphs can contain a lot of nodes, the memory requirements may guide whether you use DFS or BFS. For trees, BFS requires you to store all the nodes at a given level, while DFS requires you to store an entire path from root to leaf. Because trees are often balanced, i.e. structured in a way to minimize depth, DFS will generally require less memory. However, some decision trees and some generated trees can have branches that are infinitely long, in which case BFS would be a better choice.

A full binary search tree with depth d will require O(log d) memory for DFS but O(2d) memory for BFS.

## **Important Concepts**

------------------------

* **Branching factor (of a tree):**
  
  The maximum number of children that a node in a tree has.


* **Depth or height (of a tree):**
  
  The maximum path length between the root and a leaf in the tree.


* **Visited:**
  
  A ___visited___ node is any node that the search algorithm has already looked at. This is especially important for graphs, as keeping track of visited nodes ensures that we don't produce infinite loops.

## **Related Concepts**

------------------------

* **Trees and Graphs:**

  Both DFS and BFS search are methods for searching through a ___graph___ 
  (and often this graph is a ___tree___) to find a particular node. 
  It's important that you are familiar with trees before you continue on with this article.


* **Acyclic graphs:**

  Any graph where there is at most one path between any two nodes 
  (i.e. there are no "loops"/"cycles" in the graph). All trees are acyclic 
  by definition.


* **Stacks:**

  DFS can be implemented using a stack to store the nodes that have already 
  been visited.


* **Queues:**

  BFS can be implemented using a queue to store the nodes in the next level 
  that haven't been visited.


* **Backtracking:**

  Backtracking can be thought of as a version of DFS that is used when a graph/tree 
  has additional structure that allows you to know that descendants of a node cannot satisfy 
  your search criteria, and will not visit them.
  
## **Generalized Algorithms**

------------------------

Our goal is to find all nodes that satisfy some condition. We will refer to these nodes 
as ___solutions___. Here we keep track of all the visited nodes, which can use a substantial 
amount of memory. The array `visited` is there to prevent the code running in an infinite loop, 
so if we know we have a tree (or more generally any ___acyclic graph___) we don't need `visited`.

### **Recursive DFS**

------------------------

```
function DFS_recur(node current , set solutions, set visited):
    add current onto visited

    if current is a solution:
        add current to solutions

    for each edge from current:
        new_state <- state obtained from current by following edge
        if new_state not in visited:
          DFS_recur( new_state, solutions, visited )
```

If the nodes can be altered, it is often useful to store the "visited" status 
in the nodes instead of in a separate data-structure. Then looking up whether 
`new_state` has been visited requires looking at the appropriate field of 
`new_state`, rather than searching through the `visited` data structure.

For a tree, or other acyclic graph, the recursive algorithm for DFS is simpler 
and requires less memory:

```
// Only use this version for acyclic graphs!
function DFS_recur(node current , set solutions ):
    if current is a solution:
        add current to solutions

    for each edge from current:
        new_state <- state obtained from current by following edge
        DFS_recur( new_state, solutions )
```

In some languages, there is a limit to how many nested recursive calls you 
are allowed to make. Exceeding this limit raises a stack overflow error. 
(Python is notorious for defaulting to a low number of nested recursive calls.) 
Behind the scenes, calling a function recursively pushes all your variables to the 
call stack. We can get around this limit by implementing our own stack in an 
iterative version.


### **BFS and Iterative DFS**

------------------------

BFS is usually implemented using a queue (First In, First Out) to store nodes, 
and looks quite different from our recursive DFS. By writing an iterative version 
of DFS using an explicit stack (First In, Last Out) to store nodes, we can see 
that they're quite similar.

```
function BFS_iter(node start_node):
    create empty set visited
    create empty queue Q
    create empty set solutions

    add start_node to visited
    Q.enque(start_node)

    while Q is not empty:
      current = Q.deque()
      if current is a solution:
        add current to solutions

      for each edge from current:
        new_state <- state obtained from current by following edge
        if new_state not in visited:
          add new_state to visited
          Q.enque(new_state)
    return solutions
```

Compare this to an iterative version of DFS:

```
function DFS_iter(node start_node):
  create empty set visited
  create empty stack Stk
  create empty set solutions

  add start_node to visited
  Stk.push(start_node)

  while Stk is not empty:
    current = Stk.pop()
    if current is a solution:
      add current to solutions

    for each edge from current:
      new_state <- state obtained from current by following edge
      if new_state not in visited:
        add new_state to visited
        Stk.push(new_state)
    return solutions
```

We see that other than the names of the methods for adding and removing elements 
(`push` and `pop` vs `enque` and `deque`), the algorithms are almost exactly the same.

If we have a tree or other acyclic graph, the code can be simplified more by dropping 
all the lines that refer to the `visited` set.


### **Pathfinding**

------------------------

For some problems, such as finding a path through the maze, finding the node (the exit) 
isn't that interesting. Instead, we're looking for the path to the desired node.

An easy modification that allows a reconstruction of a path is to make the visited elements 
contain two pieces of information: the node that was visited, and where it was visited from. 
Once you have the desired node, you can follow the from nodes back to the start to recover the path.

### **For An Interview, Expect To See Problems Like...**

------------------------

* **Finding a path out of a maze.**
* **Finding the shortest path between two nodes.**
* **Finding all friends and friends of friends in a social network.**
* **Finding all nodes reachable from a given node in a graph** (i.e. identifying the connected component containing a given node).
