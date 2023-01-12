class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        arr1 = [0,0]
        arr2 = [0,0]
        hmap = {'a':1,'i':1,'e':1,'o':1,'u':1}
        for i in range(half):
            if hmap.get(s[i].lower(),0):
                arr1[0] += 1
            else:
                arr1[1] += 1 

        for i in range(half, len(s)):
            if hmap.get(s[i].lower(),0):
                arr2[0] += 1
            else:
                arr2[1] += 1 
        
        if arr1 == arr2:
            return True
