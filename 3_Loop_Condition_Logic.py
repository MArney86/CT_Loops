import random
#Task 1: Loop Condition Exploration
i=1
while i > 0: #a condition that will never evaluate false in the loop
    if i > 5: #control mechanism to stop loop after 5 iterations
        break
    else:
        print("This is an infinite loop!") #output
        i += 1 #increment i to keep track of loop iterations
#Task 2: Conditional Exit
i=1
kill_number = random.randint(1,100) #randomized stop point
while i < kill_number: #loop condition that will eventually be false
    print("This is a fininte loop!") #output
    i += 1 #increment i so conditions can be met and iterations tracked