class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_value = max(candies)
        return [True if max_value <= candi + extraCandies else False for candi in candies]
        