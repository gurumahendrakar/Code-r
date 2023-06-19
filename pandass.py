# # # # # # # #
# # # # # # # # import csv
# # # # # # # # import random
# # # # # # # #
import numpy
import numpy as np
import pandas as pd
# # # from pprint import pprint
# # # # # # # # series  = pd.Series(['a','b','c','d','e','f','g','h'])
# # # # # # # #
# # # # # # # #
# # # # # # # # marks = [50,100,150,200]
# # # # # # # # subjets = ['maths','social','hindi','computer science']
# # # # # # # # series2 = pd.Series(marks,index=subjets)
# # # # # # # # from pandas import Series as panda,read_csv
# # # # # # # #new
# # # # # # # #
# # # # # # # # #...........................................................pandas.Series..................................................................
# # # # # # # #
# # import sys
# #
# names = ['Guru','Chetan',"Pravin","Gundya","Ajay"]
# dict = {'Guru':"Mahendrakar",
#         'Pandas':"Python",
#         "Python":"WebDevelopment",
#         'Python':'Fucking'}
# data = pd.Series(data=dict)
# # import numpy as np
# # import pandas as pd
# #
# print(data.name)
# print(data.size)
# print(data.describe())
# print(data.keys())
# # # # # # # #
# data2 = pd.DataFrame([5,53,2,2,0,1],index=[3,5,3,2,1,5])
# # print(data2.sort_values(data2))
# print(data2.sort_index())
# print(data2.nunique())
# print(data2.round())
# print(data2.cumsum())
# print(data2.transpose())
# # print(data2.iloc[3])
# print(data2.iloc[1]) #
# # # # # # # #
# # # # # # # # # print(data.name)
# # # # # # # # # print(data.size)
# # # # # # # # # print(data.dtype) # object I Dont Know Y not return datatype
# # # # # # # # # print(data.is_unique)
# # # # # # # # # print(data.axes) # #indexs return in list
# # # # # # # # # print(data.dtype) # return object
# # # # # # # # # print(data.flags)
# # # # # # # # # print(data.index) # returning indexs
# # # # # # # # # print(data.keys()) # return keys
# # # # # # # # # print(data.values) # return values
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # #-------------------------------Read-csv-------------------------------------------------
# # # # # # # # #
# # # # # # # # # csvdata = read_csv('S:/csvfiles/data.csv', encoding='latin-1',squeeze=panda)
# # # # # # # # # # print(csvdata['industry'].tail(10))
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # dict_ = {'name':'Guru','sirname':"Mahedrakar",'College':'CB college Bhalki'}
# # # # # # # # # series3 = pd.Series(dict_,name='Guru Details')
# # # # # # # # # print(series3)  # (indexs auto matic setted with dict keys)
# # # # # # # #
# # # # # # # #
# # # # # # # # #
# # # # # # # # # print(series3.size) # 1 row me kitne colums hai
# # # # # # # # # print(series3.index) # return accesing indexs names
# # # # # # # # # print(series3.array) # return values
# # # # # # # # # print(series3.dtype) return what is datatype
# # # # # # # #
# # # # # # # # #print(series3.name)
# # # # # # # # # print(series3.values) # all columns values
# # # # # # # # # print(series3.values)
# # # # # # # # # print(series3.unique())
# # # # # # # # # print(series3.describe()) # all details of file how many rows and filesize etc.
# # # # # # # #
# # # # # # # # print('------------------------')
# # # # # # # # # read_csv = pd.read_csv('S:/csvfiles/bollywood.csv',index_col='movie',squeeze=True) # Squeeze = dataframe ko series me convert karna
# # # # # # # # # read_csv.info()
# # # # # # # # # print(read_csv.dtypes) #column konse object ki bani huvi hai means (float int str(object,"<U0")
# # # # # # # # #
# # # # # # # # # print(read_csv.head(5))
# # # # # # # # # print(read_csv.tail(5))
# # # # # # # # # print(read_csv.sample(6)) # random COLUMS DETA HAI
# # # # # # # #
# # # # # # # # # print(series3.value_counts()) # NAMES KO COUNT KARKE BATA SAME NAME KITNE BAAR REPEAT HUVA HAI
# # # # # # # # # print(series3.sort_values(ascending=False)) # ALPHABETIC SORTING
# # # # # # # #
# # # # # # # # # print(series3.values)
# # # # # # # #
# # # # # # # # # print(read_csv)
# # # # # # # # #
# # # # # # # # # (read_csv.sort_index(inplace=True)) # index sorting with alphabetic
# # # # # # # # #
# # # # # # # # # print(read_csv)
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(read_csv.count())
# # # # # # # # # print(read_csv.sum())
# # # # # # # # # print(read_csv.min())
# # # # # # # # # print(read_csv.max())
# # # # # # # #
# # # # # # # # # print(read_csv[read_csv.values[0][0]])
# # # # # # # #
# # # # # # # # # print(read_csv[5:8])
# # # # # # # #
# # # # # # # # # print(read_csv[-5:])
# # # # # # # #
# # # # # # # # # print(read_csv[[0,1,2]])
# # # # # # # # # print(read_csv[0])
# # # # # # # #
# # # # # # # # # read_csv['sst'] = "cool"
# # # # # # # # # read_csv[0] = "Guru Mahendrakar"
# # # # # # # # # print(read_csv.tail())
# # # # # # # # # print(read_csv.head())
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(len(read_csv)) # how many rows
# # # # # # # # #
# # # # # # # # # print(sorted(read_csv))
# # # # # # # # # print(min(read_csv))
# # # # # # # # # print(max(read_csv))
# # # # # # # # # print(reversed(read_csv))
# # # # # # # #
# # # # # # # # # read_csv.plot()aadfdfadf
# # # # # # # #
# # # # # # # # #comparision also works same as kkk+fcadfdf\
# # # # # # # #
# # # # # # # #
# # # # # # # # # in not in also works
# # # # # # # #
# # # # # # # #
# # # # # # # # series = pd.Series([['guru','pravin','ketan'],
# # # # # # # #                     ['mahendrakar','mahendrakar','biradar'],
# # # # # # # #                     [39,33,35]],index=[1,2,3])
# # # # # # # #
# # # # # # # # # print(series.size) # columns size giving
# # # # # # # # # print(series.values)
# # # # # # # #
# # # # # # # #
# # # # # # # # dict_series = pd.Series({"name":"Guru",
# # # # # # # #                          "sirname":"Mahendrakar",
# # # # # # # #                          "Rolno":'39'
# # # # # # # #                          },
# # # # # # # #                         name='names') # dict provide karne ke baad index specify mat karo nahi int or float NAN hojate hai
# # # # # # # #
# # # # # # # # # print(dict_series.is_unique) # saare columns nahi diffrent honge to True dega ek bhi same huva to false dega
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(dict_series.iloc[0]) # only indexs paas
# # # # # # # #
# # # # # # # # # print(series.loc)  # only string index for use nahi to error dega
# # # # # # # #
# # # # # # # #
# # # # # # # # # print(series.shape)
# # # # # # # # # print(series.values)
# # # # # # # # # print(series.index)
# # # # # # # # # print(dict_series.rename({'name':"Guru"},inplace=True))
# # # # # # # #
# # # # # # # # # a = pd.Series([1,2,3])
# # # # # # # # # # print(dict_series['name'])
# # # # # # # # # # print(dict_series[-1])
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # print(a.sample())
# # # # # # # # # print(dict_series.sample(2))
# # # # # # # # dict_series[0] = "SHUBHASH CHOWK"
# # # # # # # #
# # # # # # # # # print(dict_series[[0,1]])
# # # # # # # # # print(min(dict_series))
# # # # # # # # # print(max(dict_series))
# # # # # # # # # print(sorted(dict_series))
# # # # # # # # # print(reversed(dict_series))
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # #------------------------------------------------------------------------------------------------------------
# # # # # # # # #
# # # # # # # # # dataframe = pd.read_csv('S:/csvfiles/bollywood.csv')
# # # # # # # # # print(dataframe.head(2))
# # # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # # dataframe = pd.DataFrame(data=[['GURU','MAHENDRAKAR','2019'],
# # # # # # # # #                                ['HEYMAN','NOWDAYS','BEFORE']],
# # # # # # # # #                          columns=['NAME','SIRNAME','YEAR'])
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # #
# # # # # # # # # with open('csvv.csv','w+',newline='') as file:
# # # # # # # # #     csv_writer = csv.writer(file,)
# # # # # # # # #     csv_writer.writerow(['NAME','SIRNAME','ROLLNO','ID'])
# # # # # # # # #
# # # # # # # # #     for x in range(1000):
# # # # # # # # #         csv_writer.writerow(['Guru','Mahendrakar',x,np.nan])
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # csvfile = pd.read_csv('csvv.csv',index_col='NAME')
# # # # # # # #
# # # # # # # # # print(csvfile.cumsum())
# # # # # # # # # print(csvfile.get('ID'))
# # # # # # # # # print(csvfile)
# # # # # # # # # print(csvfile.transpose())
# # # # # # # #
# # # # # # # #
# # # # # # # # # print((csvfile.values=="Mahendrakar").sum())
# # # # # # # #
# # # # # # # # # print(csvfile.sort_values('ID'))
# # # # # # #
# # # # # # # #
# # # # # # # # import pandas as pd
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # # names = ['Guru',"Mahendrakar",'Pravin','Gundya']
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # for x in range(3):
# # # # # # # # #     dict_ = {'name':"Guru",
# # # # # # # # #              "sirname":5,
# # # # # # # # #              "rolno":39}
# # # # # # # # #     seriess = pd.Series(dict_,name='details')
# # # # # # # # #
# # # # # # # #
# # # # # # # # # print(seriess.values)
# # # # # # # # # print(seriess.keys())
# # # # # # # # # print(seriess.index)
# # # # # # # # # print(seriess.loc['name'])
# # # # # # # #
# # # # # # # # #
# # # # # # # # # print(seriess.size)
# # # # # # # # # print(seriess.dtype)
# # # # # # # # # print(seriess.index)
# # # # # # # # # print(seriess.is_unique)
# # # # # # # # # print(seriess.values)
# # # # # # # # # print(seriess.keys())
# # # # # # # # # print(seriess.name)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # import numpy as np,pandas as pd
# # # # # # #
# # # # # # read_csv = pd.read_csv('S:/csvfiles/bollywood.csv',squeeze=True)
# # # # # # # # print(read_csv['movie'].name)
# # # # # # #
# # # # # # # # print(np.sum([read_csv['lead']=='Akshay Kumar']))
# # # # # # # #
# # # # # # # # print(read_csv.head(5))
# # # # # # # # print(read_csv.tail(5))
# # # # # # # # print(read_csv.keys())
# # # # # # # # print(read_csv.head(5))
# # # # # # # # print('\n\n')
# # # # # # # #
# # # # # # # # data = dict.fromkeys(['name','sirname','rollno'],'Guru')
# # # # # # # # seriess = pd.Series(data=[data,data])
# # # # # # # #
# # # # # # # # print(read_csv.keys())
# # # # # # # # print(seriess.keys())
# # # # # # # # print(seriess)
# # # # # # #
# # # # # #
# # # # # # a = {'name':1,
# # # # # #      'kill':5,
# # # # # #      'king':3,
# # # # # #      'yellow':3,
# # # # # #      'king':np.NAN}
# # # # # #
# # # # # # #
# seriess = pd.Series(a)
# print(seriess.astype('int32'))
# #
# print(np.array([1,2,3,4,5]).strides)
# print(seriess[seriess.between(1,2)])
# print(seriess.clip(0,6)) # nan ko chokar sab 5 hojayenge
# print(seriess.drop_duplicates(keep='last'))
# print(seriess.duplicated())
# # print( ( read_csv[read_csv=='Akshay Kumar']).isnull().sum())
# print(seriess.dropna())
# print(seriess.fillna(0))
# print(seriess[seriess.isin([2,3])])
# # print(read_csv['movie'].apply(lambda x:x.upper()))
# print(seriess.mean())
# print(seriess.apply(lambda  x: "Good Day" if x>2 else "Guru" ))
# print(seriess.shape)
# # print(read_csv.dtypes)
# # # # #
# # # # # # # # dataframe = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5]])
# # # # # # # # # print(dataframe.shape)
# # # # # # # # # print(dataframe.loc[1])
# # # # # # # # print(dataframe.columns)
# # # # # # # # print(dataframe)
# # # # # # #
# # # # # # #
# # # # # # # names = ['Guru','Chetan',"ketan","Gundya"]
# # # # # # # marks = [33,22,22,5]
# # # # # # #
# # # # # # # dict_ = {
# # # # # # #     'maths':57,
# # # # # # #     'english':67,
# # # # # # #     'science':22,
# # # # # # #     'light':33
# # # # # # # }
# # # # # # #
# # # # # # #
# # # # # # # series = pd.Series(data=dict_,name="names")
# # # # # # #
# # # # # # # # print(series.size) # series me column kitne hai count karke batayega
# # # # # # # # print(series.name)
# # # # # # # # print(series.is_unique) # saare columns different hai to true nahi to false
# # # # # # # # print(series.values)    # saare values miljayenge
# # # # # # # # print(series.dtype)
# # # # # # # # print(series.index)
# # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # # read_csv = pd.read_csv('S:/csvfiles/bollywood.csv'
# # # # # # # #                        ,index_col='movie',
# # # # # # # #                        squeeze=True)
# # # # # # #
# # # # # # #
# # # # # # # # print(read_csv.head())
# # # # # # # # print()
# # # # # # # # print()
# # # # # # # # print(read_csv.tail(5))
# # # # # # # # print()
# # # # # # # # print()
# # # # # # # # print(read_csv.sample(5))
# # # # # # #
# # # # # # # # print(read_csv['movie'].value_counts(ascending=True))
# # # # # # # #
# # # # # # # # print(read_csv['movie'].sort_values())
# # # # # # # # print(read_csv.sample(6).sort_index())
# # # # # # #
# # # # # # # # print(read_csv.info())
# # # # # # # # print(read_csv.describe())
# # # # # # # #
# # # # # # # # print(read_csv.count())
# # # # # # # # print(read_csv.min())
# # # # # # # # print(read_csv.max())
# # # # # # # # print(read_csv.cumsum())
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # # print(read_csv.describe())
# # # # # # #
# # # # # # # #
# # # # # # # # series = pd.Series([555,333,200,100],
# # # # # # # #                    index=[1,2,3,4])
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # #indexing
# # # # # # #
# # # # # # # # print(series[[1,2]].astype('str'))
# # # # # # #
# # # # # # # # print(len(series))
# # # # # # # # print(min(series))
# # # # # # # # print(max(series))
# # # # # # # # print(sorted(series))
# # # # # # # #
# # # # # # # # print()
# # # # # # #
# # # # # # #
# # # # # # # #--------------------DataFrame----------------------------
# # # # # # #
# # # # # # #
# # # # # # # # student_data = [[1000,2000,3000],
# # # # # # # #                 [3333,4444,5555],
# # # # # # # #                 [6666,7777,8888]]
# # # # # # # #
# # # # # # # #
# # # # # # # # # dataframe =  pd.DataFrame(data=student_data)
# # # # # # # # # print(dataframe[0]>200)
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # import time
# # # # # #
# # # # # # import pandas as pd
# # # # # # data_ = pd.read_csv('S:/csvfiles/diabetes.csv')
# # # # # # # # data_2 = data_[['Pregnancies','BloodPressure']]['BloodPressure']
# # # # # # #
# # # # # # # # print(((data_2>80) & (data_2<85)).sum())
# # # # # #
# # # # # # import numpy as np
# # # # # # d = pd.DataFrame(
# # # # # # #
# # # # # #     data= [
# # # # # #
# # # # # #                        [1,2,3,4,5,3],
# # # # # #                        [1,2,3,4,5,3],
# # # # # #                        [1,2,3,4,5,np.NAN]
# # # # # #
# # # # # #                         ],index=[1,2,3],
# # # # # #                  columns=['one','two','three','four','five','king']
# # # # # #
# # # # # # )
# # # # # #
# # # # # #
# # # # # # # # attributes
# # # # # #
# # # # # #
# # # # # # # # print(d.shape)
# # # # # # # # print(d.dtypes)
# # # # # # # # print(d.index)
# # # # # # # # print(d.size)
# # # # # # # # print(d.columns)
# # # # # # # # print(d.values)
# # # # # # # # print(d.head())
# # # # # # # # print(d.tail())
# # # # # # # # print(d.describe())
# # # # # # # # print(d.count())
# # # # # # #
# # # # # # #
# # # # # # # # print(d.isnull().sum())
# # # # # # # # print(d.duplicated())
# # # # # # # # (d.drop_duplicates(inplace=True))
# # # # # # # # print(d)
# # # # # # #
# # # # # # # #
# # # # # # # # (d.rename(columns={'one':'guru','two':"Lol"},inplace=True))
# # # # # # # # print(d.sum())
# # # # # # #
# # # # # # # # print(d.sum(axis=0))
# # # # # # # print(d.min())
# # # # # # # print(d.)
# # # # # #
# # # # # # # print(data_.columns)
# # # # # # # print(data_.head(5))
# # # # # # # print(data_.iloc[0:3,2])
# # # # # # # print(data_.loc[0:2,'Age'])
# # # # # # # # print(data_['Age'].between(2,23).sum())
# # # # # # # print(data_['Age'].apply(lambda x:x+200))
# # # # # #
# # # # # #
# # # # # # # print("%s--%s--%i" %("Guru","King",3))
# # # # # #
# # # # # # # print(d.rename(columns={'one':'one-two-three'}))
# # # # # # # print(d.drop_duplicates())
# # # # # # # print(d.isnull())
# # # # # # # print(d.describe())
# # # # # # # print(d.info())
# # # # # #
# # # # # #
# # # # # #
# # # # # # import itertools
# # # # # # #
# # # # # # # o = time.time()
# # # # # # # two = time.time()
# # # # # # # for x in (itertools.count(0,8)):
# # # # # # #     if x==13318216:
# # # # # # #         break
# # # # # # #
# # # # # # # print(time.time()-o)
# # # # # # #
# # # # # # # for x in range(13318217):
# # # # # # #     if x==13318216:
# # # # # # #         break
# # # # # #
# # # # # #
# # # # # #
# # # # # # # print(time.time()-two)
# # # # # # import itertools,sys
# # # # # #
# # # # # #
# # # # # # # print(itertools.count) # while loop ki tarha
# # # # # # # xx = (itertools.islice('Guru',3))
# # # # # # # print(sys.getsizeof(itertools.chain([x for x in range(10000)])))
# # # # # # #
# # # # # # # print(sys.__stdout__.write("guru"))
# # # # # #
# # # # # #
# # # # # # # def fun(a,b):
# # # # # # #     print(a,b)
# # # # # # # print(sys.call_tracing(fun,('Guru',"Mahendrakar")))
# # # # # # #
# # # # # # # print(itertools.chain([[1,2,3,4,5,7],[8,9,10]]))
# # # # # # #
# # # # # # # for x in (itertools.accumulate([1,2,3,4,5])):
# # # # # # #     print(x)
# # # # # #
# # # # # # #
# # # # # # # x = pd.read_csv('S:/csvfiles/movies.csv')
# # # # # # # print(x.columns)
# # # # # # # o = ((x['genres'].apply(lambda xx:xx.startswith('Action|'))))
# # # # # # # i = x[o]['imdb_rating']>7.5
# # # # # # #
# # # # # # # print(i.sum())
# # # # # # #
# # # # # # # ii = x['title_x'] = 'india'
# # # # # # # print(x)
# # # # # #
# # # # # #
# # # # # #
# # # # # # # series attributes
# # # # # # """
# # # # # # SIZE
# # # # # # INDEX
# # # # # # VALUES
# # # # # # NAME
# # # # # # UNIQUE_ID
# # # # # # DTYPE
# # # # # #
# # # # # # VALUE_COUNTS
# # # # # #
# # # # # # """
# # # # # import csv
# # # # # import dis
# # # # # import functools
# # # # # import os
# # # # # import sys
# # # # #
# # # # # import pandas as pd,numpy as np
# # # # # #--------------------------------------Series-------------------------------------------------
# # # # # # import pandas as pd,numpy as np
# # # # # # series = pd.Series(data=['Guru','Guru','Pravin','Mahendrakar'])
# # # # # # print(series.size)
# # # # # # print(series.dtypes)
# # # # # # print(series.index)
# # # # # # print(series.values)
# # # # # # print(series.is_unique)
# # # # # # print(series.name)
# # # # # #
# # # # # # print(series.value_counts())
# # # # # # print(series.sort_index())
# # # # # # print(series.sort_values())
# # # # # # print(series.sample())
# # # # # # print(series.drop_duplicates())
# # # # # # print(series.duplicated())
# # # # # # print(series.describe())
# # # # # # print(series.count())
# # # # # # print(series.min())
# # # # # # print(series.max())
# # # # # # print(sorted(series))
# # # # # # print(series.sum())
# # # # # # print(series[series=='Guru'])
# # # # #
# # # # # #---------------------------------------DATAFRAME--------------------------------------------------------
# # # # # #
# # # # # # read_csv = pd.read_csv('S:/csvfiles/movies.csv')
# # # # # # print(read_csv.shape)
# # # # # # print(read_csv.dtypes)
# # # # # # print(read_csv.columns)
# # # # # # print(read_csv.index)
# # # # # # print(read_csv.columns)
# # # # # # print(read_csv.head())
# # # # # # print(read_csv.tail())
# # # # # # print(read_csv.sample())
# # # # # # print(read_csv.info())
# # # # # # print(read_csv.rename(columns={'title_x':'uiop'},inplace=True))
# # # # # # print(read_csv.head(2))
# # # # # # print(read_csv.head(5)[:])
# # # # # # print(read_csv.duplicated())
# # # # # # print(read_csv.iloc)
# # # # # # print(read_csv.loc)
# # # # #
# # # # #
# # # # #
# # # # # #------------------------------------------------------------------
# # # # #
# # # # # #
# # # # # #
# # # # # # )
# # # # #
# # # # #
# # # # # # print(d.fillna("Guru"))
# # # # # # print(d.dropna())
# # # # # # print(d.isnull())
# # # # # # print(d)
# # # # # # print(d.drop('king'))
# # # # # # print(d.count())
# # # # # # print(d.clip(3,5))
# # # # # # print(d.isin([5]))
# # # # #
# # # # #
# # # # # #-----------------------------------------------------------------------------------------------
# # # # #
# # # # # # read_csv = pd.read_csv('S:/csvfiles/ipl-matches.csv')
# # # # # #
# # # # # #
# # # # # # with open('texting.txt') as fi-le:
# # # # # #     a = csv.DictReader(file)
# # # # # #     for x in a:
# # # # # #         print(x['name'])
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # print(read_csv.value_counts().plot(kind='pie'))
# # # # #
# # # # #
# # # # # # print(read_csv[''])
# # # # # #
# # # # # # d = pd.DataFrame(
# # # # # # #
# # # # # #     data= [
# # # # # #
# # # # # #                        [33,2,3,4,5,3],
# # # # # #                        [55,2,3,4,5,3],
# # # # # #                        [555,2,3,4,5,np.NAN]
# # # # # #
# # # # # #                         ],index=[1,2,3],
# # # # # #                  columns=['one','two','three','four','five','king'])
# # # # #
# # # # # # print(d['one'].rank(ascending=False))
# # # # # # print(d.set_index('one',inplace=True))
# # # # # # print(d['two'][555])
# # # # # # print(d.reset_index(inplace=True))
# # # # # # print(d['one'])
# # # # #
# # # # #
# # # # # # print(d['one'].unique())
# # # # #
# # # # # # print(d['one'])
# # # # # # x = (d['one'].apply(lambda x:x>55))
# # # # #
# # # # # # print(d['one'][x])
# # # # #
# # # # # #
# # # # # #
# # # # # # """
# # # # # # name
# # # # # # index
# # # # # # is_unique
# # # # # # values
# # # # # # dtype
# # # # # # size
# # # # # #
# # # # # # sort_values
# # # # # # value_counts
# # # # # # sort_index
# # # # # # sample
# # # # # # iloc
# # # # # # loc
# # # # # # drop_dublicates()
# # # # # # duplicate()
# # # # # # describe
# # # # # # min
# # # # # # max
# # # # # # sum
# # # # # #
# # # # # #
# # # # # #
# # # # # # shape
# # # # # # head
# # # # # # tail
# # # # # # fillana
# # # # # # dropna
# # # # # # fill
# # # # # # d.clip
# # # # # #
# # # # # # """
# # # # # # with open('texting.txt','w') as file:
# # # # # #     for _ in range(10):
# # # # # #         file.write('Guru,Mahendrakar,22\n')
# # # # #
# # # # #
# # # # # #
# # # # # # read_  = pd.read_csv('texting.txt',
# # # # # #                      header=None,
# # # # # #                      names=['Name',"Sirname","Rollno"],
# # # # # #                      na_values= {'Name':"Guru",
# # # # # #                                  "Rollno":22},
# # # # # #                      nrows=3,
# # # # # #
# # # # # #                      )
# # # # # #
# # # # # # (read_.to_csv('neww.csv',
# # # # # #                    index=False,
# # # # # #                    columns=['Name'],
# # # # # #                    header=False)\
# # # # # #  )
# # # # # #
# # # # # #
# # # # # # print(dff.to_excel('new.xlsx',sheet_name='stocks'))
# # # # # #
# # # # # #
# # # # # # df1 = pd.DataFrame([['Guru',"Mahendrakar",32],
# # # # # #                     ["Ajay","Kushwah",29]])
# # # # # #
# # # # # # df2 = pd.DataFrame([["Prajwal","Sangppa",23],
# # # # # #                     ["Chetan","Suryawanshi",22]])
# # # # # #
# # # # # #
# # # # # # with pd.ExcelWriter('stocks_weatherrr.xlsx') as writer:
# # # # # #     df1.to_excel(writer,sheet_name='stock')
# # # # # #     df1.to_excel(writer,sheet_name='stock2')
# # # # # #
# # # # # # """
# # # # # # Index(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
# # # # # #        'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome'],
# # # # # #       dtype='object')
# # # # # # """
# # # # #
# # # # #
# # # # # # dff = pd. \
# # # # # #     read_excel(r"C:\Users\mahen\Downloads\file_example_XLS_10.xls",
# # # # # #                "Sheet1",
# # # # # #                converters=
# # # # # #                      {'First Name':lambda name: "Dulce" if name=="Dulce" else None},
# # # # # #                parse_dates=['First Name'])
# # # # # #
# # # # # #
# # # # # # # print(dff.fillna(np.NAN).info())
# # # # # #
# # # # # #
# # # # # # # print(dff.fillna({'First Name':0,}))
# # # # # #
# # # # # # print(dff.fillna(method='bfill',axis='columns',limit=1))
# # # # #
# # # # #
# # # # data = pd.DataFrame({'mumbai':[100,1000,np.NAN,1000,2000,2000,np.NAN,2000,3000],
# # # #                      'newyork':[1000,1100,1200,1300,1400,1500,np.NaN,1700,1800],
# # # #                      'bidar':[2000,2100,2200,2300,2400,np.NAN,np.NAN,8000,np.NAN],
# # # #                      'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # #                              'paris','paris','newyork','newyork']},
# # # #                     index=['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE'])
# # # # #
# # # # # # (data.fillna({
# # # # # #     'mumbai':'not avilable',
# # # # # #     'newyork':'newyork',
# # # # # #     'bidar':'Paris',
# # # # # #     'city':'KingOfLaw'
# # # # # # },inplace=True))
# # # # # #
# # # # # # print(data['newyork'])
# # # # #
# # # # # # iloc integersaaaa
# # # # # # loc string_'columns'
# # # # #
# # # # #
# # # # # # print(data.fillna(method='ffill',limit=2)) # bfill & ffill use pichecwali ya aage wali value fill karega
# #
# # # # # #
# # # # # #
# # # # # # print(data.replace(np.NAN,{'mumbai':'no weather',
# # # # # #                            'newyork':'no value',
# # # # # #                            'bidar':'happy life',
# # # # # #                            'city':'kingLife'}))
# # # # #
# # # # # #
# # # # # # print(data.replace({100:10000,
# # # # # #                     np.NINF:'Guru'}))
# # # # #
# # # # #
# # # # #
# # # # # # print(data.replace(['\w{0,4}'],' ',regex=True))
# # # # #
# # # # # #
# # # # # # data_ = pd.DataFrame([['Newyork',22,55],
# # # # # #                       ['Gulbarga',22,55],
# # # # # #                       ['Bidar',22,55],
# # # # # #                       ['Bhalki',22,55],
# # # # # #                       ['Mumbai',22,55]],columns=['City',
# # # # # #                                                'Tempreture',
# # # # # #                                                'Percentage'])
# # # # # #
# # # # # #
# # # # # #
# # # # # # data_2 = pd.DataFrame([['Banglore',22,55],
# # # # # #                       ['Ghost',22,55],
# # # # # #                       ['Ninddein',22,55],
# # # # # #                       ['Likever',22,55],
# # # # # #                       ['Coffe',22,55]],columns=['City',
# # # # # #                                                'Tempreture',
# # # # # #                                                'Percentage'])
# # # # # #
# # # # # # df = (pd.concat([data_,data_2],
# # # # # #                 ignore_index=True,
# # # # # #
# # # # # #                 keys=['one','two']))
# # # # # #
# # # # # #
# # # # # #
# # # # # # data_2 = pd.DataFrame([['Banglore',22,55],
# # # # # #                       ['Ghost',22,55],
# # # # # #                       ['Ninddein',22,55],
# # # # # #                       ['Likever',22,55],
# # # # # #                       ['Coffe',22,55]],columns=['City',
# # # # # #                                                'Tempretur',
# # # # # #                                                'Percentage'])
# # # # # #
# # # # # #
# # # # # # print(pd.concat([data_,data_2],
# # # # # #                 axis=0,
# # # # # #                 ignore_index=True))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # def fun(*args,**kwargs):
# # # # # #
# # # # # #     x = 8
# # # # # #     name = "Guru"
# # # # # #     sirname = "Mahendrakar"
# # # # # #     rollno = 39
# # # # # #
# # # # # #     return "Do Yoou Like Me!!"
# # # # # #
# # # # # #
# # # # # # o = fun
# # # # # # o.__dict__['name'] = "guru"
# # # # # # print(o.__dict__['name'])
# # # # # #
# # # # # #
# # # # # # import itertools
# # # # # #
# # # # # # groupp = itertools.groupby('aabcdefghijklabcd')
# # # # # #
# # # # # # for x,y in groupp:
# # # # # #     print(x,list(y))
# # # # #
# # # # # #
# # import time
# #
# # import matplotlib.pyplot as plt
# # import pandas as pd
# # #
# #
# # set_ = pd.DataFrame({'city':['newyork','chicago','brazil','brazil',],
# #                      'tempreture':[100,200,300,400],
# #                      'huminity':[10,20,30,40],
# #                      'ages':[10,20,30,40]
# #                      })
# #
# # set_2 = pd.DataFrame({'city':['newyork','brazil','san francisco','Sexo','newyork'],
# #                      'huminit':[10, 20,30,40,80],
# #                       'tempreture':[100,200,300,400,500]})
#
#
#
# # print(set_.groupby('city'))
# print(pd.merge(set_,set_2,on='city',how='outer'))
# # print()
# # print()
# # print(pd.merge(set_,set_2,on='huminity',how='outer'))
# # print(pd.merge(set_,set_2,on='city',how='right'))
#
# # # # #
# # # # # """
# # # # # #
# # # # #        #left
# # # # #        city  tempreture  huminity
# # # # # 0  newyork         100      80.0
# # # # # 1  chicago         200      10.0
# # # # # 2  orinado         300       NaN
# # # # # 3   brazil         400      20.0
# # # # #
# # # # #
# # # # #             #outer
# # # # #             city  tempreture  huminity
# # # # # 0        newyork       100.0      80.0
# # # # # 1        chicago       200.0      10.0
# # # # # 2        orinado       300.0       NaN
# # # # # 3         brazil       400.0      20.0
# # # # # 4  san francisco         NaN      30.0
# # # # # 5           Sexo         NaN      40.0
# # # # #
# # # # #         # right
# # # # #     city  tempreture  huminity
# # # # # 0        chicago       200.0        10
# # # # # 1         brazil       400.0        20
# # # # # 2  san francisco         NaN        30
# # # # # 3           Sexo         NaN        40
# # # # #
# # # # # """
# # # # #
# df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
#                            '5/3/2017','5/1/2017','5/2/2017','5/5/2017'),
#                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
#                     'bejing','bejing','bejing'),
#                    'humidity':(56,58,np.NAN,80,83,85,26,30,35),
#                    'tempreture':(65,66,68,75,78,82,80,77,79)})
#
#
# # print(df.unstack().unstack().unstack())
# print(df)
# data = (df.melt(id_vars=['city']))
# #
# # print(data[ (data.city=="newyork") & (data.variable=="date")])
#
# print(data)


