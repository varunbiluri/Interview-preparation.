class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for window_end in range(k, len(nums)):
            window_sum = window_sum - nums[window_end - k] + nums[window_end]
            max_sum = max(max_sum, window_sum)

        return max_sum / k