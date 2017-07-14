#include<stdio.h>
#include<conio.h>
void main()
{
 int n,i;
 int f,b,fd,bd,t,c=0,tc=0;
 clrscr();
 printf("enter no of test cases ");
 scanf("%d",&n);
 if(n>=1 && n<=100)
 {
  printf("f b t fd bd\n");
  for(i=0;i<n;i++)
  {
   scanf("%d %d %d %d %d",&f,&b,&t,&fd,&bd);
   if(fd>0 && bd>0 &&  t>0 && f>0 && b >0)
   {
     if(f>=fd)
     {
     c=fd*t;
     printf("output:%d F\n",c);
     }
     else if(f==b)
     {
     printf("output:NO Ditch\n");
     }
     else if(f>b)
     {
     while(!0)
     {
      tc=tc+f;
      c=c+f;
      if(c>fd) break;
      c=c-b;
      tc=tc+b;
     }
     tc=tc-(c-fd);
     printf("output:%d F\n",tc*t);
     }
     else
     {

     while(!0)
     {
      tc=tc+f;
      c=c-f;
      if(c>bd) break;
      c=c+b;
      tc=tc+b;
     }
     tc=tc-(c-bd);
     printf("output:%d B\n",tc*t);
     }
   }
  }
 }
}
