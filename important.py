# a = [1,2,3,33]
# a.append(1)
# a.insert(0,2)
# a.sort()
# a.remove(33)
# a.clear()
# a.extend([1,2,3])
# a.copy()
# print(a.pop())
# print(a.reverse())
import io
#
#
# class co:
#     def __enter__(self):
#         self.file = open('textin.txt','r')
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         print(exc_type)
#         print(exc_val)
#         print(exc_tb)
#
#         if io.UnsupportedOperation==exc_type:
#             print('--Error Handeled--')
#             return True
# coo = co()
#
#
# with co() as f:
#     print(f.write('g'))



from dataclasses import dataclass


@dataclass(order=True)
class method:
    uou:str
    o:str

u = method(1,3)
uu = method(0,-1)
print(max((u,uu)).o)