# # # # # # print(df.count())
# # # # # # print(df)
# # # # # # # print()
# # # # # # # print()
# # # # # # # print()
# # # # # # print(df.pivot(index='date',columns='city',values=['humidity']))
# # # # # #
# # # # # # print()
# # # # # # print()
# # # # # # print()
# # # # # #
# # # # # # for x,y in (df.groupby('date')):
# # # # # #     print(x,y)
# # # # #
# # # # #
# # # # # # print(df,end='\n\n\n')
# # # # # print(df.pivot_table(index='date',aggfunc='count',margins=True))
# # # # # # print(df.pivot_table(index='date',aggfunc='count'))
# # # # #
# # # # # #
# # # # # # df['date'] = pd.to_datetime(df['date'])
# # # # # #
# # # # # # print(df['date'])
# # # # # # print(df.pivot_table(index=pd.Grouper(key='date'),columns='city'))
# # # # # #
# # # #
# # # # #
# # # # # df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
# # # # #                            '5/3/2017','5/1/2017','5/2/2017','5/5/2017'),
# # # # #                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
# # # # #                     'bejing','bejing','bejing'),
# # # # #                    'humidity':(56,58,60,80,83,85,26,30,35),
# # # # #                    'tempreture':(65,66,68,75,78,82,80,77,79)},)
# # # # # # #
# # # # # # for io in (df.groupby('city')):
# # # # # #     print(io)
# # # # #
# # # # #
# # # # #
# # # # # # print(df.pivot(index='date',columns='city'),end='\n\n\n')
# # # # # #
# # # # # # print(df.pivot(index='date',columns='humidity'))
# # # # #
# # # # # set_1 = pd.DataFrame({'city':['chicago','brazil','san francisco'],
# # # # #                      'huminity':[10, 20,10],
# # # # #                       'tempret':[70,200,300],
# # # # #                       'tempreture':[70,200,300]},dtype=np.int64)
# # # # #
# # # # #
# # # # #
# # # # # # for io,ioo in (set_2.groupby('huminity')):
# # # # # #     print(io)
# # # # # #     print(ioo)
# # # # #
# # # # #
# # # # # # set_2.iloc[0,1] = pd.NA
# # # # #
# # # # # import math
# # # # #
# # # # # # print(math.sqrt(2))
# # # # # # print(math.ceil(2.5))
# # # # # # print(math.floor(2.5))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #
# # # # # # print(set_2[(set_2.tempreture.apply(lambda x:x<74))])
# # # # #
# # # # # #
# # # # # # set_2 = pd.DataFrame({'city':['chicago','brazil','san francisco'],
# # # # # #
# # # # # #                       'tempret':[70,200,300],
# # # # # #                       'tempretu':[70,200,300],
# # # # # #                       'tempretur':[80,200,300]},dtype=np.int64)
# # # # # #
# # # # # #
# # # # # # print(pd.concat([set_1,set_2],keys=['first','second'],axis=1)['second'])
# # # # # #
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # #
# # # # # # students_data = pd.read_csv('S:/csvfiles/students.csv')
# # # # # # regx = pd.read_csv('S:/csvfiles/reg-month2.csv')
# # # # # #
# # # # # #
# # # # # # group = (students_data.groupby('name'))
# # # # # # (students_data)
# # # # #
# # # # # # data = (pd.concat([students_data,pd.DataFrame([['Chhavi Lachman',18,23],['Elias Dodiya',25,16]],
# # # # # #                                             columns=['name','partner','student_id'])],ignore_index=True))
# # # # #
# # # # # # print(data.value_counts(ascending=True))
# # # # #
# # # # # #inner join
# # # # # # outer join
# # # # # #left join
# # # # # # right join
# # # # #
# # # # #
# # # # # # print(students_data)
# # # # # # del students_data['partner'][24]
# # # # # #
# # # # # # print(students_data)
# # # # #
# # # # #
# # # # # # print(pd.merge(students_data,regx))
# # # # #
# # # # # # print(students_data.head(5))
# # # # # # print(regx)
# # # # #
# # # # # # print(pd.merge(students_data,regx,on='student_id'))
# # # # #
# # # # # #
# # # # # # one_d = pd.DataFrame({'names':['Guru','Mahendrakar','Pravin',"Chetan","Gundya"],'marks':[1,2,3,4,5]})
# # # # # # two_d = pd.DataFrame({'names':['Guru','Mahendrakar','Pravin',"Chetan","Gundya"],
# # # # # #                       'marks':[1,2,3,4,5],
# # # # # #                       'student_id':[22,33,44,55,66]})
# # # # # # print(one_d)
# # # # # # one_d['student_id'] = (one_d['marks']  + two_d['student_id'])
# # # # # # print(one_d)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # #
# # # # # #
# # # # # # data = pd.DataFrame({'mumbai':[100,1000,np.NAN,1000,2000,2000,np.NAN,2000,3000],
# # # # # #                      'newyork':[1000,1100,1200,1300,1400,1500,np.NaN,1700,1800],
# # # # # #                      'bidar':[2000,2100,2200,2300,2400,np.NAN,np.NAN,8000,np.NAN],
# # # # # #                      'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # # # #                              'paris','paris','newyork','newyork']},
# # # # # #                     index=['ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE'])
# # # # # #
# # # # # #
# # # # # #
# # # # # # print(data.groupby('city').agg(['min','max','sum','mean']))
# # # # #
# # # # # # def funs(name):
# # # # # #     print('like me ',name)
# # # # # # def name(function):
# # # # # #     return (function())
# # # # # # @funs
# # # # # # @name
# # # # # # def fun():
# # # # # #     return ('-----fun---------'.strip('-'))
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # class uiop:
# # # # # #
# # # # # #     def __init__(self):
# # # # # #         self.start = 0
# # # # # #         self.end = 8
# # # # # #
# # # # # #
# # # # # #
# # # # # #     def __iter__(self):
# # # # # #         return self
# # # # # #
# # # # # # a = pd.Series(np.arange(5))
# # # # # #
# # # # # # print(pd.concat([a,a],axis=1))
# # # # #
# # # # #
# # # # # # one_df = pd.DataFrame([[1,2,3],
# # # # # #                       [6,7,8]])
# # # # #
# # # # #
# # # # # # two_df = pd.DataFrame([[9,10,11,12],
# # # # #                        # [12,13,14,12]])
# # # # #
# # # # #
# # # # # # print(pd.concat([one_df,two_df],axis=1,ignore_index=True))
# # # # # #
# # # # # #
# # # # # # data = pd.DataFrame({'mumbai':[100,1000,2000,1000,2000,2000,3333,2000,3000],
# # # # # #                      'newyork':[1000,1100,1200,1300,1400,1500,2222,1700,1800],
# # # # # #                      'bidar':[2000,2100,2200,2300,2400,2222,5555,8000,9000],
# # # # # #                      'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # # # #                              'paris','paris','newyork','newyork']},)
# # # # # #
# # # # # #
# # # # # #
# # # # # # data2 = pd.DataFrame({'mumbai':[100,1000,2000,1000,2000,2000,3333],
# # # # # #                      'newyork':[1000,1100,1200,1300,1400,1500,2222],
# # # # # #                      'bidar':[2000,2100,2200,2300,2400,2222,5555],
# # # # # #                       'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # # # #                              'paris','paris']
# # # # # #                      })
# # # # # #
# # # # # #
# # # # # # print(pd.merge(data,data2,how='inner',on='city'))
# # # # # # #
# # # # # # #
# # # # # # # print(pd.merge(data,data2,on='city'))
# # # # # #
# # # # # #
# # # # # # print(pd.merge(df1,df2,how='inner',on='city'))
# # # # #
# # # # #
# # # # # #
# # # # # #
# # # # # # df1 = pd.DataFrame({
# # # # # #     'city':['new york','chicago','orinado'],
# # # # # #     'tempreture':[21,14,35]})
# # # # # #
# # # # # #
# # # # # # df2 = pd.DataFrame({
# # # # # #     'city': ['chicago','new york','san francisco'],
# # # # # #     'tempreture':[100,200,300],
# # # # # #     'humidity':[65,68,75]
# # # # # # })
# # # # # #
# # # # # #
# # # # #
# # # # #
# # # # # #
# # # # # # df1 = pd.DataFrame({'name':['Guru',"Mahendrakar","TAppu"],
# # # # # #                     'sirname':['Mahendrakar','Mahendrakar',"Mahendrakar"],
# # # # # #                     0:['Guruu','Nitinn',"Likeever"]})
# # # # # # df2 = pd.DataFrame({'name':['Guru','Nitin',"Tappu"],
# # # # # #                     'sirname':['mahendrakar','mahendrakar','mahendrakar'],
# # # # # #                     0:['one','two','three'],
# # # # # #                     1:['four','five','six'],
# # # # # #                     2:['six','seven','eight']})
# # # # # #
# # # # # # print(pd.concat([df1,df2]))
# # # # #
# # # # # #
# # # # # # data = pd.DataFrame({'mumbai':[100,1000,2000,1000,2000,2000,3333,2000,3000],
# # # # # #                      'newyork':[1000,1100,1200,1300,1400,1500,2222,1700,1800],
# # # # # #                      'bidar':[2000,2100,2200,2300,2400,2222,5555,8000,9000],
# # # # # #                      'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # # # #                              'paris','paris','newyork','newyork']},)
# # # # # #
# # # # # #
# # # # # #
# # # # # data2 = pd.DataFrame({'mumbai':[100,1000,2000,1000,2000,2000,3333],
# # # # #                      'newyork':[1000,1100,1200,1300,1400,1500,2222],
# # # # #                      'bidar':[2000,2100,2200,2300,2400,2222,5555],
# # # # #                       'city':['bhalki','bhalki','bhalki','bhalki','paris',
# # # # #                              'paris','paris']
# # # # #                      })
# # # # # #
# # # # # # #
# # # # # #
# # # # # # df_1 = pd.DataFrame({
# # # # # #     'citys':['mumbai','newyork','bhalki','bidar'],
# # # # # #     'tempreture':[25,22,18,15],
# # # # # #     'grounds':['chennai_ground','Player_ground',"Saare_Ground","TAlle_Ground"],
# # # # # #
# # # # # # })
# # # # # #
# # # # # #
# # # # # # df2 = pd.DataFrame({
# # # # # #
# # # # # #     'tempreture':[17,18,25,15],
# # # # # #     'date':['5/2/2023','11/2/2023','15/3/2023','20/4/2023'],
# # # # # #     'citys':['Likever','mumbai','mumbai','bidar']
# # # # # # })
# # # # # #
# # # # # # #
# # # # # #
# # # # # # #
# # # # # # df11 = pd.DataFrame({
# # # # # #     'city':['new york','chicago','orinado'],
# # # # # #     'tempreture':[21,14,35]})
# # # # # #
# # # # # #
# # # # # # df22 = pd.DataFrame({
# # # # # #     'city': ['chicago','new york','san francisco'],
# # # # # #     'tempreture':[100,200,300],
# # # # # #     'humidity':[65,68,75]
# # # # # # })
# # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # print(pd.concat([df_1,df2],axis=1))
# # # # # # print(df_1.merge(df2,how='inner',on='citys'))
# # # # # # print(df11.merge(df22,on='city'))
# # # # # # print(data.merge(data2,on=['city']))
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # csv = pd.read_csv('S:/csvfiles/movies.csv')
# # # # # # csv2 = pd.read_csv('S:/csvfiles/ipl-matches.csv')
# # # # # # #
# # # # # # var = (csv2[csv2.Umpire2.str.replace(' ','').duplicated().to_numpy()==False].Umpire2.str.replace(' ',''))
# # # # # # # # print(csv.genres.str.split('|').loc[[0,1,2],[0]])
# # # # # # import collections
# # # # # # import functools
# # # # # #
# # # # # # named = collections.namedtuple('aalo',var.to_numpy()[:3])
# # # # # # # named_object = named(np.array([1,2,3]))
# # # # # #
# # # # # #
# # # # # # c = (functools.partial(named,'Guru',"Mahendrakar"))
# # # # # # p = c(3)
# # # # # # print(p._asdict)
# # # # # # print(named_object._asdict())
# # # # #
# # # # # # class method:
# # # # # #     pass
# # # # # #
# # # # # # method_object = method()
# # # # # #
# # # # # # print('------named tuple---------')
# # # # # # print(sys.getsizeof(named))
# # # # # # print(sys.getsizeof(named_object))
# # # # # #
# # # # # # print('------main-class----------')
# # # # # #
# # # # # # print(sys.getsizeof(method))
# # # # # # print(sys.getsizeof(method_object))
# # # # # #
# # # # # # print(1056-898)
# # # # #
# # # # #
# # # # # # #
# # # # # import pandas as pd
# # # # # # #
# # # # # df_1 = pd.DataFrame({
# # # # #     'citys':['mumbai','newyork','bhalki','bidar'],
# # # # #     'tempreture':[25,22,18,15],
# # # # #     'grounds':['chennai_ground','Player_ground',"Saare_Ground","TAlle_Ground"],
# # # # #
# # # # # })
# # # # # # #
# # # # #
# # # # #
# # # # #
# # # # # df2 = pd.DataFrame({
# # # # #
# # # # #     'tempreture':[17,18,25,15],
# # # # #     'date':['5/2/2023','11/2/2023','15/3/2023','20/4/2023'],
# # # # #     'citys':['Likever','mumbai','mumbai','bidar']
# # # # # })
# # # # #
# # # # #
# # # # #
# # # # # print(pd.merge(df_1,df2,on='citys',how='outer'))
# # # # # #
# # # # # # #
# # # # # # join_a = pd.DataFrame({'A':[1,2,3,4],
# # # # # #                        'B':[5,6,7,8]})
# # # # # #
# # # # # # join_b = pd.DataFrame({'C':[9,10,11,12],
# # # # # #                        'A':[13,14,15,16]})
# # # # # #
# # # # # # print(join_b)
# # # # # #
# # # # # # join_b.drop(index=[0,1],inplace=True)
# # # # # #
# # # # # # print(join_b)
# # # # # #
# # # # # # print(join_b)
# # # # #
# # # # #
# # # # # # print(df2.apply(lambda x:x==17))
# # # # #
# # # # #
# # # # # #
# # # # #----------------------------Real Practice Start-----------------------------------------------
# # # # import numpy as np
# # # # import pandas as pd
# # # #
# # # # #year,month,day -> periods  = 6
# # # # import numpy
# # # #
# # # # # dates = pd.date_range(start='2022-02-5',end='2022-02-10')
# # # # # print(numpy.sort(numpy.random.choice(dates.to_numpy(),size=3,replace=False)))
# # # #
# # # #
# # # # data_ = pd.read_csv('s:/csvfiles/movies.csv')
# # # #
# # # #
# # # # data = (data_[['title_x','year_of_release','release_date','actors','imdb_rating']])
# # # # df = pd.DataFrame({'time':pd.date_range(start='05-01-2022',end='05-31-2022', freq="12H"), 'value':np.random.randint(10,size=61)})
# # # #
# # # # # df.set_index('time',inplace=True)
# # # #
# # # # # data = pd.DataFrame([[1,2,np.NaN,4],[1,np.NaN,np.NaN,3],[1,3,5,8]])
# # # # # print(data)
# # # # # print(data[1].interpolate(method='linear'))
# # # #
# # # # # print(pd.concat([data,data],axis=1)['title_x'])
# # # # # group_names = (data.groupby('actors'))
# # # # # print(data.columns)
# # # # # x = (data.groupby('imdb_rating'))
# # # # #
# # # # # x = (x['year_of_release'])
# # # # # print(x.sum())
# # # # # #
#
# data = pd.MultiIndex.from_product((['cse','ece'],[2019,2020]))
#
# df1 = pd.DataFrame({'lcity': ['foo', 'bar', 'baz', 'foo'],
#                     'pilo': [1, 2, 3, 5]})
#
# df2 = pd.DataFrame({'lcity': ['diooo', 'bar', 'baz', 'foo'],
#                     'pilo': [5, 5, 7, 8]})

