from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # both arrays are already sorted
        # append from to end of nums1 (from m) and sort the result
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]

        nums1.sort()
