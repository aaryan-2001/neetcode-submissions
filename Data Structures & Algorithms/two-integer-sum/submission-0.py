class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            current = target - nums[i]
            if current in d:
                return [d[current],i]
            else:
                d[nums[i]]=i

        