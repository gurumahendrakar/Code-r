#
# #     # 1d Array Vector
# #     # 2d matrix
# #     # 3d tensor
# #
# #
# #     # arange = np.arange(0,12).reshape(3,4)
# #     # ndarray = np.array([1,2,3]) # normal list ndarray
# #     # zeros = np.zeros((3,2))
# #     # ones = np.ones((3,2))
# #     # identity = np.identity(6,dtype='int8') # diagonal ones create(only rows give)
# #     # eeye = np.eye(3,4,dtype='int8',order='C') # diagonal ones create method2
# #     # linespace = np.linspace(10,20,10) #(lower,higher,how many numbers)
# #     #
# #     # linespace.view() # (COPY KI TARHA KAAM KARTA HAI BUT AAP ORIGINAL CHANGE KAROGE YE BHI CHANGE HOGA)
# #     # linespace.copy() # Fully Different Object
# #     #
# #     #
# #     # #----------------------------------2nd Video----------------------------------
# #     #
# #     # one_d = np.arange(0,4)
# #     # two_d = np.arange(0,8).reshape(2,4)
# #     # three_d = np.arange(0,9).reshape(3,1,3)
# #     #
# #     #(shape & ndim ) you can use both
# #     # print(one_d.shape) #       (8,)
# #     # print(two_d.shape)#         (2,4)                                           # (3, 1, 3)
# #     # print(three_d.shape)#       (3,1,3)
# #     # print(one_d.ndim) #( return 1 because 1d array) return 1 only
# #     #
# #     # print(two_d.size) # How Many Elements in (two_d array)
# #
# #
# #     # # int-> 4 bytes
# #     # # float -> 8 bytes
# #     #
# #     # print(two_d.dtype) # Andar Konsa Data Store Kiya Hai O return Karega
# #     # print(one_d.itemsize) # output -> 4 (Because Stores Value in List Is Int)
# #     # print(three_d.astype(float)) # Ye Naya Array Ga Naye Object ME floats value daalega
# #     #
# #     #
# #     # # arthemetic operations
# #     #
# #     # print(one_d*two_d)
# #     # print(one_d**two_d)
# #     # print(one_d+two_d)
# #     # print(one_d-two_d)
# #     # #print(one_d-two_d) #devide karte waqt yaad rakha oppisite 0 na ho
# #     #
# #     # print(two_d@one_d) # dot
# #     #
# #     # # boolcomparehension arrays
# #     #
# #     # print(two_d>5)
# #     # print(two_d<5)
# #     # print(two_d>=5)
# #     # print(two_d<=5)
# #     # print(two_d!=5)
# #     # print(two_d==5)
# #     #
# #     #
# #     # #boolen accesing elements in array
# #     #
# #     # print(two_d[(two_d>2) & (two_d%2!=0)])
# #     # print(two_d[(two_d>2) | (two_d%2!=0)])
# #     # print(two_d[(two_d>2) ^ (two_d%2!=0)])
# #     #
# #     #
# #     # print(two_d.min())
# #     # print(two_d.max())
# #     #
# #     # print(two_d)
# #     # # 0 -> Columns 1 -> Rows
# #     # print(two_d.argmax(axis = 0 )) # columns..
# #     # print(two_d.argmin(axis=1)) # rows ...
# #     # print(two_d.sum())
# #     # print(two_d.mean())
# #     # print(np.exp(two_d))
# #     # two_d[:,:] = 1
# #     # two_d.sort()
# #     # print('sorted----',two_d)
# #     #
# #     #
# #     # # Konse bhi array me ho  1d array me convert karta hai
# #     # print(two_d.ravel())
# #     #
# #     # print(three_d)
# #     # print(three_d.transpose()) # (row ka column) (column to row)
# #     #
# #     # print(np.hstack((two_d,two_d))) # rows same hone change columns se farak nahi padta
# #     # print(np.vstack((two_d,[1,2,3,4]))) # v stack me columns matter karenge
# #
# #     # print(np.vsplit(two_d,2)[1]) # rows wise split
# #     # print(np.hsplit(two_d,4)[3]) # columns wise split
# #     #
# #     #
# #     # print(three_d)
# #     #
# #     # three_d[three_d==0] = 1
# #     # #
# #     # #
# #     # print(np.where(two_d%2==0))
# #     #
# # import numpy as np
# # # print(np.unique(['A',"A","A"],
# # #                     return_counts=True,
# # #                     return_index=True))
# #
# #     # a = np.random.random((2, 2))
# #     # b = np.random.rand(3, 2)
# #     # c = np.random.choice([1, 2, 3, 4], size=2)
# #     # d = np.random.randint(0, 8, size=1)
# #     # e = np.random.randn()
# #     # f = np.random._generator.default_rng()
# #     # ff = f.integers(3.2, 8.5, size=5)
# #
# #
# # import  numpy
# # from pprint import pprint
# #
# # # l = np.arange(0,16).reshape(2,2,4)
# # # ll  = np.arange(0,8).reshape(2,4)
# # # print(a)
# # # print()
# # # print(a.transpose())
# # #
# #
# # # print(np.cumsum(ll).reshape(2,4))
# # # print(np.percentile(ll,100))
# # # print(np.histogram(l,bins=[0,10,20,30,40]))
# # # print(np.isin([1,2,3,4,5,6],[1,2,3,4,5]))
# # # print(np.flip(l))
# # # np.put(l,[0,1],[555,1000])
# # # print(np.clip(ll,a_min=2,a_max=3))
# # #
# # # for while import as class def lambda raise return yield try except assert async await and or  in not del is from if elif else true false break local nonlocal
# # # finally paas None
# # # s = np.array([[[4,4,4]],
# # #             [[4,4,4]],
# # #             [[4,4,4]]])
# # #
# # # ss = (np.concatenate((s,[[[1,2,3]],
# # #                          [[3,4,5]],
# # #                          [[7,8,9]]]),axis=1) )
# # #
# # # print(ss)
# # # print(ss.shape)
# # #
# # # sss = np.arange(0,16).reshape(2,8)
# # # print(np.concatenate((sss,[[1,2,3,4],[4,5,6,7]]),axis=1))
# # #
# # # print(np.concatenate(([1,2,3,4],[44,44,44,44]),axis=0))
# # #
# # #
# # #
# # # import numpy as np
# # #
# # # array = np.array([1,2,3,4,5])
# # # arange = np.arange(0,16,2).reshape(2,4)
# # #
# # # o = np.concatenate((arange,[[1,2,3,4],[1,2,3,4]]),axis=1)
# # #
# # #
# # # zeros = np.zeros((3,3)) # saare 1 honge float me
# # # ones = np.ones((3,3)) # saare 1 honge float me
# # #
# # # linspace = np.linspace((3,10),10)
# # #
# # #
# # #
# # # #------------------------------------Random-------------------------------------------------
# # # random = np.random.random((3,3,4))
# # # rand = np.random.rand(3,3)                  # random & rand are same
# # # randint = np.random.randint(0,8,size=(3,3,3))
# # # genrator_int = np.random.random_integers(0,8+1,size=8)
# # # sample = np.random.sample((2,2))
# # # choice = (np.random.choice(genrator_int,size=[2]))
# # # (np.random.bytes(7).decode(encoding='latin-1')) # only latin-1 support
# # #
# # #
# # # list = np.arange(0,8)
# # # shuffle = np.random.shuffle(list) # original me changes honge
# # #
# # #
# # # #-----------------------------------DIOGONAL VALUES-----------------------------------------------------------
# # #
# # # identitty = np.identity(2) # diagonal me 1 aayenge sirf
# # # eye = np.eye(3,5)
# # #
# # #
# # # #--------------------------------IMPORTANT ATTRIBUTES---------------------------------
# # #
# # # array = np.arange(0,8)
# # #
# # # array.size # all elements counting
# # # array.ndim # konsa matrix hai
# # # array.shape # konsa shape
# # # array.itemsize # andar 1 element ka size kitna hai
# # # array.dtype # andar element konse type ka store hai
# # # array = array.astype(dtype='str') # dtype change kar sakte ho perment changes nahi honge
# # #
# # #
# # # #------------------------------IMPORTANT ARRAY OPERATIONS--------------------------------------
# # #
# # #
# # #
# # #
# # # one_d = np.arange(32,40)
# # # two_d = np.arange(0,32).reshape(4,8)
# # # three_d = np.arange(0,16).reshape(2,2,4)
# # #
# # #
# # # # print(np.concatenate((three_d,[[[8,9,10,11],
# # # #                                [12,13,14,15]]]),axis=0))
# # #
# # # # np.random.shuffle(one_d)
# # # #
# # # # (min(one_d))
# # # # (max(one_d))
# # # # (sorted(one_d))
# # # # (reversed(two_d))
# # # # abs(one_d)
# # # # (np.sum(np.arange(0,8).reshape(2,4),axis=1))
# # # # (np.split(two_d,4)) # rows wise spliting
# # # # np.hsplit
# # # # np.vsplit
# # # #
# # # # for x in (np.hsplit(three_d,2)):
# # # #     pass
# # # #
# # # #
# # # # for x in (np.vsplit(three_d,2)):
# # # #     print(x)
# # #
# # #
# # #
# # # # one = np.random.choice(np.arange(300,380,10),size=2)
# # # # one = np.where([[True,True,False,False],[True,True,True,False]],0,array)
# # # # print(one)
# # #
# # # # array = np.arange(0,8).reshape(2,4)
# # # #
# # # # print(np.argwhere(array))
# # # #
# # # # print(np.cumsum(array))
# # #
# # #
# # # o = numpy.array([1,2,3,4,5,6],dtype=np.int32).reshape(2,3)
# # # print(o.strides)
# #
# #
# #
# #
# # #----------------------------------Numpy Starts ----------------------------------------------
# #
# # import sys
# #
# #
# #
# #
# import json
# # array = (np.array([x for  x in range(100)]))
# # print('how many elements in array :',len(array))
# # print('matrix type : ',array.ndim)
# # print('matrix shape :',array.shape)
# # print('element size of array :',array.itemsize)
# # print('How Many elements in array : ',array.size)
# # print('access karne ke kitna dur jayega batayega : ',array.strides)
# # print('element datatype in array :',array.dtype)
# # (array.fill(3)) # Permenent changees in array (jo fill value doge o value pura array me fill karega)
# # zero_array = (np.zeros(shape=(3,5)))
# # (np.fill_diagonal(zero_array,val=1))
# # print(np.full(shape=(2,3),fill_value = 5)
# # print(np.transpose(arrry))
# # print(np.sum(np.arange(0,4).reshape(2,1,2),axis=1))
#
# print(np.linspace([0,3],[3,5]))
# #
# #
# #
# #
# #
# # # string_array = np.arange(0,8).reshape(2,4)
# # # string_array[[0,1]] = [[100,200,300,400],
# # #                      [100,200,300,400]]
# # # print(string_array)
# # # print()
# # #
# # # (string_array[[0,1],[0,3]]) = [20000]
# # # print(string_array)
# # # print()
# # #
# # # string_array[0:2,0:2] = [5000,10000]
# # # print(string_array)
# # # print()
# # #
# # #
# # #
# # # print(np.array([
# # #     [1,2,3,4],
# # #     [1,2,3.5,'guru']
# # # ]))
# # #
# # # foo = np.array([10,20,30,40,50],dtype='str')
# # # print(foo[[np.zeros(shape=(3,),dtype='int')]])
# # # print(np.ones(shape=(3,2),dtype='str'))
# #
#
#
# # to_darray = np.arange(0,12).reshape(3,4)
# # print(to_darray[0,None])
# # print(to_darray>2)
# #
# #
# # th_darray = np.arange(0,8).reshape(2,2,2)
# #
# # daily_routuine  = np.arange(70).reshape(10,7)//2
# # # print(daily_routuine[[0,1],2:4] + daily_routuine[[2,3],2:4])
# #
# # print(th_darray)
# # print(np.sum(th_darray,axis=0))
# # print()
# # print()
# #
# # print()
# #
# # print(np.random.randint([200,500],[300,800],size=(4,2)))
# # print(np.random.randint(0,8,size=(3,4)))
# import sys
#
# import numpy as np
# #
# # array = (np.arange(0,8).reshape(2,2,2))
# # print(array)
# # print()
# # print()
# # print(array+[[3],[4]])
# #
# # print('-----------------------------------------------')
# # o = (np.arange(0,4)[:4,np.newaxis])
# #
# # oo = (np.array([[3,0,6]])[:])
# #
# # print(o,oo)
# # print()
# # print(o+[oo])
# #
# # print()
# # print()
# # print('----------------------------------------------------')
# #
# #
# # array1 = (np.arange(0,8).reshape(2,4))
# # array2 = (np.arange(8,16).reshape(2,4))
# #
# #
# # print(array1,array2,end="\n",sep="\n\n")
# #
# # print('---------------------------------------------------------')
# # print()
# # print()
# # print('--------------------------------------------------------')
# #
# # print(array1+array2)
#
# # print(array1)
# # t = [[True,True,True,True],
# #      [True,False,True,True]]
# #
# # print(array1[np.array(t)])
# #
# #
#
# # Initialisation
# a = np.array([1,2,np.nan,3,5,np.Inf,np.NINF])
# print(a==np.Inf)
# print(np.NINF)
# print(np.isnan(a))
# print(np.isposinf(a))
# print(np.isneginf(a))
#
# # print(np.sum(np.isnan(a)))
#
#
#
# # one_d = np.array([1,2,3,4,5])
# # two_d = np.arange(0,12).reshape(3,4)
# # three_d = np.arange(18).reshape(3,2,3)
# # print(three_d)
# # print()
# # print()
# # print(three_d+[[[10],[20]]])
#
# # a = np.arange(0,8).reshape(2,4)
# # print(a)
# # print(np.concatenate((a,a),axis=1))
# #
# #
# # print()
# # print()
# #
# # print(np.concatenate((three_d,[[[2,3,4]],
# #                                [[2,3,4]],
# #                                [[2,3,4]]]),axis=1))
#
#
# # print(three_d)
# # print(np.sum(three_d,axis=1))
#
#
# #--------------------------------------------------------------------------------------------------------------------------------------------------
#
# # two_d = np.arange(14).reshape(7,2)
# # three_d = np.arange(18).reshape(3,2,3)
#
#
# # a  = np.random.randint(low=1,
# #                        high=7,
# #                        size=3)
#
# # b = np.random.choice(np.arange(0,3),
# #                      size=3,
# #                      replace=False) #replace = False karne se same value nahi return nahi karta hai
#
# # c = (np.random.randint(low=[200,500],
# #                        high=[300,800],
# #                        size=(4,2)))
#
#
#
# # d = (np.random.randint(low=0,
# #                        high=two_d.shape[0],
#
#
# #                        size=(2,)))
#
#
# #
# # e = np.random.uniform(low=200,
# #                       high=500,
# #                       size=(2,2,3))
#
# print()
#
# # f = (np.random.choice(a=10,
# #                       size=(2,3)))
#
# # genrator = np.random.default_rng(seed=222)
# # g = genrator.integers(low=0,
# #                       high=8,
# #                       size=8)
#
# a = [1,2,3,4]
# # h = np.random.shuffle([1,2,3,4])
# # print(h)
#
# #
# # i = np.random.random_sample((2,2,3)) # genrate random numbers
# # print(i)
#
# # j = np.random.sample([1,2])
# # print(j)
# # #---------------------------------------------------------------------------------------------------------------------------------------------------
#
# # a = abs = np.abs([0,0,0,0,5,4,3,2,0,np.NAN])
# # b = nonzero = abs.nonzero() # jaha pe zero nahi hai oske index return karta hai
#
#
#
# # c = np.where(abs==0,3,[100,200,300,400,500,600,700,800,900,1000])
#
#
#
# # d = (np.array_equal([1,2,3,3],[1,2,3,3])) # dono array same hai ya nahi
#
# # e = np.sum(abs)
#
# # print(np.all(np.isnan(a)))
#
# # print(np.concatenate((a,a),axis=0))
#
# # print(np.sort(a))
#
# # np.random.shuffle(two_d) # its changes in real array
#
# # print(np.sort(two_d))
#
# # print(np.argsort(two_d,axis=0))
#
#
# # print(np.argmax(two_d))
#
# # print(np.argmin(two_d))
#
# # print(np.unique([1,1,2,3,3,4,5,6,7]))
#
# # print(np.round([3.2,3.3,5.3,4.5,5.7]))
#
# # print()
# #
# # one_d = np.array([x for x in range(8)])
# # array = np.arange(0,32).reshape(4,2,4)
# # array2 = np.arange(33,33+16).reshape(4,1,4)
# # append = np.append(array,[[[1,2,3,4],[5,6,7,8]]],axis=0)
# #
# # print(array)
# # print(array2)
# #
# # # one_d = np.insert(array,0,array2,axis=0)
# # # print(one_d)
# #
# # a = [[[5,8,9,3],[5,3,2,1]],[[53,2,21,8],[7,8,9,5]]]
# # print(np.unique(a))
#
#
#
# import numpy as np
#
#     # 1d Array Vector
#     # 2d matrix
#     # 3d tensor
#
#
#     # arange = np.arange(0,12).reshape(3,4)
#     # ndarray = np.array([1,2,3]) # normal list ndarray
#     # zeros = np.zeros((3,2))
#     # ones = np.ones((3,2))
#     # identity = np.identity(6,dtype='int8') # diagonal ones create(only rows give)
#     # eeye = np.eye(3,4,dtype='int8',order='C') # diagonal ones create method2
#     # linespace = np.linspace(10,20,10) #(lower,higher,how many numbers)
#     #
#     # linespace.view() # (COPY KI TARHA KAAM KARTA HAI BUT AAP ORIGINAL CHANGE KAROGE YE BHI CHANGE HOGA)
#     # linespace.copy() # Fully Different Object
#     #
#     #
#     # #----------------------------------2nd Video----------------------------------
#     #
#     # one_d = np.arange(0,4)
#     # two_d = np.arange(0,8).reshape(2,4)
#     # three_d = np.arange(0,9).reshape(3,1,3)
#     #
#     #(shape & ndim ) you can use both
#     # print(one_d.shape) #       (8,)
#     # print(two_d.shape)#         (2,4)                                           # (3, 1, 3)
#     # print(three_d.shape)#       (3,1,3)
#     # print(one_d.ndim) #( return 1 because 1d array)
#     #
#     # print(two_d.size) # How Many Elements in (two_d array)
#     #
#     #
#     # # int-> 4 bytes
#     # # float -> 8 bytes
#     #
#     # print(two_d.dtype) # Andar Konsa Data Store Kiya Hai O return Karega
#     # print(one_d.itemsize) # output -> 4 (Because Stores Value in List Is Int)
#     # print(three_d.astype(float)) # Ye Naya Array Ga Naye Object ME floats value daalega
#     #
#     #
#     # # arthemetic operations
#     #
#     # print(one_d*two_d)
#     # print(one_d**two_d)
#     # print(one_d+two_d)
#     # print(one_d-two_d)
#     # #print(one_d-two_d) #devide karte waqt yaad rakha oppisite 0 na ho
#     #
#     # print(two_d@one_d) # dot
#     #
#     # # boolcomparehension arrays
#     #
#     # print(two_d>5)
#     # print(two_d<5)
#     # print(two_d>=5)
#     # print(two_d<=5)
#     # print(two_d!=5)
#     # print(two_d==5)
#     #
#     #
#     # #boolen accesing elements in array
#     #
#     # print(two_d[(two_d>2) & (two_d%2!=0)])
#     # print(two_d[(two_d>2) | (two_d%2!=0)])
#     # print(two_d[(two_d>2) ^ (two_d%2!=0)])
#     #
#     #
#     # print(two_d.min())
#     # print(two_d.max())
#     #
#     # print(two_d)
#     # # 0 -> Columns 1 -> Rows
#     # print(two_d.argmax(axis = 0 )) # columns..
#     # print(two_d.argmin(axis=1)) # rows ...
#     # print(two_d.sum())
#     # print(two_d.mean())
#     # print(np.exp(two_d))
#     # two_d[:,:] = 1
#     # two_d.sort()
#     # print('sorted----',two_d)
#     #
#     #
#     # # Konse bhi array me ho  1d array me convert karta hai
#     # print(two_d.ravel())
#     #
#     # print(three_d)
#     # print(three_d.transpose()) # (row ka column) (column to row)
#     #
#     # print(np.hstack((two_d,two_d))) # rows same hone change columns se farak nahi padta
#     # print(np.vstack((two_d,[1,2,3,4]))) # v stack me columns matter karenge
#
#     # print(np.vsplit(two_d,2)[1]) # rows wise split
#     # print(np.hsplit(two_d,4)[3]) # columns wise split
#     #
#     #
#     # print(three_d)
#     #
#     # three_d[three_d==0] = 1
#     # #
#     # #
#     # print(np.where(two_d%2==0))
#     #
#     # print(np.unique(['A',"A","A"],
#     #                 return_counts=True,
#     #                 return_index=True))
#     #
#     # a = np.random.random((2, 2))
#     # b = np.random.rand(3, 2)
#     # c = np.random.choice([1, 2, 3, 4], size=2)
#     # d = np.random.randint(0, 8, size=1)
#     # e = np.random.randn()
#     # f = np.random._generator.default_rng()
#     # ff = f.integers(3.2, 8.5, size=5)
#
#
# import  numpy
# from pprint import pprint
#
# # l = np.arange(0,16).reshape(2,2,4)
# # ll  = np.arange(0,8).reshape(2,4)
# # print(a)
# # print()
# # print(a.transpose())
# #
#
# # print(np.cumsum(ll).reshape(2,4))
# # print(np.percentile(ll,100))
# # print(np.histogram(l,bins=[0,10,20,30,40]))
# # print(np.isin([1,2,3,4,5,6],[1,2,3,4,5]))
# # print(np.flip(l))
# # np.put(l,[0,1],[555,1000])
# # print(np.clip(ll,a_min=2,a_max=3))
#
#
# #--------------------------------------------------------------------------
#
#
# import numpy as np
#
# array = np.arange(0,8,).reshape(2,4)

