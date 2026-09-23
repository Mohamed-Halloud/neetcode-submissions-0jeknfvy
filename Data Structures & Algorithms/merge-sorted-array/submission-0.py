class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for index, value in enumerate(nums2):
            nums1[-(index+1)] = value

        nums1.sort()
