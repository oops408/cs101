class MyType(type): pass 

class SubType(MyType): pass 

class MyObject(object): 
 __metaclass__ = MyType 

print("MyType.__class__ = %s" % (MyType.__class__)) 
print("SubType.__class__ = %s" % (SubType.__class__)) 
print("MyObject.__class__ = %s" % (MyObject.__class__))