class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def happy(n):
            sum = 0
            while n != 0:
                digit = n%10
                n = n//10
                sum += digit * digit
            return sum
        
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = happy(n)
            
        if n==1:
            return True
        else:
            return False