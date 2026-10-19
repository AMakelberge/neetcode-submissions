class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numTable = set(nums)
        maxC = 0
        for num in numTable:
            if num - 1 not in numTable:
                temp = num
                c = 0
                while temp in numTable:
                    c += 1
                    temp += 1
                if c > maxC:
                    maxC = c
        return maxC