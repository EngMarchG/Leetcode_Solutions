class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        operation_map = {"C":1, "D":1, "+":1}
        
        for operation in operations:
            if operation_map.get(operation,0) and score:
                if operation == "C":
                    score.pop()
                elif operation == "D":
                    score.append(score[-1]*2)
                else:
                    score.append(score[-1]+score[-2])

            else:
                score.append(int(operation))

        return sum(score)