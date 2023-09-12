class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
      result = list()
      highestnum = max(candies)
      start = 0
      while start < len(candies):
        if (int(candies[start]) + extraCandies) >= highestnum:
          result.append(True)
          start += 1
        else:
          result.append(False)
          start += 1
      return result  
      
