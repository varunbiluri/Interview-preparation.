def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    lo = 0
    hi = len(nums) - 1
    leftProduct = 1
    rightProduct = 1
    while lo < len(nums):
        res[lo] *= leftProduct
        res[hi] *= rightProduct
        rightProduct *= nums[hi]
        leftProduct *= nums[lo]
        lo += 1
        hi -= 1
    return res
