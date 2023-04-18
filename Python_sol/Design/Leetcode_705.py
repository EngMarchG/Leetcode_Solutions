class MyHashSet:

    def __init__(self):
        self.hmap = {}
        

    def add(self, key: int) -> None:
        self.hmap[key] = True

    def remove(self, key: int) -> None:
        self.hmap.pop(key,0)


    def contains(self, key: int) -> bool:
        return self.hmap.get(key,0)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
###