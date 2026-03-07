def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(10))

a=1
b=int(input())
for i in range(1,b):
    b=b*i
print(b)
    
    
