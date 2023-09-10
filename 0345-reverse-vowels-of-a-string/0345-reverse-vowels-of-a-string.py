class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("AEIOUaeiou")
        s = list(s)
        start, end = 0 , len(s) - 1
        while start < end:
            if s[start] in vowel and s[end] in vowel:
                s[start] , s[end] = s[end] , s[start]
                start += 1
                end -= 1
            elif s[start] not in vowel:
                start += 1
            elif s[end] not in vowel:
                end -= 1
        return "".join(s)
                

 



            
                    



                






    