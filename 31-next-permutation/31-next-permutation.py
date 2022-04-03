class Solution(object):
    def nextPermutation(self, nums):
        back = len(nums) - 1
        while (back > 0 and nums[back] <= nums[back-1]):
            back -= 1
        if back == 0:
            nums.sort()
        else:
            new_back = len(nums) - 1
            while nums[new_back] <= nums[back-1]:
                new_back -= 1
            nums[back-1], nums[new_back] = nums[new_back], nums[back - 1]
            left, right = back, len(nums) - 1
            while(left < right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1