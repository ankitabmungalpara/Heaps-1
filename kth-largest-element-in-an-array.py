"""

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4


Time Complexity:
- Min-heap approach: O(n log k) (heap operations take log k time, iterating over n elements)
- Max-heap approach: O(n + k log n) (heapify takes O(n), and extracting k elements takes O(k log n))

Space Complexity:
- Min-heap approach: O(k) (storing k elements in heap)
- Max-heap approach: O(1) (modifying input list in-place)


Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

import heapq

# Approach:
# The first approach uses a min-heap of size k, where we maintain the k largest elements seen so far.
# The second approach converts the input list into a max-heap (by negating elements), then extracts the kth largest element.
# Both approaches ensure efficient retrieval of the kth largest element using heap properties.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # min-heap
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num) 

        return min_heap[0]

        # max-heap
        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)



