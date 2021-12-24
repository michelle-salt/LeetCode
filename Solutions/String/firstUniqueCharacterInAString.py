class Solution:
    def firstUniqChar(self, s: str) -> int:    
#         create empty set, hashtable
#         for i in range(len(s)):
#             if letter in hashtable:
#                 remove from set
#             else:
#                 add to hashtable (key = letter, value = index)
                
#         if set is empty:
#             return False
#         else:
#             get first item in set
#             return hashtable.get(^^)

        uniques, allLetters = [], {}
        
        for i in range(len(s)):
            if allLetters.get(s[i]) != None:
                if allLetters.get(s[i]) != -1:
                    uniques.remove(s[i])
                    allLetters.update({s[i] : -1})
            else:
                allLetters.update({s[i]:i})
                uniques.append(s[i])
                
        if not uniques:
            return -1
        else:
            return allLetters.get(uniques[0])
