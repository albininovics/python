def largest(arr,n):
   
   max = arr[0]
   for i in range(1, n):
      if arr[i] > max:
         max = arr[i]
   return max

arr = [10, 24, 45, 90, 98]
n = len(arr)
b = largest(arr,n)
print ("Largest in the given array is",b)