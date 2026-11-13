from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "/", "*"]
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand_1, operand_2 = stack.pop(), stack.pop()
                match token:
                    case "+":
                        output = operand_1  + operand_2
                        stack.append(output)
                        continue
                    case "-":
                        output = operand_2 - operand_1
                        stack.append(output)
                        continue
                    case "/":
                        output = operand_2 / operand_1
                        stack.append(int(output))
                        continue
                    case "*":
                        output = operand_1 * operand_2
                        stack.append(output)
                        continue
                
        
        return int(stack[0])

# print(Solution().evalRPN(["4","13","5","/","+"]))