# print(array.shape)
# print(array.ndim)
# print(array.dtype)
# print(array.strides)
# print(array.size)
# print(array.itemsize)
# print(array.strides)
# print(np.linspace(0,8,num=3))
# print(np.full(3,fill_value=8))
# print(np.transpose(array))
# print(np.sum(array))
# print(array.fill(3))
# (np.fill_diagonal(array,3))

#
# one_d = np.array([1,2,3,4,5,6,7,8])
# two_d = np.array([1,2,3,4,5,6,7,8]).reshape(2,4)
# three_d = np.array(np.arange(0,12).reshape(2,1,6))

#
# print(one_d.shape)
# print(two_d.ndim)
# print(two_d.dtype)
# print(two_d.strides)
# print(two_d.astype('int64'))
# print(two_d.size)
# print(two_d.itemsize)
# print(np.fill_diagonal([[1,2,3,4],
#                         [5,6,7,8]],"Guru"))
# print(two_d.fill(3))

# print(two_d.transpose())
# print(np.linspace([0,3],[8,9]))
# print(np.cumsum(two_d))
# print(sum(np.arange(0,8).reshape(2,4)))




# string_array = np.arange(0,8).reshape(2,4)

# string = string_array[[0,1],[0,1]] = [8,7]

# print(string_array[[0,1],:1])


