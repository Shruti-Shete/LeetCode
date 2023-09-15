class Solution:
    def reverseWords(self, s: str) -> str:
        start = end = 0
        j = len(s) - 1
        result = ""
        word = ""
        length = len(s)

        while start < length:
            while (start < length and s[start] == " "):
                start += 1
            while  (j < length and s[j] == " "):
                j -= 1
            if start > j + 1: 
                break
            end = start + 1
            while (end < j + 1 and s[end] != " "):
                end += 1
            word = s[start:end:1]
            if len(result) == 0:
                result = word
            else:
                result = word + " " + result
            start = end + 1
        return str(result)



        