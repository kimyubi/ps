class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if not num:
                nums.remove(num)
                nums.append(num)
        
        