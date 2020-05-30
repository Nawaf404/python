# False = Incorrect or NO
# True = Correct or Yes
num1 = 5
num2 = 6
print("-------Bigger------")
print(num1 > num2)
print("..................")
print(num1 < num2)
print("--------smaller----")
print(5 > 6) # without Variable

print(5 == 5) # is 5 equal 5 ? yes
print(5 == 6) # is 5 equal 6 ? no

print(5 != 6) # is 5 dosen't equal 6 ? yes

print (5 >= 6) # is 5 equal or bigger 5 ? . NO { now will see first condition, is bigger ? no, then, is equal ? yes }
print(7 >= 6)
print(5 <= 6)

# Logical Opreation { and , or }
 # and
print(True and True) # 1 1 will output True
print(True and False) # 1 0 , first True and False will be False
print(False and False) # False
 
 # or
print(True or True) # True
print(True or False) # true
print(False or False) # False

# not

print(not True) # False, maybe not logical
print(not False) # sure True !

a,b = 1,2
print(a) # will print 1 because a is the first
print(b)
 # and
print(a == a and b == b) # true
print(a == a and b > a) # flase
print(a>b and b<a)
print(a<b and b > a)

# or
print(a == a or b == a)
print(a == a or b < a)
print(a > b or b < a) # false

# not

print(not (a != 5)) # true
print(not (a == 5)) # true)
# CTRL + / 
# will be commited multi lines