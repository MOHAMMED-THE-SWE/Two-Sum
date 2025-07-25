class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, i+1]