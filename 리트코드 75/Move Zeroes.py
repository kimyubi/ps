class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if not num:
                nums.remove(num)
                nums.append(num)
        
# O(1)       
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        anchor = 0
        for explorer in range(len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor += 1
        