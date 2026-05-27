"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val) # orignal node : clone of original node
        q = deque([node]) # start queue with original node

        while q:
            cur = q.popleft()
            for nei in cur.neighbors: # look at the original neighbors of the original node
                if nei not in oldToNew: # if we don't have original neighbors in our hashmap, then we clone it in our hashmap
                    oldToNew[nei] = Node(nei.val) # original neighbor node : clone neighbor node
                    q.append(nei) # append neighbor in queue to check later
                oldToNew[cur].neighbors.append(oldToNew[nei]) # original node : clone of original node with neighbors to each clone neighbor node

        return oldToNew[node] # by returning the first node, it acts as a head for a linked list, and returns the entire graph with its neighbors

        '''
        1st example:
        original node 1 value 1 : clone node 1 value 1 -> neighbors [clone node 2 value 2]
        original node 2 value 2 : clone node 2 value 2 -> neighbors [clone node 1 value 1, clone node 3 value 3]
        original node 3 value 3 : clone node 3 value 3 -> neighbors [clone node 2 value 2]
        '''