"""ADDITION OF TWO NUMBERES"""

a=input('Enter the value of a:')   #asking the user to input a value
b=input('Enter the value of b:')   #asking the user to input a value
c=int(a)+int(b)                    #addind both the values to give a integer value
print(c)                           #print command


"""ADDITION OF TWO STRINGS"""

x='AVI'                           #string1                       
y='NASH'                          #string2
z=x+y                             #string1+string2
print(z)                          #print command


"""IF CONDITION PROGRAM"""

a=int(input('Enter a value:'))    #asking for value from user
if a>0:                          #condition is a is greater than 0
    print("a is positive:")       #print command
if a<0:                          #condition is a is less than 0
    print ('a is negative')      #print command


"""IF-ELSE CONDITION PROGRAM"""

a=int(input('Enter a value:'))    #asking for value from user    
if a>0:                          #condition is greater than 0
    print('a is positive:')       #print command
elif a<0:                        #condition is less than 0
    print('a is negative:')       #print command
else:                            #if above if conditions are wrong then printing else statement
    print('zero')                #print command


"""RANDOM FUNCTION"""

import random                    #extracting random package
a=random.randint(1,100)          #generating number from 1 to 100
print(a)                         #print command




