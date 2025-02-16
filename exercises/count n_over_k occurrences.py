
from collections import Counter

class Solution:
        """Count More than n/k Occurences"""
        def countOccurence(self,arr,n,k):
            """Function to calculate n/k occurences"""
            # create a dictionarie with dict() to count repetitions of each number
            # using Counter() frm collections
            d = dict(Counter(arr))
            
            # calculate how many elementes appear n/k times
            # setting the result in v
            v = 0
            for value in d.values():
                if (value > n/k):
                    v += 1
            return v

print("Ingrese numeros: ")
arr = list(map(int, input().split()))

n = len(arr)
print("n = ", n)

k = int(input(f"Ingrese k: "))

c = Solution()
s = c.countOccurence(arr,n,k)

print(f"solution is: {s}")



       