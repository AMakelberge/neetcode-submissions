class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:]):
                if n + m == target:
                    return [i,i+j+1]