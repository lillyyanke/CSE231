#######################################################################
#  Computer Project #8
#
#  open and read a file
#  store each line in a list
#  calculate per cappita diabetes rates
#  find min and max per capita values
#  display data by region w a for loop
#
#######################################################################



import csv
from operator import itemgetter

def open_file():
    
    '''
    prompts for file name until file can be opened
    value: none
    returns: file pointer
    '''
    
    file = input("Input a file: ")
      
    i=0
    while i ==0:
        try:
            fp = open(file,encoding = "utf-8")
            i+=1
        except FileNotFoundError:
            #tries to open a file or prompts for a valid file name
            print("Error: file does not exist. Please try again.")
            
            file = input('Input a file: ')
                
    return fp

def max_in_region(D,region):
    '''
    find max per capita diabetes in the region
    value: dictionary of lists
    returns: tuple (string,float)
    '''
    
    listt = D[region]
    maxx = max(listt, key = lambda x:x[3])
    #find max per capita which is at index 3
    return (maxx[0],maxx[3])
    

    
    
def min_in_region(D,region):
    '''
    find min per capita diabetes in the region
    value: dictionary of lists
    returns: tuple (string,float)
    '''
    
    listt = D[region]
    list2 = [i for i in listt if i[3] > 0.0]
    #get rid of 0.0 values bc 0.0 can't be the min

    minn = min(list2, key = lambda x:x[3])
    #find min per capita which is at index 3
    return (minn[0],minn[3])

def read_file(fp):
    '''
    read file and store each line as a dict of lists
    value: file pointer
    returns: dictionary of sorted list of lists
    '''
    
    reader = csv.reader(fp)
    header = next(reader,None)

    dictt = {}
    newList = []
    
    for line in reader:
        
        if line[1] not in dictt:
            #if the region is not in the dict already, add it and create a 
            #empty list to add each countries data
            try:
                newList = []
                #newList is list of countries in each region
                dictt[line[1]] = newList
                #add the country to the list
                newNewList = []
                #add countries data to a list
                newNewList.append(line[2])
                newNewList.append(float(line[9]))
                newNewList.append(float(line[5].replace(",","")))
                #replace population commas to convert to float
                newList.append(newNewList)
                #add the countries list to the regions list
            except:
                continue
        else:
            try:
                #if any of the values are blank then it won't be added to the list
                #add the country to the list if the region is already in the dict
                listt2 = []
                listt = dictt[line[1]]
                listt2.append(line[2])
                listt2.append(float(line[9]))
                listt2.append(float(line[5].replace(',','')))
                listt.append(listt2)
            except:
                continue
            
    for key in dictt:
        listtt = dictt[key]
        #loop through each region to sort alphabetically
        listtt.sort()
   
    return dictt

def add_per_capita(D):
    '''
    calculate diabetes per capita for each country and append to country's list
    value: dictionary of lists
    returns: dictinary of lists
    '''
    
    for key in D: 
        for val in D[key]:
            try:
                val.append(val[1]/val[2])
                #cases/population = per capita
            except:
                val.append(0.0)
    return D            
                
             
def display_region(D,region):
    '''
    display summary data for the region followed by a table of each countries data
    value: dictionary of lists, string
    returns: nothing
    displays: table of region data
    '''

    listt = D[region] #get list of specified region
    for i in listt:
        #each list in list
        if region in i:
            cases = i[1]
            population = i[2]
            perCapita = i[3]

    print("{:<37s} {:>9s} {:>12s} {:>11s}".format\
          ("Region","Cases","Population","Per Capita"))
    print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format\
          (region,cases,population,perCapita))
    print("\n{:<37s} {:>9s} {:>12s} {:>11s}".format\
          ("Country","Cases","Population","Per Capita"))
    
    listt.sort(key = itemgetter(3),reverse = True)
    #sort by per capita max to min
    
    for i in listt: 
        if i[0] == region:
            continue
        #don't include the region data in the table

        print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}"\
              .format(i[0],i[1],i[2],i[3]))
    
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*max_in_region(D,region)))
    
    
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*min_in_region(D,region)))    

    print("-"*72)

    
    
def main():
    fp = open_file()
    D = read_file(fp)
   
    D2 = add_per_capita(D)

    for key in D2:
        print("Type1 Diabetes Data (in thousands)")
        display_region(D2,key)
    
    print('\n Thanks for using this program!\nHave a good day!')

    
   


# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()