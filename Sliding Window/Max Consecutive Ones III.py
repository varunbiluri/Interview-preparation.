class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeroCounter = 0
        for right, num in enumerate(nums):
            if num == 0: zeroCounter += 1
            if zeroCounter > k:
                if nums[left] == 0: zeroCounter -= 1
                left += 1

        return right - left + 1