#!/usr/bin/env python

# O(m+n solution)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        i,j,ret= 0,0,0
        if (m+n) % 2 == 1:
            median_num = (m+n+1)/2
            while i + j < median_num:
                if (j == n) or (i < m and nums1[i] < nums2[j]):
                    ret = nums1[i]
                    i += 1
                else:
                    ret = nums2[j]
                    j += 1
            return ret
        else:
            ret_m1 = 0
            median_num = (m+n) / 2 + 1
            while i + j < median_num:
                ret_m1 = ret
                if (j == n) or (i < m and nums1[i] < nums2[j]):
                    ret = nums1[i]
                    i += 1
                else:
                    ret = nums2[j]
                    j += 1
            return float(ret + ret_m1) / 2
                