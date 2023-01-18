#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numRods = float(input("Input rods: "))
print("You input ", numRods, " rods.")

meters = numRods*5.0292
feet = meters/.3048
miles = meters/1609.34
furlongs = numRods/40
minutes =60*( miles/3.1)


print("\nConversions\nMeters: ", round(meters,3),"\nFeet: ", 
      round(feet,3), "\nMiles: ", round(miles,3), "\nFurlongs: ",
      round(furlongs,3), "\nMinutes to walk ",numRods, " rods: ",round(minutes,3))
