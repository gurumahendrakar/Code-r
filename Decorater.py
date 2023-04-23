
import json
import sys

# Easy Understanding Decorators For Begginners


# Easy Understanding Decorators For Begginners 


# def name_spliter(decorator_1):
#     def circus():
#         name = decorator_1()
#
#         if ' ' in name or '-' in name:
#             yo =name.split(' ')
#
#             hash_indexes = []
#             [hash_indexes.append(yo.index(i)) for i in yo if  '-' in i ]
#
#             print(hash_indexes)
#         for u in range(len(hash_indexes)):
#             yo.insert(hash_indexes[u],'None')
#
#         return hash_indexes
#
#     return circus
#
#
# def Word_capitalize(decorator_2):
#     def Board_():
#         return decorator_2().upper()
#     return Board_
#
#
# @name_spliter
# @Word_capitalize
# def decorator_1():
#     Name = input("Enter Name : ")
#     Sirname = input('Enter Sirname : ')
#     return Name + Sirname
#
# print(decorator_1())
#
# print("Congratus Mission Completed ")



#@wraps with decorators work

# from functools import wraps
# def yellow(toool):
#     @wraps(toool)
#     def yellow2():
#         """Guru Mahendrakar Im Yellow 2"""
#         print(toool.__doc__)
#     return yellow2
# @yellow
# def tool():
#     """Guru Mahendrakar Im Tool """
#     return "Guru Ji Mahendrakar"
#
# print(tool.__name__) # tool ayega @wraps hai bolke @wraps nahi hoga to return kiya so name return hoga




# ----------------------------------------------------Class Decorator________________________________________________________


#
# class Decorator:
#
#     def __init__(self,name):
#         self.name = name
#         self.sirname = "Mahendrakar"
#
#
#     def __call__(self,*args):
#
#         couting = 0
#
#         for i in args:
#
#             if type(i)==int:
#                 couting+=i
#
#             else:
#                 raise ValueError('Int Not Support Calculating ')
#         else:
#             return couting
#
#
# @Decorator
# def calculate():
#     number = 0
#     for i in range(1,8):
#         number+=1
#
#
#     return number
#
# print(calculate(*(1,2,3,4,'-')))




class Decorator:

    def __init__(self,name):

        self.name = name
        self.sirname = "Mahendrakar"


    def __call__(self,*args):
        print(args)
        couting = 0

        for i in args:

            if type(i)==int:
                couting+=i

            else:
                raise ValueError('Int Not Support Calculating ')
        else:
            return couting


# @Decorator
# def calculate():
#     number = 0
#     for i in range(1,8):
#         number+=1
#
#
#     return number
#
# print(calculate())



#important not

#Decorator() -> Call ho raha hai  aur return me (Decorator ka object REturn kar raha hai ) \
# .........................................................Return Object  values pass kar rahe ho __call __ call ho raha hai result de raha hai

#
# class method:
#     def __init__(self):
#         self.name = input("Enter The Name Brother -> ")
#         self.account_ID = int(input("Enter Account Number : "))
#
#         with open('texting.txt','r+') as data_customers:
#             with open('texting.txt') as f:
#                 data = json.load(data_customers)
#                 if data['NAME'] == self.name and \
#                     data['ID']==self.account_ID:
#
#                     print('Welcome To Canara Bank')
#
#                 else:
#                     raise NameError(" NO Account In Canara Bank !!")
#
#
#
# s = method()
# #
# iterable = [1,2,3,4,5]
#
# class selfiterator:
#
#     def __init__(self,iterable,start=0,end=0,step=1):
#         self.iterable = iterable
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.end!=len(self.iterable):
#             x = self.iterable[self.end]
#             self.end+=1
#             return x
#         else:
#             raise StopIteration("Do YOu Have No Extra Elements")
#
#
#
# nex = selfiterator(iterable=iterable)
#
# for xx in nex:
#     print(xx)
# lamba = map(lambda x : x*3,[1,2,3,4,5])
#
# print([x for x in lamba])
# print([x for x in lamba])
