class Solution(object):
    def topKFrequent(self, nums, k):
        uniques = list(set(nums))
        c_dict = {}
        for val in uniques:
            c_dict[val] = nums.count(val)
        keys = sorted(c_dict.items(), key = lambda x: x[1], reverse=True)
        ans = []
        for i in range(k):
            ans.append(keys[i][0])
        return ans
        
        