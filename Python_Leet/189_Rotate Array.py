class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        
        
        out = []
        k = k%len(nums)
        for i in range(len(nums)):
            out.append(0)
        # print(out)
        for i in range(len(nums)):
            val = input[i]
            if i+k < len(nums):
                out[i+k] = val
            else:
                out[i+k-len(nums)] = val
        return out
