#######################################################################
#  Computer Project #8
#
#  open and read a file
#  store the data in a dictionary of dictionaries 
#  functions to manipulate master dictionary
#  main program loops 
#  prompts user for choices
#  displays data
#
#######################################################################



import json,string

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']
PUNCT = string.punctuation

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''

def get_option():
   ''' 
   prompts for valid option and returns it
   value: none
   returns: choice(str)
   '''
   choice = (input(MENU)).lower()
   #while choice is not an option reprompt for it    
   while choice != 'c' and choice != 'f' and choice != 'i' and choice != 'm'\
       and choice != 'w' and choice != 'q':        
       print("Incorrect choice.  Please try again.")     
       choice = (input(MENU)).lower()
       #returns lowercase choice
   return choice
   

    
def open_file(s):
   ''' 
   prompt for file name until opened
   value: string
   returns: fp
   '''
   file = input("Enter a {} file name: ".format(s))
      
   i=0
   while i ==0:
       try:
           fp = open(file)
           i+=1
       except FileNotFoundError:
           #tries to open a file or prompts for a valid file name
           print("File not found.  Try again.")
            
           file = input("Enter a {} file name: ".format(s))
                
   return fp
        
def read_annot_file(fp1):
   ''' 
   read file and turn it into a dict of dicts
   value:  fp
   returns: dictionary of dictionaries
   '''
   return json.load(fp1)

def read_category_file(fp2):
   ''' 
   put each line of a file in a dictionary
   value: fp
   returns: dictionary
   '''
   catDict = {}
   for line in fp2:
       strr = line.split()
       #keys are integers and values are categories
       catDict[int(strr[0])]=strr[1]
    
   return(catDict)


def collect_catogory_set(D_annot,D_cat):
   ''' 
   creates a set of the categories used in D_annot
   value: dictionaries of dictionaries, dictionary
   returns: set of strings
   '''

   sett = set()
   for key in D_annot:
       #go into each nested dictionary
       for num in D_annot[key]["bbox_category_label"]:
           sett.add(num)
           #add each categroy number to a set
   strSet = set()
   for  i in sett:
       strSet.add(D_cat[i])
       #add the corresponding category name for each number in the set

   return strSet

def collect_img_list_for_categories(D_annot,D_cat,cat_set):
   ''' 
   dictionary of lists of each instance when the category appears
   value: dictionary of dictionaries, dictionary, set of strings
   returns:  
   '''
   dictt = {}
   for i in cat_set:
       #empty list for each category name
       dictt[i]=[]
  
   for key in D_annot:
       for num in D_annot[key]["bbox_category_label"]:
           dictt[D_cat[num]].append(key)
           #add the category numbers to the empty list 
   for key in dictt:
       dictt[key].sort()
       #loop through each list in the dictionary and sort it
   return(dictt)

def max_instances_for_item(D_image):
   ''' 
   the most occurences of an object across all images
   value: dictionary of sorted lists
   returns: tuple
   '''
   maxx = max(D_image,key = lambda x:len(D_image[x]))
   #find the longest list in the dictionary
   lenn = len(D_image[maxx])
   #get the length of the longest list
    
   return(lenn,maxx)

def max_images_for_item(D_image):
   ''' 
   the most images an object appears
   value: dictionary of sorted lists
   returns: tuple
   '''
   
   dictt = D_image
   for key in dictt:
       dictt[key] = set(dictt[key])
       #add to a set so no repeating numbers
   for key in dictt:
        dictt[key] = list(dictt[key])
        #conver the set to a list
  
   maxx = max(D_image,key = lambda x:len(D_image[x]))
   #find the longest list in the dictionary
   lenn = len(D_image[maxx])
   #get the length of the longest list
    
   return(lenn,maxx)

def count_words(D_annot):
   '''
   counts the occurences of words in captions
   value: dictionary of dictionareis
   returns: list of tuples
   '''
   words = {}
   for key in D_annot:
       for caption in D_annot[key]["cap_list"]:
           #get each caption
           cap = caption.split()
           #split each line into list of strings
           for word in cap:
               word = word.strip()
               #strip the line of puncuation and paces
               word = word.strip(PUNCT)
               
               if word in STOP_WORDS:
                   #dont include boring words
                   continue
               try:
                   int(word)
                   #if the word can be turned into an int then skip it
               except:
                  
                   if word not in words:
                       #new word not in list
                       words[word]=1
                   else:
                       #word already in list, count goes up 1
                       words[word]+=1

   tups = [(k,v) for v,k in words.items()]
   #list of tuples
   tups.sort(key = lambda x: x[1])
   #sort and reverse the list of tuples by second element
   tups.sort(reverse = True)
   return(tups)



def main():  
    print("Images\n")
    s = "JSON image"
    dictt = read_annot_file(open_file(s))
    d = "category"
    #call al functions
    dictt2 = read_category_file(open_file(d))
    catSet = collect_catogory_set(dictt,dictt2)
    catDictList = collect_img_list_for_categories(dictt,dictt2,catSet)
    option = get_option()
    maxx = max_instances_for_item(catDictList)
    max2 = max_images_for_item(catDictList)
    wordList = count_words(dictt)
    
    while option != "q":
        if option == "c":
            print("\nCategories:")
            listt = []
            strr = ""
        
            for i in dictt2:
                if dictt2[i] in catSet:
                    listt.append(dictt2[i])
                    #only append the categories in the image
            listt.sort()
            for j in listt:
                strr += j +", "
            print(strr[:-2])
        
        elif option == "f":
            print("\nCategories:")
            listt = []
            strr = ""
            for i in dictt2:
                if dictt2[i] in catSet:
                    listt.append(dictt2[i])
                #ponly append the categroies in the image
            listt.sort()
            for j in listt:
                strr += j +", "
            print(strr[:-2])
            #ignore the last comma and space
            choice = (input("Choose a category from the list above: ")).lower()
            #reprompt for invalid input
            while choice not in listt:
                print("Incorrect category choice.")
                choice = (input("Choose a category from the list above: ")).lower()
            list2 = catDictList[choice]
            #list of chosen category
            sortList2 = []
            string2 = ""
            for i in list2:
                sortList2.append(int(i))
                #new list of ints to sort and return
            sortList2.sort()
            
            for j in sortList2:
                string2 += str(j) + ", "
            print("\nThe category {} appears in the following images:".format(choice))
            print(string2[:-2])
            #ignore the last comma and space
        elif option == "i":
            print("\nMax instances: the category {} appears {} times in images.".format(maxx[1],maxx[0]))
        
        elif option == "m":
            print("\nMax images: the category {} appears in {} images.".format(max2[1],max2[0]))
        
        elif option == "w":
            num = int(input("\nEnter number of desired words: "))
            #reprompt if invalid input
            while num < 0:
                print("Error: input must be a positive integer: ")
                num = int(input("\nEnter number of desired words: "))
            print("\nTop {} words in captions.".format(num))
            print("{:<14s}{:>6s}".format("word","count"))
            for i in range(num):
                tupp = wordList[i]
                #for i in choice number of words
                print("{:<14s}{:>6d}".format(tupp[1],tupp[0]))
        
        option = get_option()

    print("\nThank you for running my code.") 
    
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()     