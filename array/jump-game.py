class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last = len(nums) - 1
        for i in range(last):
            val = nums[i]
            i += val
        
        return i == last
