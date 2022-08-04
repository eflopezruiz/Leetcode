class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = (nums1+nums2)
        n = len(s)
        s = sorted(s)
        return (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2] if n else None