<<<<<<< HEAD
# import os
# import shutil
#
#
# os.chdir(os.path.join(os.getcwd(),'allfiles'))
# # print(os.makedirs('Guru/Gurji'))
# # print(os.removedirs('texting.csv'))
#
# for x,y,z in os.walk(os.getcwd()):
#     print(x)
#     print(y)
#     print(z)
#
#
#
#
#
# import os
# import time
#
# for x in os.listdir(os.getcwd()):
#     pass
#
#
# # c = os.open('texting.txt',os.O_RDWR)
# # os.write(c,b"Guru Mahendrakar")
# #
# # u = (os.stat("texting.txt"))
# # print(u)
#
#
# k = os.open('texting.txt',os.O_RDWR)
# # os.write(k,"Guru".encode())
# # for x in (os.read(k,10000)):
# #     print(chr(x),end=" ")
#
# # print(os.close(k))
#
# # print(os.close(k)) # closing file
# # print(os.closerange(k,k)) # closing file
#
#
# cs = os.fdopen(k,'r+')
#
# print(cs.read())
# os.lseek(k,0,0)
#
# print(cs.read(1))
# print(cs.read())
import os
import shutil
import string
#
# print(os.access(r"C:\Users\mahen\OneDrive\Pictures\28-12-2022 01_56_59.png",2))
# print(os.system('Spotify'))
# print(os.path.abspath("Guru"))
# print(os.path.dirname(os.getcwd()))
# print(os.path.basename(os.getcwd()+"/texting.txt"))
# print(os.path.split(os.getcwd()+"/texting.txt"))
# print(os.path.splitext(os.getcwd()+"\\texting.txt"))
# print(os.path.isdir("S:/floor/")) # ye directory me maujod hai folder
#



#----------------------------------shutil-----------------------------------------------

import shutil as sh
# sh.copy("index2.html","S:/floor/gurji") # isse app file store nahi karsakte
# sh.copyfile("index2.html","S:/floor/killl")
# shutil.move(file,destinatioin)
# shutil.rmtree(filepath)
=======
import os 
import shutil


os.chdir(os.path.join(os.getcwd(),'allfiles'))
# print(os.makedirs('Guru/Gurji'))
# print(os.removedirs('texting.csv'))

for x,y,z in os.walk(os.getcwd()):
    print(x)
    print(y)
    print(z)
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
