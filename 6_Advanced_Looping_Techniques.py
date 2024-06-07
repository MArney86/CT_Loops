# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

#Task 1: The Selective DJ
new_playlist = genres[1:4] #slice the 2nd through 4th elements in the genre list
for genre in new_playlist: #loop through the new list
    print(genre) #print the genres

#Task 2: The One-Liner Band with List Comprehensions

music_genres = [genre + " Music" for genre in genres] #comprehension that makes a new list that adds Music to the end of the genres in the original list 
print(music_genres) # print new list

#Task 3: Numerical Beats with range

for counter in range(10,0,-1): # Count down from 10
    print(counter) #print the count
print("The beat drops now!") # Notification of the drop