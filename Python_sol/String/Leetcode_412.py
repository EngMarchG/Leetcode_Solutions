class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = ["0"] * n
        for num in range(1, n+1):
            num_end = int(str(num)[-1])
            ans = ""
            if num % 3 == 0:
                ans += "Fizz"
            if num_end == 0 or num_end == 5:
                ans += "Buzz"
            
            if ans:
                output[num-1] = ans
            else:
                output[num-1] = str(num)

        return output