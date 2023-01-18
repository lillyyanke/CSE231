#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Computer Project #2
#ask if they want to continue
#input car information
#output car information plus calculations
#ask if they want to continue or end

import math

print ("\nWelcome to Horizons car rentals. ")
print("\nAt the prompts, please enter the following: ")
print("\tCustomer's classification code (a character: BD, D, W) ")
print("\tNumber of days the vehicle was rented (int)")
print("\tOdometer reading at the start of the rental period (int)")
print("\tOdometer reading at the end of the rental period (int)")

answer = input("\nWould you like to continue (A/B)? ")

while answer == "A":
    
    custCode = input("\nCustomer code (BD, D, W): ")
    
    if custCode != "BD" and custCode != "D" and custCode != "W":
        print("\n\t*** Invalid customer code. Try again. ***")
        continue
    #invalid input, will prompt user for a diff code
    
    numDays = float(input("\nNumber of days: "))
    odometerStart = float(input("Odometer reading at the start: "))
    odometerEnd = float(input("Odometer reading at the end:   "))
    
    if odometerEnd<odometerStart:
        odometerEnd = odometerEnd + 1000000
    #correction for odometer dial being only 6 digits
        
    numWeeks = math.ceil(numDays/7) 
    #rounding up for partial weeks
    totalMiles = (odometerEnd-odometerStart)/10 
    #odometer recors 10ths of miles
    avgMilesDaily = totalMiles/numDays
    avgMilesWeekly = totalMiles/numWeeks
    
    if custCode == "BD":
        baseCharge = numDays * 40
        mileCharge = totalMiles * 0.25
    elif custCode == "D":
        baseCharge = numDays * 60
        if avgMilesDaily <=100:
            mileCharge = 0
        else: 
            mileCharge = 0.25*(totalMiles-(100*numDays))
    elif custCode == "W":
        baseCharge = 190 * (numWeeks)
        if avgMilesWeekly <= 900:
            mileCharge = 0
        elif avgMilesWeekly>900 and avgMilesWeekly<1500:
            mileCharge = numWeeks * 100
        else:
            mileCharge = (numWeeks * 200) + 0.25*(totalMiles-(1500*numWeeks))

        
    print("\nCustomer summary:")
    print("\tclassification code:",custCode)
    print("\trental period (days):",int(numDays))
    print("\todometer reading at start:",int(odometerStart))
    if odometerEnd>1000000:
        print("\todometer reading at end:  ",int(odometerEnd-1000000))
    else:
        print("\todometer reading at end:  ",int(odometerEnd))
    #correcting the print statement if the odometer went over 6 digits
    print("\tnumber of miles driven: ",totalMiles)
    print("\tamount due: $",float(mileCharge + baseCharge))
    
    answer = input("\nWould you like to continue (A/B)? ")
    
print("Thank you for your loyalty.")

 
    
    
    
    
    