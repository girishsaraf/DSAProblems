class Solution(object):
    def threeSumMulti(self, arr, target):
        arr.sort()
        mod = 10**9 + 7
        final = 0
        for i in range(len(arr)):
            rem = target - arr[i]
            left, right = i + 1, len(arr) - 1
            
            while(left<right):
                if arr[left] + arr[right] < rem:
                    left += 1
                elif arr[left] + arr[right] > rem:
                    right -= 1
                elif arr[left] != arr[right]:
                    lc = rc = 1
                    while left+1 < right and arr[left] == arr[left + 1]:
                        lc += 1
                        left += 1
                    while right - 1 > left and arr[right-1] == arr[right]:
                        rc += 1
                        right -= 1
                    
                    final += lc*rc
                    final%= mod
                    left += 1
                    right -= 1
                else:
                    final += (right - left + 1) * (right-left) / 2
                    final %= mod
                    break
        return final
                        
                
        