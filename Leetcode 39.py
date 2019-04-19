class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        candidates.sort()
        
        Stack = [(0,list(),target)]
        
        while Stack:
            i,path,remain = Stack.pop()
            
            while i < len(candidates):
                if path and remain<path[-1]:
                    break
                if candidates[i] == remain:
                    res.append(path + [candidates[i]])
                
                Stack = Stack + [(i,path + [candidates[i]],remain-candidates[i])]
                i=i+1
        
        return res
        
        
                    
        
