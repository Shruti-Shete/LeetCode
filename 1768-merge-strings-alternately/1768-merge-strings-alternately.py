class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        merged = list ()
        pointer1 = pointer2 = 0
        
        while pointer1 < len(word1) and pointer2 < len(word2):
            a , b = word1[pointer1] , word2[pointer2] 
            merged.append(a)
            merged.append(b)
            pointer1 += 1
            pointer2 += 1
            
        while pointer1 >= len(word1) and pointer2 < len(word2):
                a = word2[pointer2]
                merged.append(a)
                pointer2 += 1
               
        while pointer2 >= len(word2) and pointer1 < len(word1):
                a = word1[pointer1]
                merged.append(a)
                pointer1 += 1
                
        return ''.join(merged) 
            
        