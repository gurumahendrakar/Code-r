import re  #
# import re
# import requests
#
# # text_ = '''>>> url = "http://olympus.realpython.org/profiles/poseidon"
# #             >>> page = urlopen(url)
# #
# #             url = "http:+olympus.realpython.org/profiles/poseidon"
# #             >>> html = page.read().decode("utf-8")
# #             >>> start_index = html.find("<title>") + len("<title>")
# #             >>> end_index = html.find("</title>")
# #             >>> title = html[start_index:end_index]
# #             >>> title
# #             '\n<head>\n<title >Profile: Poseidon
# #
# # '''
# # compile = re.compile('[a-z]+:(//|-|\+)+[a-z]+\.[a-z]+\.[a-z]+',re.IGNORECASE)
# # search = compile.finditer(text_)
# #
# # for x in search:
# #     print(x.group())
#
#
# # &
# # or
# # not
# # xor
#
#
# # import re
#
# # string = "G#uru 7411891852 Mahendrakar"
# # compile = re.compile("[a-zA-z].+")

# # print(re.search(compile,string))
#
# import os
#
# file = os.open('texting.txt',os.O_RDWR)
# io = os.fdopen(file,mode='r').read()
#
# print(io)





#--------------------------------------------------Regex Expressions-----------------------------------------------------------------------


#====================================================================================================


# butilin-exceptions ---> ] ^ \ -

# .   koi bhi charcter match karega  ----> expresion ---- p.t
            #explanation ->   pet #matched
            #                 ptt # matched
            #                 ptc #not macthed

#=======================================================================================================

# [abcd] ----> brackets ke andar jo bhi likhonge o sab match honge

#[^abcd] ----> not match any character

#[a-z] & [A-Za-z] & [a-zA-Z0-9] & [06-9-9] & [0\-/]1

#==============================================================================================

# important

# \d numrical values

# \w (numerical,letters,upper-lower->letters,)  -> symbol and whitspace not matching

#\s whitespace


#\D anything but not digit

#\w anything but not (numerical,letters,upper-lower->letters,)



#=================================================================================

#         * 0 or moretimes
#         1 or more times
#         0 or 1 time 


#==============================================================================================

 # () ---> Grouping


#================================================================================
#
import re
#
#

number = "3333-3333-3333 helloworld helloworld"

pattern = (re.compile('(\w{4})-(\w{4})-(\w{4})'))


# io = (re.search(pattern=pattern,string=number))
# print(io.group(1))



a = re.sub(pattern='helloworld',repl='likeit',string=number)

aa = re.split(pattern="helloworld",string=number,maxsplit=2)
print(a)
print(aa)



# import requests as request
# from bs4 import BeautifulSoup
#
#
# url = 'https://www.imdb.com/chart/top/'
# web_hitting = request.get(url)
#
# text = web_hitting.content
# 
# text  = (text.decode())
#
# # textt = ""
#
# # for al in text:
# #     textt+=chr(al)
#
#
#
# #
# # prettify_text = BeautifulSoup(text,'lxml')
# #
# print(re.findall(pattern=
#                  re.compile('<a href=".+"\stitle="Sergio'),string=text))
# #
# #
#





import re

# x = ".7411-89-1852"
#
# phone  = re.match(re.compile('\.(\d{4})-(\d{2})-(\d{4})'),x)
#
# print(phone)














