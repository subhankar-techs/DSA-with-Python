arr = [1,2,3,4,5,6]
n = 15
expected = n*(n+1)//2
actual = sum(arr)
print("Missing numbers: ", expected - actual)