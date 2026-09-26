#written by: Ferran,Matt
#class: DSC 510
#Week 1 Hello World Program
#2026-09-011



print('Hello, world!')

#Week 2 class note

message = "Hello, my name is Matt"
print (message)

eggsInOmlete = 3
print (eggsInOmlete)

knowshowtocook = True
print(knowshowtocook)

# \\ Backslash (\)
#  \' Single- quote (')
# •\" Double- quote (")
#  \a ASCII bell (BEL)
#  \b ASCII backspace (BS)
#  \f ASCII formfeed (FF)
#  \n ASCII linefeed (LF)
#  \N{name} Character named name in the Unicode database (Unicode only)
#  \r ASCII carriage return (CR)
#  \t ASCII horizontal tab (TAB)
#  \uxxxx Character with 16- bit hex value xxxx (Unicode only)
#  \Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
#  \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
#  \xhh Character with hex value hh

#ex
print("Hi Tim, \"It's over there!\"")
#
x=9
y=6
print( x+y)
print(x-y)
print(x*y)
print(x/y)
#
#forcedIntegerAnswer = integer1 // integer2
print (5.0/9.0055555555555555555556)

'''
A multiline comment starts with a line of three quote characters(above)
This is a long comment block It can be any length You do not need to use
the # character here You end it by entering the same three quotes you
used to start (below)
'''

'''
favoritecolor = input("What is your favorite color?")
print ('your favorite color is', favoritecolor)
'''

#to convert what data is int() or float()

number_of_feet = 125.5457
print("%.2f"%number_of_feet)

'''
The format specifier syntax above is as follows:
– % indicates the beginning of the format specifier.
– 2 indicates the number of decimal places
– f’ or ‘F’ indicates that the value is floating point decimal format. The alternate form causes the result to always contain
a decimal point, even if no digits follow it. The precision determines the number of digits after the decimal point and
defaults to 6.
– The second % is the modulo operator and separates the format specifier from the value being formatted
'''


miles = 17.1756581
print('{:.2f}'.format(miles))