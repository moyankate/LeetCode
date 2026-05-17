class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 从后往前对比每个list 里的valid element，把更大的那一个加到nums1后面
        # 3 个指针，分别对应nums1, nums2目前要比较的对象和nums1 后面的空位
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p2 >= 0 :
        
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
        
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
        
            p -=1
        
