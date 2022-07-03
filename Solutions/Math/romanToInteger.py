class Solution:
    def romanToInt(self, s: str) -> int:
        letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        i = 0
        while i < len(s):
            letter = s[i]
            sum += letters[letter]
            if i != len(s) - 1:
                if letter == 'I':
                    if s[i+1] == 'V':
                        sum += 4 - 1
                        i += 1
                    elif s[i+1] == 'X':
                        sum += 9 - 1
                        i += 1
                elif letter == 'X':
                    if s[i+1] == 'L':
                        sum += 40 - 10
                        i += 1
                    elif s[i+1] == 'C':
                        sum += 90 - 10
                        i += 1
                elif letter == 'C':
                    if s[i+1] == 'D':
                        sum += 400 - 100
                        i += 1
                    elif s[i+1] == 'M':
                        sum += 900 - 100
                        i += 1
            i += 1
        return sum
            
