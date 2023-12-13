# 3: 40 ~ 3: 58
from functools import reduce
from collections import defaultdict
class Solution(object):
    def productExceptSelf(self, nums):
        ans = []
        dic = defaultdict(int)
        for num in nums:
            if not dic[num]:
                new_arr = nums[::]
                new_arr.remove(num)
                result = reduce(lambda x, y: x * y, new_arr)
                dic[num] = result

            ans.append(dic[num])
        return ans
