def digital_root(n):
    s1=0
    while(n>9):
        s=n%10
        s1=s1+int(s)
        n=n//10
    if(n>0):
        s1=s1+n
    if(s1>9):
        x=digital_root(s1)
        return(x)
    else:
        return(s1)
n=int(input())
x=digital_root(n)
print("The sum of digits is ---", x)