# import PyPDF2
#
#
# page_read = open(r"S:\platform\Lesson-00.pdf",'rb')
#
# reader = PyPDF2.PdfReader(page_read)
# page = reader.pages[1]
#
#
# print((page.rotate(90*5)))
#
# count=0
# for img in page.images:
#     with open(str(count)+img.name,'wb') as fp:
#         fp.write(img.data)
#         count+=1
#
# print(page.extract_text())
#
#

import pandas as pd


