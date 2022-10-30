class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        arr = []
        counter = 1
        
        # Time complexity O(N*m^2) Space complexity O(set(N) + m)
        for ele in strs:
            el = "".join(sorted(ele))
            if hmap.get(el, 0):
                arr[hmap[el]-1].append(ele)
            else:
                hmap[el] = counter
                arr.append([ele])
                counter += 1
        return arr