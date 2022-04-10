class Solution(object):
    def calPoints(self, ops):
        ans = []
        for op in ops:
            if op == 'C':
                ans = ans[:-1]
            elif op == 'D':
                ans.append(2*ans[-1])
            elif op == '+':
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(op))
        return sum(ans)
        