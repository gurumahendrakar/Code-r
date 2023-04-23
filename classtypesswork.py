


import types

a = types.MethodType(function,valueyougive) # return boundmethod class __main__ method
class method:


    def __init__(self):
        print('__called__')
        name = "guru"
        return  method.__init__


    def __new__(cls,name,bases,cdict):


        for key,value in cdict.items():
            if str(value).startswith('<'):
                cdict[key] = types.MethodType(value,cls)

        cls.__init__.__dict__.update(cdict)
        print(cdict)
        return cls.__init__


    def __setattr__(self, key, value):
        print('__Called__')


class method2(metaclass=method):

    def __str__(self):

        return ("King of the world")

    def you(self,a,b):
        print("Hey Bro U Like This",a+b)


u = method2('guru')
print(u.__str__())
print(u.you(2,3))