#
#
# print(df1)
# print()
# print()
#
# print(df1.unstack())
#
# print()
#
# print(df1.unstack().unstack())
#
# print()
#
# print(df1.unstack().unstack().unstack())
# # print(df1.melt(var_name='data',value_vars='values'))



# # # # # print(df1.merge(df2,left_on='pilo',right_on = 'pilo',suffixes=['_left','_right']))
# # # # #
# # # # #
# # # # # print(pd.merge(df1,df2,how='inner',on='lcity'))
# # # #
# # # #
# # # # # print(df1.stack())
# # # #
# # # #
# # # #
# # # #


# indexx = (pd.MultiIndex.from_tuples([(1,2),(1,5),(1,7),(1,2),(2,5),(2,7),(2,8)]))
#
#
# data2 = pd.DataFrame({'mumbai':[100,1000,2000,1000,2000,2000,3333],
#                      'newyork':[1000,1100,1200,1300,1400,1500,2222],
#                      'bidar':[2000,2100,2200,2300,2400,2222,5555],
#                       'city':['bhalki','bhalki','bhalki','bhalki','paris',
#                              'paris','paris']
#                      },index=indexx)
#
#
# print(data2)




# print(data2.unstack())
# print()
# print(data2.unstack().unstack())
#








# # # # #
# # # # # print(pd.pivot(data2,index='city',columns='bidar'))
# # # #
# # # #
# # # # # stack columns ko index bana deta hai
# # # #         # 0  mumbai        100
# # # #         #    newyork      1000
# # # #         #    bidar        2000
# # # #         #    city       bhalki
# # # #
# # # #
# # # #
# # # # # xxio = pd.MultiIndex.from_product([['cse','night'],[2017,2018,2019,2020]])
# # # # #
# # # # #
# # # # #
# # # # # print(pd.DataFrame([[2019,2018,2017,2016,2015,2014,2013,2012],[2019,2018,2017,2016,2015,2014,2013,2012]]))
# # # # # print()
# # # # # print()
# # # # # print()
# # # # #
# # # # # a = pd.DataFrame({'city':[2019,2018,2017,2016,2015,2014,2013,2012],
# # # # #                   'like':['newyork','bhalki','mumbai','bidar','gulbara','humpi','banglore','mysore']},index=xxio)
# # # # #
# # # # # print(a.loc[[('cse',2017),('cse',2018)]])
# # # #
# # # #
# #
import pandas as pd
import seaborn

