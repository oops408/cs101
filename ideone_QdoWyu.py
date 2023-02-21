from fractions import Fraction as f
a=int(input());b=int(input())
if a==0:print(0)
else:
  print(a//b,f(a%b,b))