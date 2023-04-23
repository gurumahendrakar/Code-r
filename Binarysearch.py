<<<<<<< HEAD
# import dataclasses
#
# import numpyy
# import logging
# import time
#
#
# @dataclasses.dataclass(frozen=True,init=True)
# class binary:
#
#     def assending__(self,list_,target_):
# =======
# import numpy
# import logging
# import time
#
# @dataclasses.dataclass
# class binary:
#
#     def One__(self,list_,target_):
# >>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
#
#         assert not target_>list_[-1],'YOur Target is very high brother'
#
#         x,y,z, = 0,len(list_),0
#
#         while True:
# <<<<<<< HEAD
#             print(x,y)
# =======
# >>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
#             z = (x+y)//2
#
#             if target_==list_[z]:
#                 return '__index__ is : {}'.format(z)
#             #target__ = 8
#             if target_<list_[z]:
#                 x,y = 0,z-1
#
#
#             elif target_>list_[z]:
#                 x,y = z+1,y
#
# <<<<<<< HEAD
#             if x==y:
#                 return 'not found !'
#
#
#     def desending__(self,list_,target_):
#
#
#         x,y,z = 0,len(list_),0
#
#         while list_[z]!=target_:
#             z = (x+y)//2
#
#             if list_[z]>target_:
#                 x = z+1
#
#             elif list_[z]<target_:
#                 y = z-1
#
#         else:
#             return ' __index__ : {} '.format(z)
#
#
# b = binary()
# print(b.assending__([1,2,3,4,666,6666,77777,7777777],77777))
# =======
#             if x==z:
#                 return 'not found !'
#
#
# b = binary()
# print(b.One__(list(range(8,55)),8))
# >>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
#
# list = [x for x in range(0,1000,3)]
# print(list)
#
#
# x,y,z = 0,len(list),len(list)//2
# def finder(target):
#
#     global x,y,z
#
#     print(x,y)
#     while list[z] != target:
#
#         z = (x+y)//2
#
#         if target<list[z]:
#             x,y = x,z-1
#         else:
#             x,y = z+1,y
#         if x==z:
#             return 'Not Found'
#
#
#
#     else:
#         return f'target found __index__ is {z}'
#
# founded_element = finder(996)
#
# print(founded_element)
#
import dis
import linecache


s = tuple((1,2,3))
ss = tuple((1,2,3))
#
# print(s.__module__)
#
# print(id(s))
# print(id(ss))
#
# class method:
#     def __init__(self,name,sirname):
#         self.name = name
#         self.sirname = sirname
#
#
#
# s = method("Guru","Mahendrakar")
# ss = method("Guru","Mahendrakar")
#
# print(s,ss,sep='\n')
# def one():
#     a = 8
#
# class method:
#
#     def tool(self):
#         pass
#
#     def tooling(self):
#         pass
#
# print(__build_class__(one,'guru',(method),metaclass=type)())

def so_evel(list,target):

    import time
    a,b = 0,len([1,2,3,4,5])
    while list[(a+b)//2] != target:
        print((a+b)//2)

        if list[(a+b)//2]>target:
            b = ((a+b)//2)-1

        else:
            print('--Hell-LLo--')
            a  = ((a+b)//2)+1
    else:
        return f'__index__ IS {(a+b)//2}'

print(so_evel([1,2,3,4,5,6],4))

from pprint import  pprint
class method:

    s = "Guru"
    def __init__(self):
        pass

    def __class_getitem__(cls, item):
        print(cls)



ss = method()
method['Guru']
=======
import dataclasses
<<<<<<< HEAD
import numpyy
import logging
import time


@dataclasses.dataclass(frozen=True,init=True)
class binary:

    def assending__(self,list_,target_):
=======
import numpy
import logging
import time

@dataclasses.dataclass
class binary:

    def One__(self,list_,target_):
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

        assert not target_>list_[-1],'YOur Target is very high brother'

        x,y,z, = 0,len(list_),0

        while True:
<<<<<<< HEAD
            print(x,y)
=======
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
            z = (x+y)//2

            if target_==list_[z]:
                return '__index__ is : {}'.format(z)
            #target__ = 8
            if target_<list_[z]:
                x,y = 0,z-1
                
            
            elif target_>list_[z]:
                x,y = z+1,y
            
<<<<<<< HEAD
            if x==y:
                return 'not found !'


    def desending__(self,list_,target_):
        

        x,y,z = 0,len(list_),0

        while list_[z]!=target_:
            z = (x+y)//2

            if list_[z]>target_:
                x = z+1

            elif list_[z]<target_:
                y = z-1

        else:
            return ' __index__ : {} '.format(z)

        
b = binary()
print(b.assending__([1,2,3,4,666,6666,77777,7777777],77777))
=======
            if x==z:
                return 'not found !'

                        
b = binary()
print(b.One__(list(range(8,55)),8))
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
