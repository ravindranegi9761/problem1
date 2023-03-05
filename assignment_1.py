# write a python program to get the fibonacci series between 0 to 50


n=9
a=1
b=0
s=1
for x in range(n):
    print(s,end="  ")
    s=a+b
    b=a
    a=s

   
