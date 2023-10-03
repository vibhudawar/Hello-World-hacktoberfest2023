#Back-end complete function Template for Python 3

class Solution:
    def solve(self, n, k, stalls):
        stalls.sort()
        
        #Function to count the number of stalls that can be allocated with distance d.
        def count(d):
            ans, curr = 1, stalls[0]
            for i in range(1, n):
                if stalls[i] - curr >= d:
                    ans += 1
                    curr = stalls[i]
            return ans
        
        l, r = 0, stalls[-1] - stalls[0]
        #Binary search to find the maximum possible distance.
        while l < r:
            mid = r - (r - l) // 2
            #Check if it is possible to allocate k stalls with distance mid.
            if count(mid) >= k:
                l = mid
            else:
                r = mid - 1
        return l
