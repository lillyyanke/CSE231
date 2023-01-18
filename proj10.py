###########################################################
#  Computer Project #10
#
#  Allows user to play Streets and Alleys
#    prompt for a menu option
#    check validity of move
#    move the card if valid
#    undo previous move if user enters U
#    display the menu if H
#    restart game if R
#    quit and end game if Q
# 
###########################################################
 
#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''
                
def initialize():
    '''
    creates tableau and foundation
    value: none
    returns: tuple
    '''
    foundation = [[],[],[],[]]
    #initialize empty list of lists
    tableau = [[],[],[],[],[],[],[],[]]
    stock = cards.Deck()
    stock.shuffle()
    for i in range(8):
        if i%2 == 0:
            for j in range(7):
                #even rows get 7 cards
                tableau[i].append(stock.deal())
        else:
            for j in range(6):
                #odd rows get 6 cards
                tableau[i].append(stock.deal())
    return (tableau,foundation)


def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
    
          
def valid_tableau_to_tableau(tableau,s,d):
    '''
    true if valid move, false otherwise
    value: data structure representing tableu, int, int
    returns: bool
    '''
    
    if len(tableau[d]) == 0:
        return True
    #if the tableau is empty the move is always valid
    try:
        source = tableau[s][len(tableau[s])-1]
        destination = tableau[d][len(tableau[d])-1]
        #if the source is empty the move is invalid
    except:
        return False

    if len(tableau[d])== 0:
        return True
    elif source.rank() + 1 == destination.rank():
        #valid if the source rank is one less than the destination
        return True
    else:
        return False
    
    
def move_tableau_to_tableau(tableau,s,d):
    '''
    updates tableau if valid move otherwise do nothing
    value: data structure representing tableu, int, int
    returns: bool
    '''
    if valid_tableau_to_tableau(tableau,s,d):
        tableau[d].append(tableau[s][-1])
        tableau[s].pop(-1)
        #if the move is valid move it and remove it from source
        return True
    else:
        return False
      

def valid_foundation_to_tableau(tableau,foundation,s,d):
    '''
    true if valid move, false otherwise
    value: data structure representing tableu, foundation, int, int
    returns: bool
    '''
    if len(tableau[d]) == 0:
        return True
    #always valid if empty tableau
    try:
        destination = tableau[d][len(tableau[d])-1]
        source = foundation[s][len(foundation[s])-1]
        #if the source card doesn't exist its invalid
    except:
        return False

    if len(tableau[d])== 0:
        return True
    elif source.rank() + 1 == destination.rank():
        #valid if source rank one less than destination
        return True
    elif destination.suit() == source.suit() and source.rank() + 1 == destination.rank():
        return True
    else:
        return False
    
    

def move_foundation_to_tableau(tableau,foundation,s,d):
    '''
    updates tableau if valid move otherwise do nothing
    value: data structure representing tableu,foundation, int, int
    returns: bool
    '''
    
    if valid_foundation_to_tableau(tableau,foundation,s,d):
        tableau[d].append(foundation[s][-1])
        foundation[s].pop(-1)
        #if valid add it to tableau and remove from source
        return True
    else:
        return False
    

