# cheatsheet

By data structure:

* array & string
  * sorting: assumed O(N log N) with merge sort
  * string can be thought of as or converted to array for convenience of manipulation
  * fast lookup and push/append with time complexity O(1)
  * slow insert and delete with O(n)
  * two pointer
  * binary search when ‘sorted’
* hash table
  * fast insert lookup and delete with  time complexity O(1)
  * uses linked list to solve collision
* linked list
  * fast prepend and append, O(1)
  * slow lookup, insert and delete with O(n) as they need to traverse all the way to the end
  * a “dummy” node is usually put in front of head for helping traversal when head is changing
* tree
  * binary search tree
    * sorted
    * any node’s value must be >= left child tree’s nodes, \
and must be &lt;= right child tree’s nodes
    * do stuff at root (of child tree), then traverse to left and right recursively
    * when target is assigned:  \
do stuff if root.val == target,  \
traverse left tree with target when root.val > target, \
traverse right tree with target when root.val &lt; target,
    * height-balanced?
  * depth first traversal (better performance): in order, pre-order and post-order \
most often with recursion, can use stack as iterative approach
  * breadth first traversal \
can use queue
  * recursion
  * consider relationship among parent tree/node and children tree/node
  * sometime about “path” and “option list”
  * how to insert/delete node/construct tree
  * heap
  * trie
* graph
  * directed and undirected
  * adjacency list/matrix
* stack and queue
  * can be implemented with array or (doubly) linked list, usu. deque in Python

By pattern:

* two pointer
  * both from head,  \
right go first, then move left when part of a condition is met (special case of sliding window)
  * left and right, mostly head and tail \
would be useful to limit left &lt; right to avoid overfolowing
  * fast and slow, ie. turtle and hare
  * mostly seen with while looping,  \
limits are usually added like l &lt; r, r &lt;len(nums)... etc.
  * data structure may be “sorted”
* merge intervals
* cyclic sort
* binary search
  * conditions: given a “sorted iterable” and a “target” and search for any index
  * O(log(N))
  * define left and right (two pointer), usu. head and tail
  * while limit not exceeded: (like l&lt; r, q exists):

    make mid (exclude duplication),  \
consider when mid value is exactly the target or bigger or smaller,  \
then move left and right

  * consider left and right borders: +=1, &lt;= or &lt;
  * must list every case with ‘else if’
* BFS & DFS
  * set ‘visited’ for graphs
* two heaps
* top K elements
* next greater element
* bitwise manipulation, esp. XOR
* backtracking: ending condition, path, option list
  * merely MECE & decision tree traversal, time complexity is inevitably high

  1. define result and path container \
  2. backtrack, starting from root or dummy node \
  3. sanity check for ending condition,  \
        record current path data to result and return to previous layer when exceeding,  \
        ie. when reaching the leaf node of tree \
  4. record current path data if not ended \
  5. iterate over option list, on each node:  \
    visit current node and make decision (remove the option from list, or visit it and add to path),  \
    backtrack with current path and option list,  \
    and canel decision to unvisit the node

* recursion: ending condition + self calling
  * mostly ‘top-down’ approach
* dynamic programming: state, choice and base case
  * whenever there’s “cause and effect”
  * mostly ‘bottom-up’ approach
  * recursion + additional tricks to save results from sub-problems for later use
  * memoization for duplicated sub-problem (better for single ans value iteration)
  * tabulation (usually in the form of a list) to record current state for each sub-problem
  * essentially MECE -> n-ary tree traversal:

    divide problem to sub-problem, and run recursively

  * characterize the optimal sub-structure of solution
  * recursively define (duplicated) sub-problems and calculate the solutions of sub-problems
  * construct state-transition equilibrium
* sorting
  * only need to know:  \
bubble sort, selection sort (need to know implementation) quick sort, merge sort and heap sort(need to know time complexities and stability)
