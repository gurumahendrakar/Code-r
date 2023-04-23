
# import argparse
#
# #kisi ke andar
# x = argparse.ArgumentParser(description='This Is Like you',
#
#                             usage=' Two Elements; Adding !!',
#                             )

# x.add_argument('--root',
#                help='this two numbers adding',
#                action='store_true', # action_ #
#                # type=int,
#                # default=3000
#
#
#               )
#
# x.add_argument('-guru',
#                help='this two numbers adding',
#                action='store_true', # action_
#                dest='one'
#                # default = 3000,
#                # type=float
#
#                )
# #
# x.add_argument('-p',
#                help='this two numbers adding',
#                nargs='+'
#                # default = 3000,
#                # type=float
#
#                )
#
# xx = x.parse_args()
# print(xx)


import argparse
#
#
x = argparse.ArgumentParser(description="THIS ORDERING FOR FOOD")
x.add_argument("ID",type=int) # POSITIONAL ARGUMENT ARGUMENT TO PAAS KARNA HI PADEGA
x.add_argument('--FOOD',type=str,help="ENTER THE NAME OF FOOD") # ARGUMENT PASS NAHI KAROGE TO BHI CHALEGA
x.add_argument('--Cheese',help="CHEESE NAME ENTER",
               action='store_true',
               default="NO ORDERED",
               dest='CHEESE',
               ) # (DEST ARGUMENT)  --Cheese Ko KO NAYA NAAM RAKH SAKTE HAI

x.add_argument('--friends',nargs="+") #jitna bhi argument de sakte ho


print(x.parse_args())

import getopt
import sys

# x = getopt.getopt(sys.argv[1:],"f:m:")
#
# print(x)


#
# PS S:\Code-r> python argparseee.py -f guru -m tillo
# ([('-f', 'guru'), ('-m', 'tillo')], [])
# PS S:\Code-r> python argparseee.py -f guru
# ([('-f', 'guru')], [])
# PS S:\Code-r> python argparseee.py guruji -f guru
# ([], ['guruji', '-f', 'guru'])
# PS S:\Code-r> python argparseee.py -f Guru -m Killer
# ([('-f', 'Guru'), ('-m', 'Killer')], [])
# PS S:\Code-r>




# import argparse
#
#
# x = argparse.ArgumentParser(description='This Is Like you',usage='This Is for adding some digits saveing your time!!',)
# x.add_argument('num1',help='this two numbers adding')
# x.add_argument('num2',help='this two numbers adding')
# x.add_argument('num3',help='this two numbers adding')
#
# xx = x.parse_args()
#
# print(int(xx.num1) + int(xx.num2) + int(xx.num3))

