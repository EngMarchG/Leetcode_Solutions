class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = {}
        for word in words:
            hmap[word] = hmap.get(word,0) + 1

        freq = {}
        for key, value in hmap.items():
            if not freq.get(value,0):
                freq[value] = []
            freq[value].append(key)

        hmap = []
        for key in sorted(freq.keys(), reverse=True):
            hmap.extend(sorted(freq[key]))
            if len(hmap)>=k:
                return hmap[:k]
