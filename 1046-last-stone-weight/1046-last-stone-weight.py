class Solution(object):
    def lastStoneWeight(self, stones):
        weight, curr = 0, stones[-1]
        while(len(stones) > 1):
            stones.sort()
            diff = stones[-1] - stones[-2]
            stones = stones[:-2]
            stones.append(diff)
        return stones[0]
        