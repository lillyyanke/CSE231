##############################################################
#   Computer Project #7
#
#   Prompt for and open a file
#   Display menu
#   loop for invalid input
#   prompt for country/regime/integer
#   output regime history/allies/regime changes
#   display closing message when q is entered
#
##############################################################


import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy",\
        "Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():

    '''
    prompts for file name until file can be opened
    value: none
    returns: file pointer
    '''
    file = input('Enter a file: ')
        
    i=0
    while i ==0:
        try:
            fp = open(file,"r")
            i+=1
        except FileNotFoundError:
            #tries to open a file or prompts for a valid file name
            print("File not found. Please try again.")
            
            file = input('Enter a file: ')
                
    return fp


def read_file(fp):
    ''' 
    Reads a csv file and stores country names and political regimes
    value: file pointer
    returns: list of string, list of lists of ints
    '''
    country_names = []
    list_of_regime_lists = []
    reader = csv.reader(fp)
    next(reader,None)

    newList = []
    for line in reader:
        if line[1] not in country_names: #if the country isn't in list yet,
                                         # add it and create new empty list
                                         
            list_of_regime_lists.append(newList) #add previous countires
                                                 #regime list of ints
            country_names.append(line[1])
            newList = []
            newList.append(int(line[4]))
            
        else:
            newList.append(int(line[4])) #if country in list, add regime num
                                         #to current countries list
            
    list_of_regime_lists.append(newList) #add the last countries regime list
    
    list_of_regime_lists.pop(0) #get rid of first empty regime list (newList)
    
    return country_names,list_of_regime_lists
    
def history_of_country(country,country_names,list_of_regime_lists):
    ''' 
    Calculate dominant regime in a country
    value: country (str), list of countries (strs), list of list of ints
    returns: dominant regime (str)
    '''
    index = country_names.index(country) #figure out which index you want
    listt = list_of_regime_lists[index]  #to find the list of it's regimes
    
    closed = 0
    electAuto = 0
    electDemo = 0
    libDemo = 0
    regimeList = [closed, electAuto, electDemo,libDemo] #initialize to [0,0,0,0]
    
    for i in listt : #count how many times the country had each regimes
        if i == 0:
            regimeList[0] += 1
        elif i == 1:
            regimeList[1] += 1
        elif i == 2:
            regimeList[2] += 1
        elif i == 3:
            regimeList[3] += 1

    maxIndex = regimeList.index(max(regimeList)) #index of the most frequent regime

    if maxIndex == 0:
        return REGIME[0] #regimeList corresponds to REGIME list
    elif maxIndex == 1:
        return REGIME[1]
    elif maxIndex == 2:
        return REGIME[2]
    else:
        return REGIME[3]
       


def historical_allies(regime,country_names,list_of_regime_lists):
    ''' 
    Figure out which countries are historical allies/same political ideology
    value: str, list of str, list of lists of ints
    returns: sorted list of str
    '''
    allies = [] #empty list to add allies
    for i in range(len(country_names)):  
        currRegime = history_of_country(country_names[i],\
                                        country_names,list_of_regime_lists)
        #regime of current country in list
        if currRegime == regime: #if it matches to the same regime add it to the list
            allies.append(country_names[i])
         
    return allies 

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    ''' 
    figure out which country had the most coups in their history
    value: int, list of str, list of lists of ints
    returns: sorted list of tuples
    '''
    tups = [] #empty list for tuples
    for i in range(len(list_of_regime_lists)):
        change = 0 #number of times the country changed regimes
        tup = tuple() #empty tuple for current country
        for j in range(len(list_of_regime_lists[i])-1):
            #j is each regime num in curr countries list
            if list_of_regime_lists[i][j] != list_of_regime_lists[i][j+1]:
                #if the curr regime isn't == to the last regime there was a coup
                #so add 1 to change
                change += 1
        tup = (country_names[i],change) #make country and num of changes a tuple
        tups.append(tup) #add the tuple to the list
    
    tups.sort(key = itemgetter(1),reverse=True) #sort by second ele of tup and reverse
    top = int(top)
    return tups[0:top] #index the top countries
    
def main():
    # by convention "main" doesn't need a docstring
    fp = open_file()
    countryNames,listOfCountries = read_file(fp)
    print(MENU)
    option = (input("Input an option (Q to quit): ")).lower()
    while option != "q":
       
        if option == "1" :
            countryOption = input("Enter a country: ")
            
            while countryOption not in countryNames: #input error checking
                print("Invalid country. Please try again.")
                countryOption = input("Enter a country: ")
            history = history_of_country(countryOption,countryNames,\
                                         listOfCountries)
            if history == REGIME[0]:
                print("\nHistorically {} has mostly been a {}".\
                      format(countryOption,REGIME[0]))
            elif history == REGIME[1]:
                print("\nHistorically {} has mostly been an {}".\
                      format(countryOption,REGIME[1]))
            elif history == REGIME[2]:
                print("\nHistorically {} has mostly been an {}".\
                      format(countryOption,REGIME[2]))
            else:
                print("\nHistorically {} has mostly been a {}".\
                      format(countryOption,REGIME[3]))

        elif option == "2":
            regimeOption = input("Enter a regime: ")
            while regimeOption not in REGIME: #input error checking
                print("Invalid regime. Please try again.")
                regimeOption = input("Enter a regime: ")
        
            stringg = "" #add allies to a string so we can index out the last comma
            allies = historical_allies(regimeOption,countryNames,listOfCountries)
            print("\nHistorically these countries are allies of type:",regimeOption)
            print("\n")

            for j in allies:
                stringg = stringg + j + ", " #space and comma between each country

            print(stringg[0:-2]) #ignore the last comma and space

        elif option == "3":
            num = input("Enter how many to display: ")
            i=0
            while i==0:
                try:
                    coups = top_coup_detat_count(num, countryNames,listOfCountries)
                    print("\n{: >25} {: >8}".format("Country","Changes"))
                    print("\n")
                    for j in coups: #loop to format the output
                        print('{: >25} {: >8}'.format(j[0],j[1]))
                        i+=1
                
                except:
                    #error checking the input
                    print("Invalid number. Please try again.")
                    num = input("Enter how many to display: ")
                
          
        else:
            print("Invalid choice. Please try again.")
            option = (input("Input an option (Q to quit): ")).lower()
            continue
        print(MENU)
        option = (input("Input an option (Q to quit): ")).lower()
    
    
    print("The end.")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 
