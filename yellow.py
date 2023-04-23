import numpy as np

#
# array = np.array([x for x in range(8)]).reshape(4,2)
# # print(array.ndim)
# # print(array.shape)
# # print(array.dtype)
# # print(array.size)
# # print(array.itemsize)
# # print(array.strides)
# # (array.fill('Guru'))
# # print(array.astype())
# print(array.ravel())
# print(array.transpose())
#
# # print(np.histogram(array,bins=[0,10,20,30]))
# print(np.full([2,3],fill_value="Guru"))
#
# array = [np.nan,np.Inf,np.NINF]
#
# print(np.isnan(array))
# print(np.isposinf(array))
# print(np.isneginf(array))


x = np.arange(8)
print(np.delete(x,x%2==0))