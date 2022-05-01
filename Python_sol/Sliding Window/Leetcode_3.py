class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        count = 0
        maxi = 0
        temp =0
        
        # Time Complexity: O(n+temp) and Space Complexity: O(n)
        for i in s:
            # Avoids duplicates
            if i not in arr:
                arr.append(i)
                count +=1
            else:
                # Updating the max substring found so far
                if count>maxi:
                    maxi = count
                arr.append(i)
                count +=1
                
                # remove the strings before i
                temp = arr.index(i)
                if temp > 0:
                    for j in range(temp+1):
                        arr.pop(0)
                        count -=1
                else:
                    arr.pop(0)
                    count -=1
        return max(maxi,count)