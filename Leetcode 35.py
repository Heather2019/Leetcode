class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._searchInsert(nums, target,left=0,right=len(nums)-1)
    
    def _searchInsert(self,nums, target,left,right): 
        if left>=right:
            if nums[left]>=target:
                return left
            else:
                return left+1

        if left<right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return self._searchInsert(nums,target,left,mid-1)
            else:
                return self._searchInsert(nums,target,mid+1,right)
