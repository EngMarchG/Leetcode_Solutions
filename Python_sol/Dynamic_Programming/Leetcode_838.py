# Another solution would use 2 pointers where the 2nd pointer is the closest non "." 
# value after the 1st pointer

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        hmap = {}
        dominoes = [x for x in dominoes]
        
        def move(direction, pos, rank):
            side = 1
            if direction == "L":
                side *= -1
            pos += side
            dominoes[pos] = direction
            hmap[pos] = rank
            rank += 1
            return rank, pos
            
        def decision(direction, pos, rank):
            side = 1
            opp = "L"
            if direction == "L":
                side *= -1
                opp = "R"
            pos += side
            if dominoes[pos] == opp:
                if hmap.get(pos, 0) < rank:
                    return 0
                if hmap.get(pos, 0) == rank:
                    dominoes[pos] = "."
                    return 0
            elif dominoes[pos] == direction:
                return 0
            return 1
        
        for pos, num in enumerate(dominoes):
            rank = 1
            if num == "L":
                while pos > 0 and decision(num, pos, rank):
                    rank, pos = move(dominoes[pos], pos, rank)
           
            elif num == "R":
                while pos < len(dominoes) - 1 and decision(num, pos, rank):
                    rank, pos = move(dominoes[pos], pos, rank)
                    
        return "".join(dominoes)

            """Non dry sol
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        hmap = {}
        dominoes = [x for x in dominoes]
        
        def move(direction, pos, rank):
            side = 1
            if direction == "L":
                side *= -1
            pos += side
            dominoes[pos] = direction
            hmap[pos] = rank
            rank += 1
            return rank, pos
            
        # def decision(direction, rank):
        # I will have to check the return val anw
        
        for pos, num in enumerate(dominoes):
            rank = 1
            if num == "L":
                while pos > 0:
                    if dominoes[pos-1] == "R":
                        if hmap.get(pos-1, 0) < rank:
                            break
                        elif hmap.get(pos-1, 0) == rank:
                            dominoes[pos-1] = "."
                            break
                    elif dominoes[pos-1] == "L":
                        break
                    rank, pos = move(dominoes[pos], pos, rank)
           
            elif num == "R":
                while pos < len(dominoes) - 1:
                    if dominoes[pos+1] == "L":
                        if hmap.get(pos+1, 0) < rank:
                            break
                        elif hmap.get(pos+1, 0) == rank:
                            dominoes[pos+1] = "."
                            break
                    elif dominoes[pos+1] == "R":
                        break
                    rank, pos = move(dominoes[pos], pos, rank)
                    
        return "".join(dominoes)
            """