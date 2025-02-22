"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 10^4.


Time Complexity: O(N log k) where N is the total number of nodes across all lists, and k is the number of linked lists.
Space Complexity: O(k) for storing at most k elements in the heap at any time.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach: 
# used a min-heap to efficiently merge k sorted linked lists by always extracting the smallest node. 
# First, we push the head of each list into the heap with its value and index to handle duplicate values.
# We iteratively pop the smallest node, attach it to the result, and push its next node into the heap until all lists are merged.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        d = ListNode()
        cur = d

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            cur = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return d.next


