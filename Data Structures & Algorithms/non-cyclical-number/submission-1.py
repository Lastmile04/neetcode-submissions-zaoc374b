class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            accu = 0
            while n != 0:
                digit = n%10
                n = n//10
                accu += digit * digit
            return accu
        slow = n
        fast = happy(n)
        while fast != 1 and  slow != fast:
            slow = happy(slow)
            fast = happy(happy(fast))
        return fast == 1