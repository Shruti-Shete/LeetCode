class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
      first = second = float('inf')

      for num in nums:
        if num <= first:     # first = 0 
          first = num
        elif num <= second:
          second = num        # second = 4
        else:
          return True
      return False

 
        
        