# print(three_d[1])

# print(np.zeros((2,4),dtype=np.int64))


# print(np.ones((2,4),dtype=np.int64))

# print(two_d[:2,0])


# ==================import random========================================

import numpy as np
# io = np.random.randint(0,8,size=(3,2))
# print(io)
#
#
# ioo = np.random.choice([1,2,3,4,5],size=(3,4))
# print(ioo)
#
#
# iooo = np.random.rand()
# print(iooo)
#
#
# ioooo = np.random.random_sample()
# print(ioooo)
#
#
# iooooo = np.random.random(size=(3,2))
# print(iooooo)

# print(two_d+[[1],[2]])

#
# ioooooo = np.random.uniform(0,8,size=(2,3))
# print(ioooooo)


a = np.array([1,2,3,4,5,6])
# print(np.nonzero(a))



# print(np.where(a==0,3,2))

# print(np.random.shuffle(np.array([1,2,3,4,5])))

# print(a)


# print(np.vstack((a)))
# print(np.hstack((a,a,a)))
two_d = [[1,8,3,2],
         [7,8,0,1]]
# print(np.all([1,2,3,4,5]))
# print(np.any([1,2,3,4,45]))
# print(np.sort(two_d))
# print(np.argsort(two_d,axis=0))


# print(np.argmax(two_d))

