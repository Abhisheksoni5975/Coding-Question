#include<iostream>
using namespace std;
int main()
{
int a[10]=[1,2,4,67,23,26]
int max1=a[0];
int min1=a[0];
int n=sizeof(a);
for(int i=0;i<n;i++)
{
    if(a[i]>a[i+1])
    max1=a[i];
    else if(a[i]<a[i+1])
    min1=a[i];
}
cout<<"Max"<<max1<<<"Min"<<min1;
return 0;
}
