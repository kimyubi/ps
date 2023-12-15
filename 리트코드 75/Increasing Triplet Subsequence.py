# 11:08 ~ 11: 26 : 시간 초과
class Solution(object):
    def increasingTriplet(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return True if 3 <= max(dp) else False
    

#시간 초과 해결 풀이 O(N)
import sys
class Solution(object):
    def increasingTriplet(self, nums):
        if len(nums) < 3:
            return False

        first, second = sys.maxsize, sys.maxsize
        for third in nums:
            if third <= first:
                first = third
            elif third <= second:
                second = third
            else:
                return True

        return False

