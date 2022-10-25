class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        if n == 1:
            
            return start
        
        elif n == 2:
            
            return(start + 2)
        
        else:
        
            arr = []

            for i in range(n):

                arr.append(start + 2 * i)


            result = arr[0] ^ arr[1]

            for i in range(1, len(arr) - 1):

                result ^= arr[i + 1]

            return result