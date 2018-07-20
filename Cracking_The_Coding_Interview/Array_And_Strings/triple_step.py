# Coded by Jing Kun Ting
# Cracking the Coding Interview
# Question 8.1
# Coded on 19 July 2018

def triple_step(number_of_steps):

    # 1, 2 or 3 steps
    if number_of_steps < 0:
        return 0
    
    elif number_of_steps == 0:
        return 1

    else:
        return triple_step(number_of_steps-1) + triple_step(number_of_steps-2) + triple_step(number_of_steps-3)


print("Enter the number of steps: ")
number_of_steps = int(input())

answer = triple_step(number_of_steps)
print("The total number of steps are %d" % answer)