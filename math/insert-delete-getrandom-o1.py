class RandomizedSet(object):

    def __init__(self):
        self.nums = []
        self.pos = {}
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        
        # if present, return false
        if val in self.pos:
            return False
        
        # if not present, insert, return true
        # 把新的数填到数列的最后端（position是现在数列的长度）
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True 

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
    
        # if not present, return false
        if val not in self.pos:
            return False
        
        # if present, remove, return true
        # because we want remove to be O(1), we switch the position of the element we want to 
        # remove with the last element, then pop the last element
        index = self.pos[val] # index of value we want to remove
        last = self.nums[-1] # value of the last element

        self.nums[index] = last
        self.pos[last] = index

        self.nums.pop()

        del self.pos[val]

        return True 

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()