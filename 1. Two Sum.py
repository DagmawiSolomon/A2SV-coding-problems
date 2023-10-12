class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        n = len(nums)

        for i in range(n):
            # get the number that gives our target number
            addend = target - nums[i]
            # check if it's in our dictionary/ hash map
            if addend in my_dict:
                return [my_dict[addend], i]
            my_dict[nums[i]] = i
        return []
