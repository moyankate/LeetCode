class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 初始设置profit为0，最低价为正无穷
        max_profit = 0
        min_price = float("inf")

        for price in prices:

            if price < min_price:
                min_price = price
            
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit


