n=input(" ")#checking a string id palindrome or not using while loop
l,r=0,len(n)-1
while l<r:
    if n[l]!=n[r]:
        print("not palindrome")#time complexity=o(n/2)==>o(n),sc=o(1)
        break
    l=l+1
    r=r-1
else:    
    print("palindrome")#checking a string is pplindrome or not using slice
s=input(" ")
if s==s[::-1]:
    print("palindrome")
'''
'''num=1234
result=0#checking number is palindrome or not without converting into string
n=num
while num>0:
      ld=n%10
      result=(result*10)+ld
      n= n//10

if (n== result):  
   print("palindrome")

else:
    print(result)
'''

          
    
