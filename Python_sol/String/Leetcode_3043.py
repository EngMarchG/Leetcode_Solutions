class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()

        for num in arr1:
            num_str = str(num)
            for length in range(1, len(num_str) + 1):
                prefix = num_str[:length]
                prefix_set.add(prefix)

        max_prefix_length = 0

        for num in arr2:
            num_str = str(num)

            for length in range(len(num_str), 0, -1):
                prefix = num_str[:length]
                if prefix in prefix_set:
                    if length > max_prefix_length:
                        max_prefix_length = length
                    
                    break

        return max_prefix_length