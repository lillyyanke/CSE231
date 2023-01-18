###########################################################################
# Computer Project #6
#
# reads a csv file
# manipulate master list of songs w diff functions
# loop for correct input
# call correct function
# output manipulated list
# prompt for correct input
#
###########################################################################




import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

def get_option():
    '''
    prompt for valid input and return it
    value: none
    returns: string
    '''
    print(OPTIONS)
    
    option = input(PROMPT).lower()
    
    while option != "a" and option !="b" and option != "c" and option != "d"\
        and option != "e" and option != "q":
        print('Invalid option!\nTry again')
        option = input(PROMPT).lower()
        
    return option

def open_file():
    '''
    prompts for file name until file can be opened
    value: none
    returns: file pointer
    '''
    file = input('Enter a file name: ')
    
    i=0
    while i ==0:
        try:
            fp = open(file,"r")
            i+=1
        except FileNotFoundError:
        #tries to open a file or prompts for a valid file name
            print('\nInvalid file name; please try again.\n')
            file = input('Enter a file name: ')
            
    return fp


def read_file(fp):
    '''
    read file and put each song into a list and add to a master song list
    value: file pointer
    returns: sorted list of lists
    '''
    masterList = []
    reader = csv.reader(fp)
    next(reader,None)
    
    for line in reader:
        try:
            line[2] = int(line[2]) 
        except:
            line[2] = -1 #changes empty data entries to -1
        try:
            line[3] = int(line[3])
        except:
            line[3] = -1
        try:
            line[4] = int(line[4])
        except:
            line[4] = -1
        try:
            line[5] = int(line[5])
        except:
            line[5] = -1
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])
        listt = [line[0],line[1],line[2],line[3],line[4],line[5]]
        masterList.append(listt)
        
    return masterList
    

def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    '''
    select christmas songs from master list and return a list of only
    christmas songs sorted alphabetically
    value: list of lists
    returns: list of lists
    '''
    xmasList = []
    
    for line in master_list:
        title = line[0]
        title = title.lower()
        for i in CHRISTMAS_WORDS:
            if i in title: #goes through each word in the title
                xmasList.append(line) #if it has a xmas word in it, 
                                      #its added to xmas song list
                
    return sorted(xmasList)
    
            
def sort_by_peak(master_list):
    '''
    sorts master list by peak rank in increasing order
    value: list of lists
    returns: list of lists
    '''
    rankList = []
    
    for line in master_list:
        if line[4]==-1: #skips over empty data entries
            continue
        else:
            rankList.append(line) 
    rankList = sorted(rankList,key = itemgetter(4)) 
    
    return rankList

def sort_by_weeks_on_list(master_list):
    '''
    sorts the master list by weeks on top 100 in decreasing order
    value: list of lists
    returns: list of lists
    '''
    weekList = []
    newMaster = master_list[::-1] #flips master_list so that ties
                                  #are correctly organized
    for line in newMaster:
        if line[5]==-1: #skips over empty data entries
            continue
        else:
            weekList.append(line)

    weekList = sorted(weekList,key = itemgetter(5))
    
    return weekList[::-1] #flips list to decreasing order

    
def song_score(song):
    '''
    calculates the overall rank of a song based on peak rank, curr rank
    and weeks on top 100 list
    value: song (list)
    returns: float
    '''
    peak_rank = int(song[4])
    
    if peak_rank == -1:
        peak_rank = -100
    else:
        peak_rank = 100 - int(song[4]) #reverses the rank
   
    rank_delta = int(song[2]) - int(song[3])
    weeks_on_chart = int(song[5])
    rank = int(song[2])

    if rank == -1:
        curr_rank = -100
    else:
        curr_rank = 100 - int(song[2]) #reverses the rank
    
    score = A * peak_rank + B * rank_delta + C * weeks_on_chart\
        + D * curr_rank
    
    return score

def sort_by_score(master_list):
    '''
    sorts master list ranked by the value of score_song function
    value: list of lists
    returns: list of lists
    '''
    
    scoreList = []
    master_list.sort() #sorts master list in alphabetical order
    newMaster = master_list[::-1] #sorts master list in reverse alphabetical 
                                  # order so ties are sorted by song name in 
                                  #reverse order
    
    for line in newMaster:
        score = song_score(line)
        line.append(score)
        scoreList.append(line)
        
    scoreList = sorted(scoreList,key = itemgetter(6),reverse = True)  
    #sorts score list by score
    for line in scoreList:
       del line[6] #deletes the score so it wont show up in the output
      
    return scoreList
        
    
def main():
    print("\nBillboard Top 100\n")
    
    masterList = read_file(open_file())  
    print_data(masterList)
    answer = get_option()
    
    while answer != "q":
        
        if answer == "a":
            
            christmasSongs = get_christmas_songs(masterList)
            print_data(christmasSongs)
            percent = 100*((len(christmasSongs))/len(masterList))
            #percentage of christmas songs to total songs
            if percent == 0:
                print('None of the top 100 songs are Christmas songs.')
            else:    
                print('\n{:d}% of the top 100 songs are Christmas songs.'.format(int(percent)))
                
        elif answer == "b":
            print_data(sort_by_peak(masterList))
            #sorts master list by peak song rank
        elif answer == "c":
            print_data(sort_by_weeks_on_list(masterList))
            #sorts master list by weeks on list
        elif answer == "d":
            print_data(sort_by_score(masterList))
            #sorts master list by calculated score
        answer = get_option()
        
    print("\nThanks for using this program!\nHave a good day!\n")
            

# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           