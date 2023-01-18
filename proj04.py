#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:41:45 2022

@author: lillianyanke
"""
##################################################
#  Computer Project #4
#
#  Prompt for Z, C or to quit
#  Prompt for an integer 
#  Call functions
#  String to base 13 number
#  Expand base 13 number to tridecimal
#  Convert tridecimal to Conway float or return 0
#  OR calculate zeta function
###################################################



PROMPT = "Enter Z for Zeta, C for Conway, Q to quit: "

def int_to_base13(n):
    '''
    Converts an positive integer to a base 13 number
    value: n (non negative int)
    returns: base 13 number (string) 
    '''
    string = ""
    while n != 0:
        remainder = n%13
        quotient = n//13
        if remainder == 10:
            string += "A"
        elif remainder == 11:
            string += "B"        
        elif remainder == 12:
            string += "C"
        else:
            string += str(remainder)
        n = quotient
        #remainder from step 1 becomes new value
        #for current base 13 digit

    return(string[::-1]) #calculate digits L to R then reverse
        


def tridecimal_expansion(n_str):
    ''' 
    Converts base 13 num to trideciaml value
    value: basae 13 num (string)
    returns: tridecimal value (string)
    '''
    n_str = n_str.replace("A","+")
    n_str = n_str.replace("B","-")
    n_str = n_str.replace("C",".")
    return(n_str)
        

def tridecimal_to_conway(n_str):
    '''
    Converts tridecimal to conway float
    value: tridecimal (string)
    returns: conway float (float)
    '''
    i=0
    if len(n_str)==1:
        return 0
        #if n is length 1 it can't have a conway float
    try:
        for i in range(len(n_str)-1):
            try:
                #try to convert the tridecimal to a float
                #at each index
                n_float = float(n_str [i:])
                n_int = int(n_float)
                #check if the number is an integer
                #and if it is then return 0
                if n_int != n_float:
                    return(n_float)
                else:
                    return 0

            except:
                i+=1
                if i == (len(n_str)-1):
                    return 0 
                #return 0 if the loop has run through
                #the length of the string with no
                #Conway float calculated
                continue
    except:
        return 0


def zeta(s):
    ''' 
    Calculates Zeta function for s
    value: s (float)
    returns: sum (float)
    '''
    if s<=0:
        return None
    else:
        DELTA = 10**-7
        sum1 = 1
        i=2
        term = 1/i**s
        lastTerm = 0
        while abs(lastTerm - term) > DELTA:
            
            sum1 += term
            lastTerm = term
            #update lastTerm to be current term
            #to check if the difference is less than delta
            i = i + 1
            term = 1/i**s

        return sum1


def main():

    print("Functions")
    letter = ""
    while letter != "q":
        letter = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
        if letter == "z":
            print("Zeta")
            num = input("Input a number: ")
            while num.isalpha():
                #check if input is not a number and print an error if it is
                print("Error in input.  Please try again.")    
                num = input("Input a number: ")
            num = int(num) 
            print(zeta(num))
    
        elif letter == "c":
            print("Conway")
            num = input("Input a positive integer: ")
            while num.isdigit() == False:
                #check if num is a digit and positive
                print("Error in input.  Please try again.")    
                num = input("Input a positive integer: ")
            num = int(num)   
            print("Base 13:", int_to_base13(num)) #convert num to base13
            print("Tridecimal:", (tridecimal_expansion(int_to_base13(num))))
            #convert num to base 13 to tridecimal to conway float
            print("Conway float:",tridecimal_to_conway(tridecimal_expansion(int_to_base13(num))))
        elif letter == "q":
            continue
        #if q is entered the loop ends and thanks the user
        else:
            print("Error in input.  Please try again.")
        

      
    print("\nThank you for playing.")
        
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()
   
