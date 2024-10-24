#Task 1: Your Mood Today
#Write a program that prints off different moods for each day of the week. 
import random
moods = ["happy", "sad", "energetic", "calm", "playful"]#A list of moods 
weekdays = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] #Days of the week for print function later

for x in range(7):#looping through the days of the week using range()
    print(f"On {weekdays[x]} you were felling {random.choice(moods)}") #randomly choosing the mood when printing the mood for that day of the week