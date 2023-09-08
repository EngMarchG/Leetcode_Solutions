class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        if numRows == 1:
            return arr
        
        arr.append([1,1])
        if numRows == 2:
            return arr

        for num in range(3, numRows+1):
            arr.append([1])
            for pos in range(1,num):
                if pos != num-1:
                    arr[num-1].append(arr[num-2][pos-1]+arr[num-2][pos])
                else:
                    arr[num-1].append(1)
        
        return arr
    
### Sol 2
# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         arr = [[1]]
#         if numRows == 1:
#             return arr
        
#         arr.append([1,1])
#         if numRows == 2:
#             return arr

#         for num in range(3, numRows+1):
#             arr.append([1])
#             for pos in range(1,num):
#                 if pos != num-1:
#                     arr[num-1].append(arr[num-2][pos-1]+arr[num-2][pos])
#                 else:
#                     arr[num-1].append(1)
        
#         return arr