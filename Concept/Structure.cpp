#Get area of rectangle using structure
#include<iostream>
using namespace std;
struct rectangle
{
  float length;
  float breadth;    /* data */
};
int main()
{
    struct rectangle r1; 
    
    r1.length=12;
    r1.breadth=23;
    cout<<"Area is "<<r1.length*r1.breadth<<" Of rectangle"<< "with length "<<r1.length<<"Breadth "<<r1.breadth;
        
    
    
}
/* padding is concept of structure where it use the memory for character same as of interger but at the 
time of using charcter it will use the real memery required by char */
