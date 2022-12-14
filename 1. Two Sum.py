class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        watched = {}
        for i,n in enumerate(nums):
            rem = target - nums[i]

            if rem in watched:
                return [i,watched[rem]]
            watched[n]=i