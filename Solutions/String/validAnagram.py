class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#         sDict = {}
        
#         if len(s) != len(t):
#             return False
        
#         for letter in s:
#             if letter in sDict:
#                 value += 1
#             else:
#                 add {letter : 1} to sDict
        
#         for letter in t:
#             if letter not in sDict:
#                 return False
#             sDict.get(letter) -= 1
#             if sDict.get(letter) == 0:
#                 remove letter from sDict
        
#         return True

        sDict = {}
    
        if len(s) != len(t):
            return False
        
        for letter in s:
            if sDict.get(letter) != None:
                sDict.update({letter: sDict.get(letter) + 1})
            else:
                sDict.update({letter : 1})
        
        for letter in t:
            if sDict.get(letter) == None or sDict.get(letter) <= 0:
                return False
            sDict.update({letter: sDict.get(letter) - 1})
        
        return True
            
        
            
    
        
        # for letter in t:
        #     if letter in s   
        #         remove 1 occurrence of letter from s
        #     else:
        #         return False
        # if s is empty:
        #     return True
        # return False
        
        for letter in t:
            if s.find(letter) != -1:
                s = s.replace(letter, "", 1)
            else: 
                return False
        
        if len(s) == 0:
            return True
        return False
