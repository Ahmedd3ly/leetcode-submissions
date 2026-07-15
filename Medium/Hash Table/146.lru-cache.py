"""
146. LRU Cache
Difficulty: Medium
https://leetcode.com/problems/lru-cache/

──────────────────────────────────────────────────

Design a data structure that follows the constraints of a Least
Recently Used (LRU) cache.

Implement the LRUCache class:

• LRUCache(int capacity) Initialize the LRU cache with positive size
capacity.

• int get(int key) Return the value of the key if the key exists,
otherwise return -1.

• void put(int key, int value) Update the value of the key if the
key exists. Otherwise, add the key-value pair to the cache. If the
number of keys exceeds the capacity from this operation, evict the
least recently used key.

The functions get and put must each run in O(1) average time
complexity.



Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get",
"get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1,
3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4,
3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4



Constraints:

        • 1 <= capacity <= 3000

        • 0 <= key <= 10^4

        • 0 <= value <= 10^5

        • At most 2 * 10^5 calls will be made to get and put.
"""


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheMap = {}

        # Dummy Nodes to mark list boundaries
        self.left = self.right = Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at right
    def insert(self, node):
        # Always insert right before the 'right' dummy node (Most Recent Used)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            # Refresh its placement to show it was recently accessed
            self.remove(self.cacheMap[key])
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # If key exists, clear old node from the list before updating
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])

        # Create and link new node
        self.cacheMap[key] = Node(key, value)
        self.insert(self.cacheMap[key])

        if len(self.cacheMap) > self.capacity:
            # remove from the list and delete the LRU from the hashMap
            lru = self.left.next
            self.remove(lru)
            del self.cacheMap[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
