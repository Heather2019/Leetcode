class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        sum0=nums[0]+nums[1]+nums[2]
        if len(nums)==3 or sum0 == target:
            return sum0
        
        i=0
        
        while i < len(nums)-2:
            while   i>0 and i < len(nums)-2 and nums[i] == nums[i-1]  :
                i=i+1
            j = i+1
            k = len(nums) -1
            
            while j<k:
                while nums[j]==nums[j-1] and j>i+1 and j<k-1:
                    j=j+1
                
                newsum = nums[i]+nums[j]+nums[k]
                if abs(newsum-target)<abs(sum0-target):
                    sum0 = newsum
                if sum0==target:
                    return sum0
                if newsum > target:
                    k=k-1
                else:
                    j=j+1
            
            i=i+1
        
        return sum0
                
                
