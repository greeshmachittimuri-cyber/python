#n=int(input())990
#for i in range (1,n+1):
#   if i[0]==i[n-1]:
#      print("palindrome")
a=1234
num=a 
result=0
while num>0:
    ld=a%10
    result=(result*10)+ld
    num=num//10
    if a==result:
       print("palindrome")
    

