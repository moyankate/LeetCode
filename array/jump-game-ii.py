class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_end = 0
        max_reach = 0
        jumps = 0

        # 不check最后一个因为题目保证我们能走到最后一个
        for i in range(len(nums) - 1):
            # 每次比当下对大的数和新产生的数，取最大值
            max_reach = max(max_reach, i + nums[i])
            # 如果当下我们走到了边界点，跳，设currrent_end为新的i 能reach 到最远的地方
            if i == current_end:
                jumps += 1
                current_end = max_reach
        
        return jumps

            
    