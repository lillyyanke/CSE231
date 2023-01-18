#!/usr/bin/env python3
# -*- coding: utf-8 -*-
####################################################
# Computer Project #3
# Algorithm
# prompt for class year, specific college, credits,
# output tuition based on that info
# ask if they want to do another
####################################################

print("2021 MSU Undergraduate Tuition Calculator.\n")

again = "yes"
college = "none"
collegeEGR = "no"
collegeJM = "no"
tuition = 0

while again == "yes":
    
    level = input("Enter Level as freshman, sophomore, junior, senior: ")\
        .lower()
       
    while (level != "freshman") and (level != "sophomore") and \
        (level != "junior") and (level !="senior"):
        print("\nInvalid input. Try again.")
        level = input("Enter Level as freshman, sophomore, junior, senior: ")\
            .lower()
    #while loop for when invalid input is entered
    
    if (level == "freshman") or (level == "sophomore") or (level == "junior")\
        or (level =="senior"):
        if (level == "junior") or (level == "senior"):
            collegeInput = input\
("Enter college as business, engineering, health, sciences, or none: ").lower()
            
            if collegeJM != "yes":
                collegeJM = "no"
            if collegeInput == "business":
                college = collegeInput
                #changing the variable college if business, eng, health, or
                #sciences is entered so that if anything else is entered
                #college will remain "none"
            elif collegeInput == "engineering":
                college = collegeInput
            elif collegeInput == "health":
                college = collegeInput
            elif collegeInput == "sciences":
                college = collegeInput
            else:
                collegeJM = input \
                    ("Are you in the James Madison College (yes/no): ").lower()
                if collegeJM != "yes":
                    collegeJM = "no"
        
        else:
            collegeEGR = input\
                ("Are you admitted to the College of Engineering (yes/no): ").lower()
            if collegeEGR == "no":
                collegeJM = input \
                    ("Are you in the James Madison College (yes/no): ").lower()
            if collegeEGR != "yes":
                collegeEGR = "no"
            if collegeJM != "yes":
                collegeJM = "no"
            
    
    credit = input("Credits: ")
    if credit == "0":
        print("\nInvalid input. Try again.")
        credit = input("Credits: ")
        #if credit is 0 -> error message
    while credit.isdigit() == False:
        print("\nInvalid input. Try again.")
        credit = input("Credits: ")
        # if credit is str or float -> error message
    while (credit.isdigit() == True):
        credit = int(credit)
        if credit < 1:
            #if credit is less than 1 -> error message
            print("\nInvalid input. Try again.")
            credit = input("Credits: ")
        else:
            break
            
    if level == "freshman" and (college == "none" or collegeEGR == "yes"):
        #if they're a freshman and admitted to the college of EGR
        if credit < 12:
            tuition = tuition + (credit * 482)
        elif credit >= 12 and credit <19:
            tuition = tuition + 7230
        else:
            tuition = tuition + (7230 + ((credit-18)*482))
    elif level == "sophomore" and (college == "none" or collegeEGR == "yes"):
        #if they're a sophomore and admitted to the college of EGR
        if credit < 12:
            tuition = tuition + (credit * 494)
        elif credit>=12 and credit <19:
            tuition = tuition + 7410
        else:
            tuition = tuition + (7410 + ((credit-18)*494))
            
    elif (level == "junior" or level == "senior") and \
        (college == "none" or college == "health" or college == "science"):
        #if they're a upperclassman not in EGR or business
         if college == "health" or college == " sciences":
             if credit<4:
                 tuition = tuition +  50
             else:
                 tuition = tuition + 100
                                                        
         if credit < 12:
             tuition = tuition + (credit * 555)
         elif credit>=12 and credit <19:
             tuition = tuition + 8325
         else:
             tuition = tuition + (8325 + ((credit-18)*555) )
            
    elif (level == "junior" or level == "senior") and \
        (college == "business" or college == "engineering"):
         if college == "business":
             if credit < 4:
                 tuition += 113
             else:
                tuition += 226
         elif college == "engineering":
             if credit < 4:
                 tuition = tuition + 402
             else:
                tuition = tuition + 670
 
         if credit < 12:
             tuition = tuition + (credit * 573)
         elif credit>11 and credit <19:
             tuition = tuition + 8595
         else:
             tuition = tuition + (8595 + ((credit-18)*573) )
    if collegeEGR == "yes":
        if credit <=4:
            tuition = tuition + 402
        else:
            tuition = tuition + 670
            
    tuition+=24
    if credit>6:
        tuition+=5
        
    if collegeJM == "yes":
        tuition += 7.50
         
    
    print("Tuition is ${:,.2f}.".format(tuition))   
    
    tuition = 0
    #setting tuition back to 0 for the next calculation
    
    again = input("Do you want to do another calculation (yes/no): ").lower()
        
        