class Solution(object):
    def countBits(self, n):
        res = []
        for i in range(n+1):
            binary = "{0:b}".format(int(i))
            res.append(binary.count('1'))
        return res