#
# df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
#                            '5/3/2017','5/1/2017','5/2/2017','5/5/2017','5/2/2018'),
#                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
#                     'bejing','bejing','bejing','bhalki'),
#                    'humidity':(56,58,60,80,83,85,26,30,35,2),
#                    'tempreture':(65,66,68,75,78,82,80,77,79,3),
#                    'gender':('girl','boy','girl','boy','girl','boy','girl','girl','girl',np.NAN)},)





















# print(df.groupby(pd.Grouper(key='date')).mean())
# #
# data = (df.groupby('date').mean())
# print(data.unstack())

# print(df.sum())
# print(pd.crosstab(index=df.date,columns=df.gender))
# print(pd.concat([df.melt(),df],axis=0))
# # # # # #
# # # # #
# # # # # print(df.pivot(index='date',columns='city'))
# # # # #
# # # # #
# # # # # print(df.pivot(index='city',columns='date'))
# # # #
# # # #
# # # # import matplotlib.pyplot as plt
# # # #
# # # # #
# # # # # price = [100,200,200,400,500]
# # # # # city = ['bhalki','bidar','gulbarga','banglore','mumbai']
# # # # #
# # # # # price2 = [550,600,700,800,900]
# # # # # city2 = ['pune','lalkhila','dehli','natak-kk','piloraaj']
# # # # #
# # # # #
# # # # #
# # # # # plt.plot(price,city,marker='*',color='c',markersize=15)
# # # # # plt.plot(price2,city2,marker="*",color='b',markersize=15)
# # # # # plt.show()
# # # # #
# # # #
# # # # #
# # # # # plt.scatter(df.season,df.Fours,c=[0,1,2,3,4,5],cmap='hsv_r')
# # # # # plt.scatter(df.season,df.Sixes,c=[0,1,2,3,4,5],cmap='viridis')
# # # # #
# # # # #
# # # # # for texts in zip(df.season,df.Fours):
# # # # #     plt.text(x=texts[0],y=texts[1],s='Four')
# # # # #
# # # # #
# # # # # for texts in zip(df.season,df.Sixes):
# # # # #     plt.text(x=texts[0],y=texts[1],s='Sixes')
# # # #
# # # # # plt.show()
# # # #
# # # #
# # # #
# # # # # bar = plt.bar(df.season,df.Fours,width=0.2,color=['y','g','r','b','b'])
# # # # #
# # # #
# # # # # a = [10,15,33,44,49,51,70,80,60,66]
# # # # #
# # # # # histogram = plt.hist(df.Fours,width=10,bins=[1563,1700,2054])
# # # # # plt.show()
# # # #
# # #
# # #
# # # df = pd.read_csv('s:/csvfiles/fours-sixes.csv')
# # # df2  = pd.read_csv('s:/csvfiles/batter (1).csv')
# # # df3 = pd.read_csv('s:/csvfiles/vk.csv')
# # # df4 = pd.read_csv('s:/csvfiles/gayle-175.csv')
# # # df5  = pd.read_csv('s:/csvfiles/batsman_season_record.csv')
# # # df6 = pd.read_csv('s:/csvfiles/iris.csv')
# # #
# # #
# # #
# # #
# # # # print(df5)
# # # # # iris = (df6.sample(5))
# # # # # iris2 = iris.replace({'Iris-setosa':0,'Iris-virginica':1,'Iris-versicolor':2})
# # # # # plt.bar(df5.batsman,df5['2015'],width=0.2,color='black',label='2015')
# # # # # plt.bar(df5.batsman,df5['2016'],bottom=df5['2015'],width=0.2,color='red',label=2016)
# # # # # plt.bar(df5.batsman,df5['2017'],bottom=df5['2016']+df5['2015'],color='green',width=0.2,label=2017)
# # # # # plt.legend()
# # # # # print(pd.pivot(df5,index='2015',columns='batsman'))
# # # # # pie = plt.pie(df5['2015'],labels=df5.batsman,autopct='%0.1f%%',explode=[0,0,0,0.3,0.3])
# # # # # plt.show()
# # # # # print(df5)
# # # #
# # # # # print(iris.filter(['Id',"SepalLengthCm"]))
# # # # # plt.figure(figsize=(10,10))
# # # # # plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=iris2.Species,cmap='summer',)
# # # # # for index,_ in enumerate(zip(iris.SepalLengthCm,iris.PetalLengthCm)):
# # # # #     plt.text(_[0],_[1],iris.Species.iloc[index])
# # # # # plt.show()
# # # #
# # # # #
# # # # # batsmans = (df2.sample(25))
# # # # # print(batsmans.runs.max())
# # # # #
# # # # # plt.figure(figsize=(10,10))
# # # # # plt.scatter(batsmans.runs,batsmans.strike_rate)
# # # # #
# # # # # for index,xx in enumerate(zip(batsmans.runs,batsmans.strike_rate)):
# # # # #     plt.text(xx[0],xx[1],batsmans.batter.iloc[index])
# # # # #
# # # # #
# # # # # plt.axhline(150,color='red')
# # # # # plt.axvline(4000,color='yellow')
# # # # # plt.show()
# # # #
# # # #
# # # #
# # # #
# # # # # figure,axis = plt.subplots(figsize=(10,10))
# # # # #
# # # # # print(p)
# # # #
# # # #
# # # #
# # # # fig = plt.figure()
# # # #
# # # # x = fig.add_subplot(221,)
# # # #
# # # # x.scatter(df5.batsman,df5['2015'])
# # # #
# # # #
# # # # x = fig.add_subplot(222)
# # # #
# # # # x.scatter(df5.batsman,df5['2016'])
# # # #
# # # #
# # # # x = fig.add_subplot(223)
# # # # plt.xticks(rotation='vertical')
# # # # x.scatter(df5.batsman,df5['2016'])
# # # #
# # # #
# # # #
# # # # x = fig.add_subplot(224)
# # # # plt.xticks(rotation='vertical')
# # # # x.scatter(df5.batsman,df5['2016'])
# # # #
# # # #
# # # #
# # # #
# # # # plt.show()
# # #
# # # import matplotlib.pyplot as plt
# # # # fig = plt.figure()
# # # #
# # # # df2 = df2.sample(5)
# # # #
# # # # a = fig.add_subplot() # his create only (pie hist bar plot) #subplot not working
# # # #
# # # #
# # # #
# # # # subplott = plt.subplot()
# # # # # print(df2)
# # # # # subplott.scatter(df2.runs,df2.avg,df2.strike_rate)
# # # #
# # # # x = np.linspace(-10,10,100)
# # # # y = np.linspace(-10,10,100)
# # # #
# # # # xx,yy = np.meshgrid(x,y)
# # # # z = xx**2+yy**2
# # # # #
# # # # # x = subplott.plot_surface(xx,yy,z)
# # # # # plt.colorbar(x)
# # # #
# # # # x = subplott.contourf(xx,yy,z)
# # # # plt.colorbar(x)
# # #
# # #
# # #
# #
# # # import pandas as pd
# # # import numpy as np
# # #
# # #
# # # read_excel = pd.read_excel('s:/code-r/csvfiles/xlxs')
# #
# #
# import seaborn as sea
# import numpy as np
# import pandas as pd
#
#
# #
# # titanic =  sea.load_dataset('titanic')
# # print(titanic)
# #
# #
# #
# # titanic.pivot(index=t)
# #
# #
#
# #
# # df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
# #                            '5/3/2017','5/1/2017','5/2/2017','5/5/2017'),
# #                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
# #                     'bejing','bejing','bejing'),
# #                    'humidity':(56,58,60,80,np.NAN,85,26,30,35),
# #                    'tempreture':(65,66,68,75,78,82,80,77,79),
# #                    'gender':('girl','boy','girl','boy','girl','boy','girl','girl','girl')},)
# #
# #
# #
# #
# #
# # city_groupby = (df.groupby('city'))
#
# # print(city_groupby.get_group('bejing'))
#
#
# #
# # print(df.replace({'city':'newyork',
# #                   'gender':'girl'},{'city':'bhalki',
# #                                     'gender':'boy'}))
#
#
# # df['sex'] = np.NAN
# # print(np.isnan(df.sex))
# # print(df.sex.sum())
#
# # print(pd.concat([df,df],))
#
#
# # print(df.fillna(method='ffill'))
#
#
#
#
# # print(df.merge(df,on='city'))
#
# # print(df)
# #
# #
# # print(pd.pivot(df,index='date',columns='city'))
# #
# # print(pd.pivot_table(df,index='date',columns='city',aggfunc='sum'))
#
#
#
#
# # print(" Hello World----> Light Weight Brother King Of The world !! ")
# #
# # print(df)
# # print(df.melt('city'))
# #
# # import matplotlib.pyplot as plt
# # array = [1,2,3,4,5,6]
# # array2 = [1,2,3,4,5,6]
#
#
# # print(np.mean(np.cumsum(array2)))
# # print(np.cumsum(array2)-np.mean(array2))
# #
# # # sea.histplot(x=np.cumsum(array2))
# # sea.barplot(y=np.cumsum(array2),estimator='mean')
#
# # plt.show()
#
# #
# # my  = time.perf_counter()
# # array = [x for x in range(100000)]
# #
# # left_index = 0;
# # main_index = 0
# # right_index = 1;
#
#
#
#
# # data = sea.load_dataset('titanic').age
# #
# #
# # sea.kdeplot(x=data)
# #
# # print(np.mean(data))
# # print(np.std(data))
# # plt.show()
#
#
# #
# # samples = []
# #
# # from pprint import pprint  as print
# #
# # data = sea.load_dataset('titanic')
# #
# #
# # for _ in range(40):
# #     samples.append(data.age.sample(50).mean())
# #
# #
# #
# #
# # sea.kdeplot(samples)
# #
# #
# #
# # plt.show()


# import pandas as pd
#
#
# a = pd.read_csv('S:/csvfiles/data.csv',encoding='latin-1',nrows=5,)
#
# print(a.shape)


# titanic = seaborn.load_dataset('titanic')
#
# print(titanic.pivot_table(index='survived',columns='sex',aggfunc='count')['alone'])
#
# print(titanic[['alone','survived','sex']])














