num=1234
result=0
n=num
while num>0:
      ld=n%10
      result=(result*10)+ld
      n= n//10

if (n== result):  
   print("palindrome")

else:
    print(result)


          
    

