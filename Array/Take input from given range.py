# Create list of numbers with given range

r1= int(input()) # by default input function take string to use as inter use typecasting int(input())
r2=int(input())
a=[]
if(r1==r2):
   print(r1)
else:
   while(r1<=r2):
      a.append(r1)
      r1=r1+1
print(a)    
