#https://repl.it/join/grmsdfwg-ericvigil
#Chosing action based on whether an expression is true or false:
#TrueValue if Expression else FalseValue
print ("True if 2==2 else false:   ","True" if 2==2 else "False")
print ("True if 2==3 else false:   ","True" if 2==3 else "False")
#(FalseValue, TrueValue) [Expression]
print ("(False, true) [2==3]):   ",("False", "true") [2==3])

#Python Arithmetic Operators
#+, -, ,* ,/ add, subtract, multiply, divide
#% mod function -- returns remainder when dividing two #s
#This is useful for checking for odd/even #%2 = 0 for even 1 for odd  
print ("even if (5 % 2==0) else odd returns ","even" if (5 % 2==0) else "odd")
print ("even if (4 % 2==0) else odd returns ", "even" if (4 % 2==0) else "odd")

# // oposite of mod % only gives whole number no remainder
print ("5 // 2 is ",5 //2 )
print ("5 % 2 is ", 5 % 2)
# so to show fractions:
print ("5/2 is ", 5//2," ", 5%2, "/ 2")
# ** exponential function 
print ("5 ** 2 is ", 5 ** 2)

#  == checks to see if two values are equal
print ("4==5 is ", 4 ==5)
# != checks to see if two values are NOT equal
print ("4!=5 is ", 4!=5)
# >, < >=, <= compares two values
print ("4 < 5 is ", 4 < 5)
# and checks to see if both values are True
print ("4<5 and 4==5 is ", 4<5 and 4==5)
# or checks to see if ONE value is True
print ("4<5 or 4==5 is ", 4<5 or 4==5)
# not negates an answer if True, then makes false
print ("not(4<5 or 4==5) is ", not(4<5 or 4==5))