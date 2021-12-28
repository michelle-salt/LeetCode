class Solution:
    def isValid(self, s: str) -> bool:
#         create empty stack
       
#         if strlen not divisible by 2
#             return False
        
#         loop through each char
#             if char is (, [, or {
#                 add to stack
#             else:
#                 if char is )
#                     if stack is empty or last char in stack is not (
#                         return False
#                     pop last char from stack
#                ^^ do same for other closed brackets
        
#         if stack is empty:
#             return True
#         return False
                     
        if len(s) % 2 == 1:
            return False
        
        openBrackets = []
        
        for c in s:
            if c == '(' or c == '[' or c == '{':
                openBrackets.append(c)
            else:
                if len(openBrackets) == 0:
                    return False
                if c == ')':
                    if openBrackets[-1] != '(':
                        return False
                    openBrackets.pop()
                elif c == ']':
                    if openBrackets[-1] != '[':
                        return False
                    openBrackets.pop()
                elif c == '}':
                    if openBrackets[-1] != '{':
                        return False
                    openBrackets.pop()
                
        if len(openBrackets) == 0:
            return True
        return False
                    
              
