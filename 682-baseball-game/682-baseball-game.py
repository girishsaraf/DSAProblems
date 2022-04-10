class Solution(object):
    def calPoints(self, ops):
        ans = []
        s = 0
        for op in ops:
            if op == 'C':
                s -= ans[-1]
                ans = ans[:-1]
            elif op == 'D':
                s += 2*ans[-1]
                ans.append(2*ans[-1])
            elif op == '+':
                s += ans[-1] + ans[-2]
                ans.append(ans[-1] + ans[-2])
            else:
                s += int(op)
                ans.append(int(op))
        return s
        