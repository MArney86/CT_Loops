#Task 1: The for Loop DJ Set

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for genre in genres: #iterate through the genres with at for loop
    if genre == 'Jazz': #test what genre is cued up
        print(f"Track {genres.index(genre) + 1}: Jazz - Smooth rythms to relax the soul.") #print the genre and a custom message after the track number
    elif genre == 'Rock': #test what genre is cued up
        print(f"Track {genres.index(genre) + 1}: Rock - Screaming guitars and heavy drums to get the blood flowing!") #print the genre and a custom message after the track number
    elif genre == 'Hip-hop': #test what genre is cued up
        print(f"Track {genres.index(genre) + 1}: Hip-hop - Art and story-telling using the sounds of urban living and musical sampling") #print the genre and a custom message after the track number
    elif genre == 'Classical': #test what genre is cued up
        print(f"Track {genres.index(genre) + 1}: Classical - Insturmental music characterized by formality and complexity in musical form and the use of polyphony") #print the genre and a custom message after the track number

#Task 2: The Remix Artist with while

i = 0
while 1 < len(genres): #iterate the genres by index using a while loop
    if genres[i] == 'Jazz': #test what genre is cued up
        print(f"Track {i + 1}: Jazz - Smooth rythms to relax the soul.") #print the genre and a custom message after the track number
        i += 1 #iterate the loop
    elif genres[i] == 'Rock': #test what genre is cued up
        print(f"Track {i + 1}: Rock - Screaming guitars and heavy drums to get the blood flowing!") #print the genre and a custom message after the track number
        i += 1 #iterate the loop
    elif genres[i] == 'Hip-hop': #test what genre is cued up
        print(f"Track {i + 1}: Hip-hop - Art and story-telling using the sounds of urban living and musical sampling.") #print the genre and a custom message after the track number
        break #stop the loop if this genre is played
    elif genres[i] == 'Classical': #test what genre is cued up
        print(f"Track {i + 1}: Classical - Insturmental music characterized by formality and complexity in musical form and the use of polyphony.") #print the genre and a custom message after the track number
        i += 1 #iterate the loop

#Task 3: Light Show Technician Loop

for x in range(len(genres)): #looping using range()
    if genres[x] == 'Jazz' or genres[x] == 'Classical': #test to skip genres that don't pair well with lightshow
        continue #skip this iteration
    else:
        print(f"Track {x + 1}: light show is ready!") #print track number and message that light show is ready