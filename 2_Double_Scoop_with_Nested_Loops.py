#Task 1:
import random
moods = ["happy", "sad", "energetic", "calm", "playful", "morose", "mischievous", "excited", "overwhelmed"]# a list of moods 
weekdays = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # days of the week for print function later]
times_of_day = ["morning", "afternoon", "evening"] # times of the day when mood is recorded

for weekday in weekdays: #loop through the days of the week
    for time_of_day in times_of_day: #loop through the times of day when mood is recorded
        print(f"On {weekday} {time_of_day} you were {random.choice(moods)}") # output a randomly selected mood for the day and time of day indicated by the loops