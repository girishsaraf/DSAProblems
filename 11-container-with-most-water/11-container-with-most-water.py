class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_val = 0
        while(left < right):
            water = (right-left) * min([height[left], height[right]])
            max_val = max([max_val, water])
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_val