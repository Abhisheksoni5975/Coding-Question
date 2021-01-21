#include<iostream>
using namespace std;

int main()
{
int a=5;
int &r=a;
cout<<a<<"/n"<<r<<endl;
int b=25;
r=b;
cout<<a<<"/n"<<r;
}