# print(np.unique([0,2,3,2,2,3,0]))

#
# x = (two_d.insert(1,[1,2,3,4]))
# print(two_d)


# xx = np.append(two_d,[[1,2,3,4]],axis=0)
# print(xx)


# print(np.identity(5))
#
# print(np.eye(2,3))

#
# print(np.random.shuffle([1,2,3,4,5]))

# print(np.round([1,2,3.5]))

# a = np.array([1,2,3,4])
# b = a.copy()
# a[0] = 8
# print(b)

#
# # print(np.isnan([1,2,3,np.nan]))
# b = (np.isposinf([[1,2,3,np.Inf,np.NINF]]))
# print(np.isneginf([1,2,3,np.NINF]))

import keyword
from pprint import pprint as print
print(keyword.kwlist)

"""
size itemsize ndim shape dtype astype fill full transpose linspace random shutffle nan round abs copy identity eye vstack hstack concatinate
strides fill_diagonal pass none 

python keywords 

def lambda class while for and or not in is if elif else  continue break assert del try except else with from import as True False None Pass
finally pass none global nonlocal raise 


def lambda class while for and or not in is try exeplect finally true false break continue yeile return with from import as assert 
del  if elif else 




def lambda class while for and or not in is try excpet finally if elif else true flase none paas assert raise global nonlocal with from import as return yeild raise continue break
list 
tuple dict set string float int frozenset


arthemetic
assignment operators
relational operators
membership operators 
logical operators 
bitwise operators
identity operators

name index colums is_unique shape keys 
"""




#
# a = np.arange(0,12).reshape(3,4)
# print(np.append(a,[[35,5,6,6]],axis=0))


# two_d = np.arange(20).reshape(4,5)
#
# two_d_slice = two_d[[0,1,2,3],[[0,1,2,3]]] = np.arange(1000,5000,1000)
# print(two_d)

