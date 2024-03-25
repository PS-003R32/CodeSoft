import math
import random

def genPass():
    PassLength = int(input("Enter the length of password you need: "))
    isLower = input("does the password includes Lower case? y/n: ")
    isUpper = input("does the password includes Upper case? y/n: ")
    isNum = input("does the password includes Numbers? y/n: ")
    isSymb = input("does the password includes special characters? y/n: ")

    allowedchr = ""
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = '1234567890'
    symb = "!@#$%^&**()~[]{}=-_+`/"
    genPass = ""

    if isLower == 'n' or isLower == 'N':
        pass
    else:
        allowedchr += lower
    if isUpper == 'n' or isUpper == 'N':
        pass
    else:
        allowedchr += upper
    if isNum == 'n' or isNum == 'N':
        pass
    else:
        allowedchr += num
    if isSymb == 'n' or isSymb == 'N':
        pass
    else:
        allowedchr += symb

    if PassLength <= 0:
        print("Password length must be atleast 1!!")
    if len(allowedchr) == 0:
        print("atleast one set of characters must be selected!!")
    for i in range(PassLength):
        rndIndex = math.floor(random.random() * len(allowedchr))
        genPass += allowedchr[rndIndex]

    print(genPass)

genPass()
