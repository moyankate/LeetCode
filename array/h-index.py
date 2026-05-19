class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # sort(citations)
        # l = len(citations)

        # for i in range(0, l):
        #     if citations[i] >= l - i:
        #         return l- i
        # return 0
        citations.sort()
        l = len(citations)

        for i in range(l):
            if citations[i] >= l - i:
                return l - i

        return 0