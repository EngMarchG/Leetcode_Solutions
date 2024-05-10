class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        hmap = {}
        mini = min(k, len(arr))

        for pos, num in enumerate(arr):
            limit = max(len(arr)-mini-2, pos)
            for i in range(len(arr)-1, limit, -1):
                if not hmap.get(num/arr[i], 0):
                    hmap[num/arr[i]] = []
                hmap[num/arr[i]].extend([num, arr[i]])

        # In case of duplicate keys
        def quicksort(keys):
            if len(keys) <= 1:
                return keys
            pivot = keys[len(keys) // 2]
            left = [x for x in keys if x < pivot]
            middle = [x for x in keys if x == pivot]
            right = [x for x in keys if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        sorted_keys = quicksort(list(hmap.keys()))
        pointer = 0

        while k-1-pointer>=0 and sorted_keys[k-1] == sorted_keys[k-1-pointer]:
            pointer += 2
        return hmap[sorted_keys[k-1]][pointer-2:pointer]