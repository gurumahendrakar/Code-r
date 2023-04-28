import numpy
import pandas
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

#
#
# #
# # data_ = pd.read_csv('s:/csvfiles/ipl-matches.csv')
# # print(data_.WinningTeam.value_counts().head(1))
# #
# #
# # date = np.arange(0,10000)
# #
# # a = np.random.randint(low=0,high=date.shape[0],size=100)
# # # print(plt.hist(a,rwidth=0.1,color='black'))
# #
# # a = [100,200,200,400,500]
# # subjects = ['english','hindi','kannda','account','social'
# #             ]
# #
# # print(plt.style.available)
# # plt.style.use('seaborn')
# # plt.pie(a,labels=subjects,explode=[0,0,0,0.5,0])
# #
# # plt.savefig('likebaby.png')
# # import os
# #
# # print('likebaby.png' in os.listdir(os.getcwd()))
# #
# #
# # #
# # iris = pd.read_csv('S:/csvfiles/iris.csv')
# # iris = (iris.sample(5).replace({'Iris-setosa':0,
# #                                 'Iris-virginica':1,
# #                                 'Iris-versicolor':2}))
# # print(iris.shape)
# #
# #
# # iriss = pd.DataFrame([*iris.Id],columns=['Id']).head(10)
# #
# # print(pd.concat([iris,iriss])['Id'].size)
#
# # print(iris)
# # colors = ['r','g','b','y','p']
# # plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=['g'],alpha=0.2)
#
#
# # for x in ((zip(iris.SepalLengthCm,iris.PetalLengthCm))):
# #     plt.text(x=x[0],y=x[1],s='like')
# #
# # plt.xticks(rotation='vertical')
# # plt.axhline(4.9)
# # plt.axvline(5.6)
#
#
# # a = np.array([1,2,3,4])
# #
# # print(a[np.isnan(np.where(a%2==0,True,np.nan))==False])
#
# # figure,subplott = plt.subplots(nrows=2,ncols=2)
# # figure.show()
# # print(figure,subplott,sep='\n')
# #
# # print(iris)
# # subplott.scatter(iris.SepalLengthCm,iris.PetalLengthCm)
# # plt.show()
#
#
#
#
# #
# #
# # # bar = plt.bar(df.season,df.Fours,width=0.2,color=['y','g','r','b','b'])
# # #
# #
# # # a = [10,15,33,44,49,51,70,80,60,66]
# # #
# # # histogram = plt.hist(df.Fours,width=10,bins=[1563,1700,2054])
# # # plt.show()
# #
# #
# #
# # df = pd.read_csv('s:/csvfiles/fours-sixes.csv')
# # df2  = pd.read_csv('s:/csvfiles/batter (1).csv')
# # df3 = pd.read_csv('s:/csvfiles/vk.csv')
# # df4 = pd.read_csv('s:/csvfiles/gayle-175.csv')
# # df5  = pd.read_csv('s:/csvfiles/batsman_season_record.csv')
# # df6 = pd.read_csv('s:/csvfiles/iris.csv')
#
# # print(df5)
# # # iris = (df6.sample(5))
# # # iris2 = iris.replace({'Iris-setosa':0,'Iris-virginica':1,'Iris-versicolor':2})
# # # plt.bar(df5.batsman,df5['2015'],width=0.2,color='black',label='2015')
# # # plt.bar(df5.batsman,df5['2016'],bottom=df5['2015'],width=0.2,color='red',label=2016)
# # # plt.bar(df5.batsman,df5['2017'],bottom=df5['2016']+df5['2015'],color='green',width=0.2,label=2017)
# # # plt.legend()
# # # print(pd.pivot(df5,index='2015',columns='batsman'))
# # # pie = plt.pie(df5['2015'],labels=df5.batsman,autopct='%0.1f%%',explode=[0,0,0,0.3,0.3])
# # # plt.show()
# # # print(df5)
# #
# # # print(iris.filter(['Id',"SepalLengthCm"]))
# # # plt.figure(figsize=(10,10))
# # # plt.scatter(iris.SepalLengthCm,iris.PetalLengthCm,c=iris2.Species,cmap='summer',)
# # # for index,_ in enumerate(zip(iris.SepalLengthCm,iris.PetalLengthCm)):
# # #     plt.text(_[0],_[1],iris.Species.iloc[index])
# # # plt.show()
# #
# # #
# # # batsmans = (df2.sample(25))
# # # print(batsmans.runs.max())
# # #
# # # plt.figure(figsize=(10,10))
# # # plt.scatter(batsmans.runs,batsmans.strike_rate)
# # #
# # # for index,xx in enumerate(zip(batsmans.runs,batsmans.strike_rate)):
# # #     plt.text(xx[0],xx[1],batsmans.batter.iloc[index])
# # #
# # #
# # # plt.axhline(150,color='red')
# # # plt.axvline(4000,color='yellow')
# # # plt.show()
# #
# #
# #
# #
# # # figure,axis = plt.subplots(figsize=(10,10))
# # #
# # # print(p)
# #
# #
# #
# # fig = plt.figure()
# #
# # x = fig.add_subplot(221,)
# #
# # x.scatter(df5.batsman,df5['2015'])
# #
# #
# # x = fig.add_subplot(222)
# #
# # x.scatter(df5.batsman,df5['2016'])
# #
# #
# # x = fig.add_subplot(223)
# # plt.xticks(rotation='vertical')
# # x.scatter(df5.batsman,df5['2016'])
# #
# #
# #
# # x = fig.add_subplot(224)
# # plt.xticks(rotation='vertical')
# # x.scatter(df5.batsman,df5['2016'])
# #
# #
# #
# #
# # plt.show()
#
# import matplotlib.pyplot as plt
# # fig = plt.figure()
# #
# # df2 = df2.sample(5)
# #
# # a = fig.add_subplot() # his create only (pie hist bar plot) #subplot not working
# #
# #
# #
# # subplott = plt.subplot()
# # # print(df2)
# # # subplott.scatter(df2.runs,df2.avg,df2.strike_rate)
# #
# # x = np.linspace(-10,10,100)
# # y = np.linspace(-10,10,100)
# #
# # xx,yy = np.meshgrid(x,y)
# # z = xx**2+yy**2
# # #
# # # x = subplott.plot_surface(xx,yy,z)
# # # plt.colorbar(x)
# #
# # x = subplott.contourf(xx,yy,z)
# # plt.colorbar(x)
# #
# #
# #
# # df = (df[(df.ballnumber<7) & (df.batsman_run==6)])
#
#
#
# # (df[['ballnumber','batsman_run']])
# #
# # print(df.pivot_table(index='overs',columns='ballnumber')['batsman_run'])
# #
# #
# # a = (df.pivot_table(index='overs',columns='ballnumber',aggfunc='count')['batsman_run'])
# #
# #
# # plt.imshow(a)
# # plt.colorbar()
# # plt.show()
#
#
# #
# # series = pd.Series([1,2,3,4,5,6,7])
# #
# # print(series.plot(kind='pie'))
# # plt.show()
#
#
#
#
# # df5.plot(kind='scatter',x='batsman',y='2015',marker='+',c='2016')
# # plt.show()
#
#
#
#
#
#
# # df = pd.read_csv('s:/csvfiles/IPL_Ball_by_Ball_2008_2022.csv')
#
#
# # df = pd.DataFrame({'date':('5/1/2017','5/2/2017','5/3/2017','5/1/2017','5/2/2017',
# #                            '5/3/2017','5/3/2017','5/2/2017','5/5/2017'),
# #                    'city':('newyork','newyork','newyork','mumbai','mumbai','mumbai',
# #                     'bejing','bejing','bejing'),
# #                    'humidity':(56,58,60,80,83,85,26,30,35),
# #                    'tempreture':(65,66,68,75,78,82,80,77,79)})
# #
# #
# #
# # print(df.pivot('city','date')['humidity'])
# # print()
# # print()
# # print(df.pivot('city','date')['tempreture'])
# # print()
# # print()
# # print(df.pivot_table('city','date',aggfunc = 'count'))
# #
# #
#
#
#
#
# import seaborn as sn
#
# data = pd.DataFrame({'bill':[10,20,30,40,25,30,27,22,45],
#                      "gender":['male','female','male','male','female','male','male','female','female']})
#
# def fun(value):
#     if value=='male':
#         return 1
#     return  0
#
#
# data.gender = (data['gender'].apply(func=lambda x : 11 if x=='male' else 00))
#
#
# print(data)
# # print(data)



