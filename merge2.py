def mctFromLeafValues(self,arr):
        ans = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                ans += min(arr[minIndex - 1], arr[minIndex + 1]) * arr[minIndex]
            else:  #handle corner cases : when minimun value is either first value or last value of the list
                ans += arr[1 if minIndex == 0 else minIndex - 1] * arr[minIndex]
            arr.pop(minIndex)
        return ans # OR return arr[0]
arr=[10,20,30]
self=[]
print(mctFromLeafValues(self,arr)) 
   