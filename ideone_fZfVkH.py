from decimal import *
a,b=input().split()
l,r=a.split('.')
p=len(a[a.index('.')+1:])
b=int(b);a=str(int(l+r)**b)
t=str((10**p)**b);idx=len(a)-len(t)+1
if idx<0:print('0.'+'0'*(-idx)+a)
else:print(a[:idx]+'.'+a[idx:])