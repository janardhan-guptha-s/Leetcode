class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Merge both arrays into a temporary array and sort it.
        merged = nums1[0:m] + nums2
        merged.sort()
        
        # Copy the sorted merged array back to nums1.
        for i in range(m + n):
            nums1[i] = merged[i]
