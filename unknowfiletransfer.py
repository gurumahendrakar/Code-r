
# # import shutil
# # import os
# #
# # # print(os.getcwd())
# #
# # # Codeing_files = [
# # # ]
# # # for files in os.listdir(os.getcwd()):
# # #     if files.endswith('.py') or files.startswith('.') or files.startswith('__') or files.startswith('allfiles'):
# # #         Codeing_files.append(files)
# #
# #
# # # for file in os.listdir(os.getcwd()):
# # #     os.chdir(r'C:\Users\mahen\bitepy\allfiles')
# # #     if file not in Codeing_files and file not in os.listdir(os.getcwd()) and not file.startswith('allfiles'):
# # #         shutil.move(fr'C:\Users\mahen\bitepy\{file}', r"C:\Users\mahen\bitepy\allfiles")
# #
# #
# # # else:
# # #     print("All Files Are Moved In Your Directory")
# #
# #
# # # #shutil.move(#kya Bhejna hai uska path,kidar bhejna hai uska path)
# #
# #
# #
# # # #
# #

# import os
# import shutil

# pngs_names = []
# for x in os.listdir(os.getcwd()):
#     if x.endswith('.jpg') or \
#         x.endswith('.jpeg') or \
#             x.endswith('.webp') or \
#                 x.endswith('.png'):\
#                     pngs_names.append(x)


# for png_file in pngs_names:
#     shutil.move(png_file,'S:/pygame/')

# print(os.getcwd())

# # Codeing_files = [
# # ]
# # for files in os.listdir(os.getcwd()):
# #     if files.endswith('.py') or files.startswith('.') or files.startswith('__') or files.startswith('allfiles'):
# #         Codeing_files.append(files)


# # for file in os.listdir(os.getcwd()):
# #     os.chdir(r'C:\Users\mahen\b\allfiles')
# #     if file not in Codeing_files and file not in os.listdir(os.getcwd()) and not file.startswith('allfiles'):
# #         shutil.move(fr'C:\Users\mahen\bitepy\{file}', r"C:\Users\mahen\bitepy\allfiles")


# # else:
# #     print("All Files Are Moved In Your Directory")


# # #shutil.move(#kya Bhejna hai uska path,kidar bhejna hai uska path)

import shutil
import os

# print(os.getcwd())

# Codeing_files = [
# ]
# for files in os.listdir(os.getcwd()):
#     if files.endswith('.py') or files.startswith('.') or files.startswith('__') or files.startswith('allfiles'):
#         Codeing_files.append(files)


# for file in os.listdir(os.getcwd()):
#     os.chdir(r'C:\Users\mahen\bitepy\allfiles')
#     if file not in Codeing_files and file not in os.listdir(os.getcwd()) and not file.startswith('allfiles'):
#         shutil.move(fr'C:\Users\mahen\bitepy\{file}', r"C:\Users\mahen\bitepy\allfiles")


# else:
#     print("All Files Are Moved In Your Directory")


# #shutil.move(#kya Bhejna hai uska path,kidar bhejna hai uska path)





import os 
import shutil


for x in os.listdir(os.getcwd()):
    if x in ['.idea''.metadata','__pycache__'] or x.endswith('py'):
        pass 
    else:
        shutil.move(x,r"S:\Code-r\allfiles")
=======
pngs_names = []
for x in os.listdir(os.getcwd()):
    if x.endswith('.jpg') or \
        x.endswith('.jpeg') or \
            x.endswith('.webp') or \
                x.endswith('.png'):\
                    pngs_names.append(x)


for png_file in pngs_names:
    shutil.move(png_file,'S:/pygame/')

print(os.getcwd())

Codeing_files = [
]
for files in os.listdir(os.getcwd()):
    if files.endswith('.py') or files.startswith('.') or files.startswith('__') or files.startswith('allfiles'):
        Codeing_files.append(files)


for file in os.listdir(os.getcwd()):
    os.chdir(r'C:\Users\mahen\bitepy\allfiles')
    if file not in Codeing_files and file not in os.listdir(os.getcwd()) and not file.startswith('allfiles'):
        shutil.move(fr'C:\Users\mahen\bitepy\{file}', r"C:\Users\mahen\bitepy\allfiles")


else:
    print("All Files Are Moved In Your Directory")


#shutil.move(#kya Bhejna hai uska path,kidar bhejna hai uska path)



#