def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''
    true if valid move, false otherwise
    value: data structure representing tableu,foundation, int, int
    returns: bool
    '''

    try:
        source = tableau[s][len(tableau[s])-1]
        if len(foundation[d]) == 0 and (tableau[s][-1]).rank() == 1:
            #valid if the foundation is empty and the source card is an ace
            return True
        else:
            
            destination = foundation[d][len(foundation[d])-1]
            if destination.suit() == source.suit() and source.rank() - 1 == destination.rank():
                #valid if same suit and source rank is one higher than destination rank
                return True
            else:
                return False
    except:
        return False


def move_tableau_to_foundation(tableau, foundation, s,d):
    '''
    updates foundation if valid move otherwise do nothing
    value: data structure representing tableu,foundation, int, int
    returns: bool
    '''
    if valid_tableau_to_foundation(tableau,foundation,s,d):
        foundation[d].append(tableau[s][-1])
        tableau[s].pop(-1)
        #if valid move and remove
        return True
    else:
        return False
    

def check_for_win(foundation):
    '''
    checks if foundation is full
    value: data structure representing foundation
    returns: bool
    '''

    count = 0
    for i in range(len(foundation)):
        for j in foundation[i]:
            count+=1
            #counts the cards in the foundation
    if count == 52:
        return True
    else:
        return False

def get_option():
    '''
    prompts for input and checks if valid and returns option in a list
    value: none
    returns: list
    '''
   
    option = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): ").upper()
    option = option.split()
    #splits option into list
    if len(option) > 1:
        #if mxx num num was entered turn num strings to ints
        option[1] = int(option[1])
        option[2] = int(option[2])
        
    if option == ["U"] or option == ["R"] or option == ["H"] or option == ["Q"]:
        return option
    
    elif option[0] == "MTT" or option[0] == "MTF" or option[0] == "MFT":
        if option[0] == "MTT"  :    
            if option[1] < 0 or option[1] > 7 or type(option[1]) != int:
                #if source row does not exist
                print("Error in Source.")
                return None
            elif option[2] < 0 or option [2] > 7 or type(option[2]) != int:
                #if destination row does not exist
                print("Error in Destination")
                return None
            else:
                return option
            
        elif option[0] == "MTF":
            if option[1] < 0 or option[1] > 7 or type(option[1]) != int:
                print("Error in Source.")
                return None
            elif option[2] < 0 or option [2] > 3 or type(option[2]) != int:
                print("Error in Destination")
                return None
            else:
                return option
            
        elif option[0] == "MFT":
            if option[1] < 0 or option[1] > 3 or type(option[1]) != int:
                print("Error in Source.")
                return None
            elif option[2] < 0 or option [2] > 7 or type(option[2]) != int:
                print("Error in Destination")
                return None
            else:
                return option
        
        
    else:
        print("Error in option:",option)
        return None

def main():  

    print("\nWelcome to Streets and Alleys Solitaire.\n")
    tab,found = initialize()
    display(tab,found)
    print(MENU)
    option = get_option()
    moves = []
    #keep track of moves to undo

    while option != ['Q']:

        if option == None:
            option = get_option()
            #invalid option --> reprompt for option
        elif len(option) == 3:
            choice = option[0]
            source = option[1]
            dest = option[2]
            if choice == "MTT":
                if valid_tableau_to_tableau(tab,source,dest):
                    #if valid move the card
                    move_tableau_to_tableau(tab,source,dest)
                    moves.append(tuple(['MTT',source,dest]))
                    #add move to previous moves list
                else:
                    print("Error in move: {} , {} , {}".format(choice,source,dest))
                    #if not valid error message and get new option
                    option = get_option()
                    continue
           
            elif choice == "MTF":
                if valid_tableau_to_foundation(tab,found,source,dest): 
                    #if valid move the card
                    move_tableau_to_foundation(tab,found,source,dest)
                    moves.append(tuple(['MTF',source,dest]))
                    #add move to previous moves list
                    
                else:
                    print("Error in move: {} , {} , {}".format(choice,source,dest)) 
                    #if not valid error message and get new option
                    option = get_option()
                    continue
                
            elif choice == "MFT":
                if valid_foundation_to_tableau(tab,found,source,dest):   
                    #if valid move the card
                    move_foundation_to_tableau(tab,found,source,dest)
                    moves.append(tuple(['MFT',source,dest]))
                    #add move to previous moves list
                    
                else:
                    print("Error in move: {} , {} , {}".format(choice,source,dest))
                    #if not valid error message and get new option
                    option = get_option()
                    continue
    
            if check_for_win( found ):
                print("You won!")
                display(tab,found)
                print("\n- - - - New Game. - - - -\n")
                tab,found = initialize()
                display(tab,found)
                print(MENU)
                option = get_option()                
            else:
                display(tab,found)
                option = get_option()
        
        elif option == ['R']:
            #reshuffle deck and display new cards
            tab,found = initialize()
            display(tab,found)
            option = get_option()
        
        elif option == ['H']:
            print(MENU)
            option = get_option()
            
        elif option == ['U']:
            if len(moves)==0:
                print("No moves to undo.")
                option = get_option()
                
            else:
                last = moves.pop()
                option = last[0]
                source = last[1]
                dest = last[2]
                print("Undo:",option,source,dest)
                if option == 'MTT':
                    tab[source].append(tab[dest].pop())
                    #add last moved card back 
                elif option == 'MTF':
                    tab[source].append(found[dest].pop())
                    #add last moved card back
                else:
                    found[source].append(tab[dest].pop())
     
            
        else:
            print("Error in option:",option)
            option = get_option()
        
    print("Thank you for playing.")    
            
    

if __name__ == '__main__':
     main()