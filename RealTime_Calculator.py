#Importation of Modules for Function
import time
import os
import random
import math
from datetime import datetime
import calendar
from decimal import Decimal

#Essential Functions
def d():pass
d = datetime.utcnow()
def UTCH():pass
UTC = ('Null')
def Usr_Loct_Slt():pass
Usr_Loct_Slt = 0
def Usr_Long():pass
Usr_Long = 180
def UTCM():pass
UTCM = 00

#Defining Final Output Functions
def Hours():pass
Hours = 00
def Minutes():pass
Minutes = 00

#Non-Essential Functions (For Menus, UI fashinoning(?), e.t.c.)
def BGN_Var():pass
BGN_Var = ('begin by')
def Doing_Var():pass
DOING_Var = ('ing')

#Enables Debug, Disables any timers in software as well as flashy bits
def Dev():pass
Debug = 0

if Dev == 1: 
    WaitTime = 0
    BGN_Var = ('')
    DOING_Var = ('')

print ("Hello and welcome to the Real Time Calculator.")
while UTC == ('Null'):
    print('Please enter Current UTC time with a 24 hour format')
    UTCH = input('Hours >')
    UTCM = input('Minutes >')
    if UTCH == ('Dev'):
        Debug = 1
        UTC = ('Null')
    else:
        UTC = 1
while Usr_Loct_Slt == 0:
    print('Please enter your longitude (without letters)')
    Usr_Long = (input('>'))
    if Debug ==1:
        print (Usr_Long)
    Usr_Long = (Usr_Long)
    if Debug == 1:
        print (Usr_Long)
    Usr_Loct_Slt = 1
    
Usr_Long = float(Usr_Long)
Usr_Long = (int(Usr_Long))+180
Usr_Long = ((Usr_Long)/360)*24
if Debug == 1:
    print (Usr_Long)
Hours = int(math.floor(Usr_Long))
if Debug == 1: 
    print (Hours)
Minutes = (Usr_Long) - (Hours)
if Debug == 1:
    print (Minutes)
Minutes = (Minutes)*60
if Debug == 1:
    print (Minutes)
Minutes = int(Minutes)
#Rounding
if Debug == 1:
    print (Hours)
    print (Minutes)
Hours = (Hours) + int(UTCH)
Minutes = (Minutes) + int(UTCM)
while Minutes >= 60:
    Minutes = (Minutes)-60
    Hours = Hours + 1
while Hours >= 24:
    Hours = (Hours)-24
print ('Your time is' ,Hours, ':', Minutes, ' (in a 24 hour format) based on our calculations')
