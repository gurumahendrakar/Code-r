<<<<<<< HEAD
# from functools import (lru_cache,total_ordering,singledispatch,singledispatchmethod,partialmethod)
=======
 __from functools import (lru_cache,total_ordering,singledispatch,singledispatchmethod,partialmethod)
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd


#------------------------------------------------singledispatch--------------------------------------------------
# class functool:
#
#     @singledispatchmethod
#     def tool(self):
#         pass
#
#     @tool.register(list)
#     def _(self,list):
#         print(list)
#
#     @tool.register(int)
#     def _(self,a,b):
<<<<<<< HEAD
#         print(a+b)
=======
#         pass
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
#
#     @tool.register(str)
#     def  _(self,a):
#         print(a)
<<<<<<< HEAD


# a = functool()
# a.tool([1,2,3],1) # jo pehle type ka doge o ose function pe jayega
=======
#
#
# a = functool()
#
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd

#---------------------------------------------total_ordering-----------------------------------------------------------
#
# @total_ordering
# class functool:
#
#     def __init__(self):
#         self.computer = 0
#         self.me = 100
#
#     def __eq__(self, other):
#         return self.me == other.me
#
#     def __lt__(self, other):
#         return  self.me < other.me
#
#
# b = functool()
# c = functool()
# c.me = 200
# print(b<c)
# print(b>c)
# print(b<=c)
# print(b>=c)
# print(b!=c)
# print(b==c)
#
#

# #============================================lru_cache=================================================================
# import time
# class functool:
#
#     @lru_cache()
#     def __bigdata(self,param):
#         print('__called__')
#         time.sleep(3)
#         print('__Finished__',param)
#
#
# c = functool()



#-------------------------------------------------partial----------------------------------------------------------

<<<<<<< HEAD
# class method:
#
#     def __init__(self):
#         self.one = 'guru'
#         self.tool = method._tool(3,)
#
#     @partialmethod
#     def _tool(self,a,b):
#         return 'Your Result -- ',a+b
#
#
# a= method()
# a.tool(3)
#
# from pprint import  pprint as print
# import  builtins
#
# name = "Doreamon --Main Global Scope---"
#
import builtins
from pprint import pprint as print

class global_local():
    name = 'Guru Class MEthod'


    def func(self):
        hi = "Nobita Method Func"
        # print(globals())
        builtins.print()
        builtins.print()
        # print(locals())

check_ = global_local()
check_.func()


def addition(self,a,b):
    c = 'Guru'
    print(a+b)


=======
class method:

    definit__(self):
        self.one = 'guru'
        self.tool = method._tool

    @partialmethod
    def _tool(self,a,b):
        return 'Your Result -- ',a+b


a = method()
print(a.tool(a,3,))
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
