class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        res = [0] * len(T)
        stack = []
        
        for i,t in enumerate(T):
            while stack and T[stack[-1]] < t:
                tem = stack.pop()
                res[tem] = i-tem
            
            stack.append(i)
        
        return res
