class Solution(object):
    def permute(self,nums):
    
        if len(nums)==1:
            return [nums]
    
        result = [[nums[0]]]
        tem = []
        for i in range(1,len(nums)):
            for perm in result:
                for j in range(i+1):
                    tem.append(perm[:j] + [nums[i]] + perm[j:])
            result = tem
            tem = []
        return result
