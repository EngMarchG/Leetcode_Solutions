class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
      hmap = {5:0, 10:0, 20:0}
      
      for bill in bills:
        hmap[bill] += 1
        if bill > 5:
          temp = bill

          while temp > 5:
            if temp > 10 and hmap[10]:
              temp -= 10
              hmap[10] -= 1
            else:
              temp -= 5
              hmap[5] -= 1

            if hmap[5] < 0 or hmap[10] < 0:
              return False

      return True
        