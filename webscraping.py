# # # import requests
# # # from bs4 import BeautifulSoup
# # # import pandas
# # # #
# # # # agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
# # # # request = requests.get('https://goldrate.com/gold-rate-today/').text
# # # # beuti = BeautifulSoup(request,'html5lib')
# # # #
# # # # x = (beuti.findAll('div',class_ = 'mt-bw-card-box')[0].findAll('div',class_='card-body')[0].findAll('table',class_='table')[0].findAll('tbody'))
# # # #
# # # # city_names = []
# # # # for city_name in ((x[0].findAll('tr'))):
# # # #     city_names.append(city_name.td.text)
# # # #
# # # #
# # # # all_details = []
# # # # for one_gram in (x[0].findAll('td','pl-lg-5')):
# # # #     all_details.append(one_gram.text)
# # # #
# # # #
# # # # i,o = 0,4
# # # # colums = []
# # # # for divide_c in range(13):
# # # #     colums.append(all_details[i:o])
# # # #     i,o = o,o+4
# # # #
# # # #
# # # # if __name__ == '__main__':
# # # #     print(colums)
# # #
# # # # api = 'https://www.bing.com/search?q=gold+rate+today&cvid=cfd82f5d741a4b8aafe12714ed37a1bd&aqs=edge.0.0l9.4883j0j1&pglt=43&FORM=ANSPA1&PC=ACTS'
# # # # request = requests.get(api)
# # # #
# # # # soup = BeautifulSoup(request.text)
# # # # # print(soup.title)
# # # # # print(soup.title.parent.name)
# # # # # print(soup.get_text())
# # # #
# # # # # print(soup.p.get('class'))
# # # # # print(soup.p.attrs)
# # # #
# # # # print(soup.body.findAll('p')[0].findAll('p'))
# # import pandas as pd
# # import requests
# # from bs4 import BeautifulSoup
# # """
#
# # <!DOCTYPE html>
# # <html lang="en"><head>
# #         <meta charset="utf-8"/>
# #         <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
# #         <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
# #         <title>Document</title>
# #         <meta charset="utf-8"/>
# #         <link href="cssfile1.css" rel="stylesheet"/>
#
# #     </head>
#
# #     <body>
# #         <header>
#
# #             <h1>JOKeRR</h1>
# #             <nav>
# #                 <ul>
# #                     <li><a href="www">HOME</a></li>
# #                     <li><a href="www">ABOUT</a></li>
# #                     <li><a href="www">CONTACT_US</a></li>
# #                 </ul>
# #             </nav>
# #             <div class="clearfix"></div>
#
#
#
# #             <p>FIGHTS WITH YOU DREAM BIKE</p>
# #             <a class="explore-plus">EXPLOREPLUS</a>
# #         </header>
#
#
# #         <main>
# #             <section class="bikes-section">
# #                 <div class="bikes">
# #                     <figure class="arrow">
# #                         <img src="./project1/arrow.jpg"/>
# #                     </figure>
# #                     <img src="./project1/bike.webp"/>
# #                     <p>APACHE 200<br/>RS : 30000RS<br/>SHOP IS : GREEPARK BHALKI</p>
# #                     <img src="./project1/bike2.webp"/>
# #                     <p>BMW 200<br/>RS :    500000RS<br/>SHOP IS : GREEPARK BHALKI</p>
# #                 </div>
# #             </section>
#
# #             <section class="car-section">
# #                 <h1>CARS</h1>
# #                 <div>
# #                     <img src="./project1/cars.jpeg"/>
# #                     <p>APACHE CAR NYC<br/>RS : 30000RS<br/>SHOP IS : GREEPARK BHALKI</p>
# #                     <img src="./project1/cars2.webp"/>
# #                     <p>BMW CAR NYC<br/>RS : 500000RS<br/>SHOP IS : GREEPARK BHALKI</p>
# #                 </div>
#
# #             </section>
# #         </main>
#
# #         <footer>
# #             <nav>
# #                 <ul>
# #                     <li><a href="www">HOME</a></li>
# #                     <li><a href="www">ABOUT</a></li>
# #                     <li><a href="www">CONTACT_US</a></li>
# #                 </ul>
# #             </nav>
# #         </footer>
#
# # </body></html>
#
# # """
# # #
# # api ='https://groww.in/gold-rates'
#
# # request = requests.get(api)
# # soup_ = BeautifulSoup(request.text,'html.parser')
#
#
#
# # headings = (soup_.find_all('div','grp846ExplWrapper col l12')[0].
# #       find_all_next('thead')[0].text)
#
# # headings = ['Gram','Today','Yesterday']
# # columns = soup_.find_all('div','grp846ExplWrapper col l12')[0]\
# #     .find_all_next('tbody')[0]
#
# # rates = []
# # colu = []
# # columns = (columns.find_all('tr'))
# # for column in range(len(columns)):
# #     rate = [columns[column].get_text().split("₹")[0]]+\
# #         columns[0].get_text().split("₹")[1].split('+')
# #     colu.append(rate[0])
# #     rate = columns[0].get_text().split("₹")[1].split('+')
# #     rates.append(rate)
#
#
# # frame = pd.DataFrame(data=rates,index=colu,columns='rates-selling'.split('-'))
# # print(frame)
#
# # uiop = (soup_.findAll('table',{'class':'tb10Table'})\
# #           [1].findAll('tr'))
#
# # grams = []
#
# # for column in range(len(uiop)):
# #     grams.append(uiop[column].text.split("₹"))
#
# # for x in range(3):
# #     for xx in range(3):
# #         print(grams)
#
# # dataframe =  pd.DataFrame(grams)
# # print(dataframe)
#
# x = """
#
# <head>
#     <body>
#         <header>
#             <div>
#                 <p id='kill' >hlo brother</p>
#                 <a href='hlo'>hlo brother</a>
#             </div>
#         </header>
#     </body>
# </head>
# """
#
#
# from bs4 import BeautifulSoup
#
# with open('htmlfile1.html') as file:
#     soup_ = BeautifulSoup(x,'html.parser')
#     # soup_.a.name = "so"
#     # del (soup_.p['id'])
#     # soup_.p['class'] = ['kill','kingone']
#     #
#     # print(soup_.find_all('p')[0].string.replace_with('no long bold'))
#     # print(soup_.head)
#
#     # print(soup_.contents)
#
#
#
#
# import pandas as pd
# import requests,bs4,pprint
#
# api = 'https://www.imdb.com/list/ls576754431/'
#
# request = requests.get(api)
# soup_ = bs4.BeautifulSoup(request.text,'html.parser')
#
# io = (soup_.find_all('div',{'class':"lister list detail sub-list"}))[0].findAll('div',{'class':'lister-item mode-detail'})

# movies = []
# ratings = []
# for ioo in range(len(io)):
#     movies.append(io[ioo].find('a').find('img').get('alt'))
#     ratings.append('-'.join(io[ioo].find('span',class_='genre').text.strip().split(',')))
#
# dataf = pd.DataFrame(index=movies,data=ratings)
#
# print(dataf)

# print(soup_.find('div',attrs={'id':'nblogin'}))


