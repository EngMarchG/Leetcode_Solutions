class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hmap = {}
        for path in paths:
            hmap[path[0]] = path[1]

        for path in paths:
            for city in path:
                if not hmap.get(city, 0):
                    return city 