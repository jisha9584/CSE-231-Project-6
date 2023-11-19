###########################################################
#  Computer Project #6
#
#  Print the welcome statements 
#    define functions
#       1. open file
#       2. read file
#       3. get characters by criterion
#       4. get characters by criteria
#       5. get region list
#       6. sort characters
#       7. display characters
#       8. get option
#    define main
#       call open file
#       call read file
#       call get option and loop until 4 is entered:
#           1. this option will be coded to get all available regions.
#           2. this option will filter characters by a certain criteria. 
#           3. this option will filter characters by element, weapon, and rarity.
#           4. this option breaks the loop and quits the program.
###########################################################

import csv
from operator import itemgetter

NAME = 0
ELEMENT = 1
WEAPON = 2
RARITY = 3
REGION = 4

MENU = "\nWelcome to Genshin Impact Character Directory\n\
        Choose one of below options:\n\
        1. Get all available regions\n\
        2. Filter characters by a certain criteria\n\
        3. Filter characters by element, weapon, and rarity\n\
        4. Quit the program\n\
        Enter option: "

INVALID_INPUT = "\nInvalid input"

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 1. Element\n\
                 2. Weapon\n\
                 3. Rarity\n\
                 4. Region\n\
                 Enter criteria number: "

VALUE_INPUT = "\nEnter value: "

ELEMENT_INPUT = "\nEnter element: "
WEAPON_INPUT = "\nEnter weapon: "
RARITY_INPUT = "\nEnter rarity: "

HEADER_FORMAT = "\n{:20s}{:10s}{:10s}{:<10s}{:25s}"
ROW_FORMAT = "{:20s}{:10s}{:10s}{:<10d}{:25s}"

def open_file():
    ''' 
    Open the promted file.
    Value: No argument.
    Return: file_pointer.
    '''
    file_pointer = input("Enter file name: ")
    while True:
        try:
            file_pointer = open(file_pointer, 'r')
            return file_pointer
        except FileNotFoundError:
            print("\nError opening file. Please try again.")
            file_pointer = input("Enter file name: ")    

def read_file(fp):
    '''
    This function reads the comma-separated value (csv) file using file pointer fp.
    fp: file pointer
    Return: the list of tuples
    '''
    file_pointer = csv.reader(fp)
    skip = next(file_pointer,None)
    
    master_list = []
    for line in file_pointer:
        name = line[0]
        element = line[2]
        weapon = line[3]
        rarity = int(line[1])
        region = line[4]
        region = region if region else None
        my_tuple = (name, element, weapon, rarity, region)
        master_list.append(my_tuple)
    return master_list

def get_characters_by_criterion (list_of_tuples, criteria, value):
    '''
    Given a list of character tuples, retrieve the characters that match a certain criteria. 
    List of tuples: used to retrive characters
    Criteria: to match them to the element, weapon and rarity
    Value: value is used to match it to the criteria 
    '''
    output_list = []
    for line in list_of_tuples:
        if line[criteria] == None:
            continue
        elif criteria == RARITY:
            if type(line[criteria]) == int and type(value) == int:
                if line[criteria] == value:
                    output_list.append(line)
        else:
            if type(line[criteria]) == str and type(value) == str:
                if value.title() == line[criteria].title():
                        output_list.append(line)     
    return output_list 
        
def get_characters_by_criteria(master_list, element, weapon, rarity):
    '''
    This function uses the list of tuples returned by the read file function, an element, a weapon, and a rarity and returns a list of tuples filtered using those 3 criterias.
    master_list: to take values from the master list in read file.  
    Element: a variable that stores the input for element and compares it to the master list
    Weapon: a variable that stores the input for element and weapon --> and compares it to the master list and sorts out the tuples based on the inputs.
    Rarity: a variable that stores the input for element, weapon and rarity --> and compares it to the master list and sorts out the tuples based on the inputs.
    '''
    for line in master_list:
        first= get_characters_by_criterion(master_list, ELEMENT, element)
        second= get_characters_by_criterion(first, WEAPON, weapon)
        third= get_characters_by_criterion(second, RARITY, rarity)       
    return third

def get_region_list(master_list):
    '''
    The master list of character tuples, retrieves all available regions into a list and no duplicates are allowed.
    Value: list of tuples
    Return: sorted list of strings
    '''
    region_list = []
    for line in master_list:
        region_in_function = line[4]
        if region_in_function == None:
            continue
        elif region_in_function not in region_list:
            region_list.append(region_in_function)  
    region_sorted= sorted(region_list)
    return region_sorted

