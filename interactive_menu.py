'''
python apprentice

write a program with a menu that has the following options:
    + accept and store a string
    + basic calculator (addition, subtraction, multiplication, division)
    + print the previously stored string
    + compare 2 numbers to determine the larger
    + remove a selected letter from a string
'''

def menu():
    print "[1] store a string"
    print "[2] print string"
    print "[3] basic calculator"
    print "[4] maximum"
    print "[5] remove letter from string"
    print "[m] print this menu"
    print "[q] quit"

def arithmetic(i, j, o):
    if o == "+":
        return i + j
    elif o == "-":
        return i - j
    elif o == "*":
        return i * j
    elif o == "/":
        return i / j
    else:
        return 0

def max(i, j):
    if i < j:
        return j
    else:
        return i

choice = ""

menu()
while choice != "q":
    choice = raw_input("[your choice]> ")
    if choice == "1":
        userStr = raw_input("enter a string> ")
    elif choice == "2":
        if userStr:
            print userStr
        else:
            print "no string stored"
    elif choice == "3":
        operator = raw_input("enter arithmetic operator> ")
        num1 = int(raw_input("enter first number> "))
        num2 = int(raw_input("enter second number> "))
        print arithmetic(num1, num2, operator)
    elif choice == "4":
        num1 = int(raw_input("enter first number> "))
        num2 = int(raw_input("enter second number> "))
        print max(num1, num2)
    elif choice == "5":
        newStr = ""
        userStr = raw_input("enter a string> ")
        letter = raw_input("enter letter to remove> ")
        for char in userStr:
            if char != letter:
                newStr += char
        print newStr
    elif choice == "m":
        menu()

