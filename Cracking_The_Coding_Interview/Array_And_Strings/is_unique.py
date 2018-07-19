# Coded by Jing Kun Ting
# Cracking the Coding Interview
# Question 1.1
# Coded on 19 July 2018

def is_unique(specific_string):

    index = 0

    for character in specific_string:
        if character in specific_string[index+1:]:
            return False
        
        index += 1
        
    return True


print("Enter a string: ")
string = input()

if (is_unique(string)):
    print("This string is unique")

else:
    print("This string is not unique")