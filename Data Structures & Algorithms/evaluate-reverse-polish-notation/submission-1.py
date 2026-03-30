class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    n1 = stack.pop() 
                    n2 = stack.pop() 
                    stack.append(n2 + n1)
                case "-":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2 - n1)
                case "*":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(n2 * n1)
                case "/":
                    n1 = stack.pop()
                    n2 = stack.pop()
                    stack.append(int(n2 / n1))
                case _:
                    stack.append(int(t))
                    
        return stack[0]
