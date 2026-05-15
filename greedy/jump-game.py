class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 对于每个i，看这个i最远能走到哪里，如果下一个要visit的i已经超过当下能走到的最远距离，return false

        max_reach = 0

        for i in range(len(nums)):
            
            if i > max_reach:
                return False
            
            current_max = i + nums[i]
            max_reach = max(max_reach, current_max)
        
        return True


