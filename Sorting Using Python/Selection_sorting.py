#Selection Sorting Algorithms 
#List Definition
a=[1,2,0,8,3,6,4,5,8,9]
#Loop for swapping two element
for i in range(0,len(a)):
    m=len(a)
    for j in range(i+1,m):
        if(a[i]>a[j]):
             a[i],a[j]=a[j],a[i]
print(a)