# data = pd.DataFrame(data)
# res = sn.distplot(data,rug=True,bins=2)



# data = pd.DataFrame()

#

#
# print(tips.columns)
# tips.set_index('sex',inplace=True)

#
# io = plt.imshow(data=tips,X=np.arange(0,20).reshape(5,4),cmap='hot')
#
# plt.colorbar()
#
# io = plt.imshow(data=tips,X=np.ones(shape=(5,2)),cmap='hot')

# plt.show()
#
# i = seaborn.heatmap(data=[[0,1,2,3],
#                           [4,5,6,7],
#                           [8,9,10,11]],cmap='hot',yticklabels=['sunday','monday','trusday'])


# plt.show()


#
# io = np.array([1,2,3,4,5,6])/6
#
# print(io)

# sn.displot(x=io,kind='hist',col=io)

# x = np.random.default_rng(seed=1000)
# print(x.uniform(0,10,size=10))

#
# x = (np.arange(140,191))
# genders = np.array((['male','female']*25))
# genders = np.append(genders,'male')
#
# (np.random.shuffle(genders))
#
# print(genders.size,x.size)
# sn.displot(x=x,kind='kde',fill=True,hue=genders)
#
# plt.show()


#
# iris = sns.load_dataset('iris')
#
# print(iris.columns)
#
# sns.displot(data=iris,x='sepal_length',kind='kde',
#             hue='species')
# sns.displot(data=iris,x='sepal_width',kind='kde',
#             hue='species')



