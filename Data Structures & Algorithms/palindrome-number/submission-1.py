class Solution:
    def isPalindrome(self, x: int) -> bool:
        #input is integer, output boolean true if palindrome
        #fits in memory 
        
        #edge case
        if x<0: 
            return False 
        original = x
        reversed_num = 0
        while x>0:
            reversed_num = reversed_num*10+x%10
            x//=10
        return original==reversed_num  

