class Solution(object):
    def winningPlayer(self, x, y):
        y=y//4
        a=min(x,y)
        if a%2==0: return "Bob"
        else: return "Alice"