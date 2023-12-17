import sys
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -sys.maxsize

        for i in range(len(nums) - k + 1):
            if not i:
                tmp = sum(nums[i:i+k])
            else:
                tmp = prev + nums[i+k-1]

            max_sum = max(max_sum, tmp)
            prev = tmp - nums[i]
                
        return max_sum / k