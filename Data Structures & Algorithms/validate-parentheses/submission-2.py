class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_map = { '}': '{', ']':'[', ')':'(' }
        for char in s:
            if char in p_map:
                if stack and stack[-1] == p_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False