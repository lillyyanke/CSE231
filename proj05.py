
###############################################################
# 
# Computer Project #5
#
# Prompt for a year
# open the corresponding file
# loop through each file line
# return average, max, min
# return best sufing time
#
###############################################################


def open_file():
    ''' 
    Prompt for year and open file
    value: none
    returns: file pointer
    '''
    file = input("Input a year: ")
    i=0
    while i ==0:
        try:
            fileName = "wave_data_"+file+".txt"
            fp = open(fileName,"r")
            i+=1
        except FileNotFoundError:
            print("File does not exist. Please try again.")
            file = input("Input a year: ")
    return fp


def get_month_str(mm):
    ''' 
    converts string representing a month to month abbreviation
    value: mm (str)
    returns: str
    '''
    if mm == "01":
        return "Jan"
    elif mm == "02":
        return "Feb"
    elif mm == "03":
        return "Mar"
    elif mm == "04":
        return "Apr"
    elif mm == "05":
        return "May"
    elif mm == "06":
        return "Jun"
    elif mm == "07":
        return "Jul"
    elif mm == "08":
        return "Aug"
    elif mm == "09":
        return "Sep"
    elif mm == "10":
        return "Oct"
    elif mm == "11":
        return "Nov"
    elif mm == "12":
        return "Dec"


def best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,best_hr,best_wvht,best_dpd):
    ''' 
    determine which day and time had the best surf
    value: str,str,int,float,float,str,str,int,float,float
    returns: str,str,int,float,float
    '''
    if hr<6 or hr >=19: #disregard night time wave data
        return best_mm,best_dd,best_hr,best_wvht,best_dpd
    else:
        if wvht>best_wvht:
            return mm,dd,hr,wvht,dpd
        elif wvht<best_wvht:
            return best_mm,best_dd,best_hr,best_wvht,best_dpd
        else:
            if dpd>best_dpd:
                return mm,dd,hr,wvht,dpd
            else:
                return best_mm,best_dd,best_hr,best_wvht,best_dpd
        

def main():  

    print("Wave Data")
    fp = open_file()
    mm = ""
    dd = ""
    hr = 0
    wvht = 0
    dpd = 0
    maxx = 0
    minn = 10**6
    best = 0
    total = 0
    count = 0
    fp.readline()
    fp.readline()
    best_mm = "01" #initializing best values
    best_dd = "01"
    best_hr = 0
    best_wvht = 0
    best_dpd = 0
    for line in fp:
        mm = line[5:7]
        dd = line[8:10]
        hr = int(line[11:13])
        wvht = line[30:36]
        if wvht == "99.00": #disregarding spurious values
            continue
        else:
            wvht = float(wvht)
        dpd = line[37:42]
        if dpd == "99.00":
            continue
        else:
            dpd = float(dpd)
        total = wvht + total
        count += 1
        if wvht > maxx:
            maxx = wvht
        elif wvht < minn:
            minn = wvht
        #call best surf function to compare data from each day    
        best_mm, best_dd, best_hr, best_wvht, best_dpd\
            = best_surf(mm,dd,hr,wvht,dpd,best_mm,best_dd,\
                        best_hr,best_wvht,best_dpd)
    average = total/count

  
    print("Wave Height in meters.") 
    print("{:7s}: {:4.2f} m".format("average",average))
    print("{:7s}: {:4.2f} m".format("max",maxx))
    print("{:7s}: {:4.2f} m".format("min",minn))
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}"\
          .format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s"\
          .format(get_month_str(best_mm), best_dd, best_hr, best_wvht, best_dpd))


        
        

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()