#
# figure,axis  = (subp)
#
# print(axis)

# sns.displot(data=iris,x='petal_width',kind='kde',
#             hue='species')
#
#
#
# sns.displot(data=iris,x='petal_length',kind='kde',
#             hue='species')


# sns.displot(data=iris,kind='ecdf')

#
# joint = sns.jointplot(data=iris,
#                       x='sepal_length',
#                       marginal_ticks=True,
#                       y='petal_length',color='w',
#                       kind='reg')
#
# joint.plot_joint(sns.kdeplot,color='green',
#                  zorder=0,levels=6,fill=True)

# facet = sns.FacetGrid(data=iris,hue='species',
#                       col='species',
#                       row='species')
# facet.map(x=iris.sepal_length,
#
#           y=iris.sepal_width,
#           func=sns.histplot)



# ages = np.random.randint(1,70,size=100)
# agess = pd.Series(ages).value_counts()
# print(agess.reset_index(inplace=True))
#
# ages = (pd.Series(ages).value_counts()/pd.Series(ages))
# print(ages.max())
#
# a = sns.displot(x=agess['index'],y=ages,cbar=True)
#
# plt.show()
#
# print(numpy.cov([1,2,3,4,5,6,10,20]))
#
#
# print(sum([1,2,3,4,5,6,7,8]))
#
# print(np.std([1,2,3,4,5,6,10,20]))
#
#
# print(17.5/np.sqrt(4.3*125))

# s = pd.Series([1,2,3,1,2])
#
# print(s.unique())

# from pprint import pprint as print


tips = sea.load_dataset('tips')



pivot = pd.DataFrame({'day':['s','m','f','w','f'],
                      'year':[2021,2018,2023,2024,2018],
                      'price':[500,5888,200,100,25000]})

#
# data = (pd.pivot_table(data=pivot ,index='day',columns='year',
#                values='price',aggfunc='sum'))
#
# print(data)
#
# sea.heatmap(data,annot=True)


#
# scatter = sea.scatterplot(data=tips,x='day',y='tip',hue='sex')
# lineplot = sea.lineplot(data=tips,x='day',y='tip',hue='total_bill')



# relplot = sea.relplot(data=tips,x='day',y='tip',hue='sex')



#heatmap

# relplot ---> scatter lineplot
# displot ---> kde hist ecdf


#catplot ---> stripplot  swarmplot boxplot  voilinplot countplot pointplot barplot facetgrid pairgrid jointplot




# tips.time = pd.date_range('12-04-2023',periods=tips.time.size)
# print(type(tips.time))
# displot = sea.displot(data=tips,x='tip',kind='ecdf',hue='sex',rug=True)
# plt.xticks(rotation='vertical')


