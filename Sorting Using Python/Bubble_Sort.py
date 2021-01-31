#Bubble Sorting Algorithms 
#List Definition
a=[1,2,0,8,3,6,4,5,8,7]
#Swapping element position and doing n operation
for j in range(0,len(a)):
    for i in range(0,len(a)-j-1):
        if(a[i]>a[i+1]):
            a[i],a[i+1]=a[i+1],a[i]
print(a)
