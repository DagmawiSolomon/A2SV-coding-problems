class Solution:
    # Better time complexity O(n)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # length of the array 
        # using the arthimetic sequence formula 
        expected_sum = n * (n + 1) // 2 
        actual_sum = sum(nums) # sum of the array nums
        return expected_sum - actual_sum

    """
    # Better space complexity
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    """




            

       