#
# heatmp = sea.heatmap(data='tips',=np.arange(20).reshape(4,5))
#
#


# x = plt.figure(figsize=(10,10))
#
# figure = plt.figure()
#
# io = figure.add_subplot(2,2,1)
# io.scatter(data=tips,x='sex',y='tip')
#
#
#
#
# io = figure.add_subplot(2,2,2)
# io.scatter(data=tips,x='sex',y='tip')
#
#
#
# io = figure.add_subplot(2,2,3)
# io.scatter(data=tips,x='sex',y='tip')
#
#
#
#
# io = figure.add_subplot(3,2,4)
# io.scatter(data=tips,x='sex',y='tip')
#
#
# io = figure.add_subplot(3,3,4)
# io.scatter(data=tips,x='sex',y='tip')


# print(tips.columns)

# print(tips.columns)
# catplot = sea.catplot(data=tips,x='sex',y='total_bill',kind='point',estimator='max')
# print(pd.crosstab(index=np.arange(tips.tip.size),columns='tip'))

# print(tips.columns)
# coming_data = (pd.crosstab(index=[tips.sex,tips.day],columns=tips.smoker).unstack())
#
# print(coming_data)
# sea.heatmap(coming_data,annot=True,cmap='jet')

# plt.show()

#
# ages = np.arange(0,101)
#
# array = ([])
# for _ in range(100):
#     x = (np.percentile(ages,_))
#     array.append(x)
#
#
# sea.scatterplot(ages)
# titanic = sea.load_dataset('titanic')
#

#
# normal_data = (pd.Series(np.random.normal(loc=5,scale=5,size=30)))
#
# print(normal_data.mean(),normal_data.std())
#
# sea.kdeplot(x=normal_data)
#
# titanic = sea.load_dataset('titanic')
# print(titanic.columns)
#
#
#
# titanicc= sea.kdeplot(data=titanic,
#                        x='age')
#
#
# print(titanic.age.mean(),titanic.age.std())


# io  = numpy.random.uniform(0,100,100)
# subplot = plt.subplots(nrows=1,ncols=2)



# hist = subplot[1][0].hist(x=io,bins=8)
# kde = subplot[1][1].kde(x=io)




# bionomil = np.random.binomial(2,0.5,1000)




# sea.swarmplot(pd.Series(bionomil),y=pd.Series(bionomil).value_counts(),hue=pd.Series(bionomil).value_counts().unique())
#
# seris  = pd.Series(bionomil)
# x = (seris.value_counts())
#
# sea.barplot(x=x.index,y=x)
#
#
# print(x)

# random = np.random.randint(0,2,size=(1000,10))
# two_d = np.arange(0,25).reshape(5,5)
#
# random = random.mean(axis=1)
#
#
# sea.histplot(random,bins=20)


# print(np.concatenate([two_d,two_d],axis=1))
# print(two_d.sum(axis=0))
# print(random)



# so = np.arange(0,101)
#
# print(pd.Series(so).mean())
# titanic = sea.load_dataset('titanic')

#
# sea.kdeplot(
#     x=titanic.age
# )


# sea.kdeplot(
#     so=titanic.age
# )


# print(sea.histplot(
#))
#
# da = (pd.crosstab(index=titanic.age,columns=titanic.sex))
# print(da)
#
#
# plt.xticks(rotation='vertical')
# sea.barplot(x=da.index,y=da.male)
#






#heatmap

# relplot ---> scatter lineplot
# displot ---> kde hist ecdf


#catplot ---> stripplot  swarmplot boxplot  voilinplot countplot pointplot barplot facetgrid pairgrid jointplot

#
#
#
# data = pd.read_csv('s:/csvfiles/students.csv')
# data2 = pd.read_csv('S:/csvfiles/batsman_season_record.csv')
# print(data2.columns)


# print(data2['2015'].max(),data2['2016'].max(),data2['2017'].max())


# x = sea.pairplot(data2,hue='batsman')
# x.map(func=sea.histplot)

# plt.xticks(rotation= 'vertical')



#
#
# for name,value in (list(zip(data.name,data.partner))):
#     plt.text(name,value,name)




# print(data2)

# plt.show()