def sort_characters (list_of_tuples):
    '''
    Create a new list where character tuples have been sorted --> the order of sorting is by decreasing rarity and alphabetically by name. 
    Value: list of tuples
    Return: sorted list of tuples
    '''
    return sorted(list_of_tuples, key = itemgetter(3), reverse = True)

def display_characters (list_of_tuples):
    '''
    Display the characters along with their information, using the formats. If a region has the value None, display 'N/A'.
    Value: list of tuples
    Return: nothing
    '''
    if list_of_tuples == []:
        print("\nNothing to print.")
    else:
        print(HEADER_FORMAT.format("Character", "Element", "Weapon", "Rarity",\
                                   "Region"))   
        display_characters = []
        for line in list_of_tuples:
            name = line[0]
            element = line[1]
            weapon = line[2]
            rarity = line[3]
            region = line[4]
            if region == None:
                display_characters= print(ROW_FORMAT.format(name, element,\
                                                            weapon, rarity,\
                                                                "N/A"))
            else:
                display_characters = print(ROW_FORMAT.format(name, element,\
                                                             weapon, rarity,\
                                                                 region))

def get_option():
    '''
    Prompt for input (MENU in the starter code). Ask for the input in the function. If the user enters a valid option (between 1 and 4), return the integer, otherwise print an error message.
    Value: nothing
    Return: int
    '''
    prompt = int(input(MENU))
    if (1<=prompt<=4):
        return prompt
    else:
        print(INVALID_INPUT)

def main():
    file_pointer = open_file() #Call open file function
    read = read_file(file_pointer) #Call read file function
    option = get_option() #Call get option function
    region = get_region_list(read) #Assign a variable to get region 

    while option != 4: #Loop until the user chooses 4
        if option == 1: #call a function to get all available regions
            print("\nRegions:")
            print(", ".join(region)) #Display all regions, separated by ", "

        elif option == 2:
            criteria_prompt = input(CRITERIA_INPUT) #Prompt for a criteria.
            while True:      
                try:
                    criteria_prompt = int(criteria_prompt)
                    if (1 <= criteria_prompt <= 4):
                        break
                    else: #if criteria is not an int between 1 and 4 (inclusive), print an error message and re-prompt for a criteria
                        print(INVALID_INPUT)
                        criteria_prompt = input(CRITERIA_INPUT)
                except ValueError:
                    print(INVALID_INPUT)
                    criteria_prompt = input(CRITERIA_INPUT)
        
            value_prompt = input(VALUE_INPUT) #Prompt for a value (use VALUE_INPUT in your prompt).
            if criteria_prompt == RARITY: #if criteria is RARITY, convert value to an int.
                while True:
                    try:
                        value_prompt = int(value_prompt)
                        break
                    except (TypeError, ValueError): #If it is not an int, print an error message and re-prompt.
                        print(INVALID_INPUT)
                        value_prompt = input(RARITY_INPUT)
            characters = get_characters_by_criterion(read, criteria_prompt,\
                                                     value_prompt) #Call get_characters_by_criterion to filter characters by a certain criteria with a value.
            sort_char = sort_characters(characters) #Sort characters using sort_characters
            display_characters(sort_char) #Display characters using display_characters

        elif option == 3: 
            #Prompt in this order for element, weapon, rarity; (use ELEMENT_INPUT, WEAPON_INPUT, RARITY_INPUT respectively)
            prompt_element = input(ELEMENT_INPUT)
            prompt_weapon = input(WEAPON_INPUT)
            prompt_rarity = input(RARITY_INPUT)
            while True:  
                try: #for RARITY convert value to an int
                    prompt_rarity = int(prompt_rarity) 
                    break
                except (TypeError, ValueError): #print an error message (use INVALID_INPUT) and re-prompt if it is not an int.
                    print(INVALID_INPUT)
                    prompt_rarity = input(RARITY_INPUT)
            characters = get_characters_by_criteria(read, prompt_element,\
                                                    prompt_weapon,\
                                                        prompt_rarity) #Call get_characters_by_criteria to filter characters by above criteria.
            sort_char = sort_characters(characters) #Sort characters using sort_characters
            dis_char = display_characters(sort_char) #Display characters using display_characters
        
        elif option == 4: #If option is 4 --> quit the program
            break
        
        option = get_option()

# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__":
    main()