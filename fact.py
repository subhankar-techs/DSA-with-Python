num=int(input("Enter the number which factorial you want:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial of",num,"is",fact)
