class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                candidate = x

            if x == candidate:
                count += 1
            
            else:
                count -= 1
        
        return candidate