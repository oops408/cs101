from fractions import Fraction as f
a=int(input());b=int(input())
if a==0:print(0)
elif b==1:print(a)
elif a%b:print(a//b,f(a%b,b))
else:print(a//b)