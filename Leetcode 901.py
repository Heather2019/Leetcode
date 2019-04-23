class StockSpanner(object):

    def __init__(self):
        self.stack = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        
        res = 1
        
        while self.stack and self.stack[-1][0] <= price:
            res = res + self.stack.pop()[1]
        
        self.stack.append((price,res))
        
        return res
        
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
