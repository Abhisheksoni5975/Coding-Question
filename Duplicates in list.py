#How do you find the duplicate number on a given integers
a=[1,2,2,4,1,7,7,8,85,8]
unique_list=[]
x=len(a)
for i in range(x):
    k=i+1
    for j in range(k,x):
        if(a[i] == a[j] ):
            unique_list.append(a[i])
print(unique_list)
