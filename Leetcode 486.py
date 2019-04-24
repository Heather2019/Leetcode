class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        
        mem = [[0]*n for _ in range(n)]
        
        def selectnumber(l,r):
            if l==r:
                mem[l][r] == nums[l]
                return mem[l][r] 
            if mem[l][r] >0:
                return mem[l][r]
            mem[l][r] = max(nums[l]-selectnumber(l+1,r),nums[r]-selectnumber(l,r-1))
            return mem[l][r]
        
        return True if selectnumber(0,n-1) >=0 else  False
            
