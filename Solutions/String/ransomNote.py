class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # for each letter in ransomNote:
        #     if magazine.indexOf(letter) == -1:
        #         return False
        #     magazine.remove(letter)
        # return True
        
        for i in range(len(ransomNote)):
            if magazine.find(ransomNote[i]) == -1:
                return False
            magazine = magazine.replace(ransomNote[i], '', 1)
        return True
    
        #solution without string methods:
        countLetter = [0]*26
        
        for i in range(len(magazine)):
            countLetter[ord(magazine[i]) - ord('a')] += 1
        
        for i in range(len(ransomNote)):
            countLetter[ord(ransomNote[i]) - ord('a')] -= 1
            if countLetter[ord(ransomNote[i]) - ord('a')] == -1:
                return False
        return True
