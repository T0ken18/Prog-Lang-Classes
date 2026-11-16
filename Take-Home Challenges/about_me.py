"""
Write a short program called about_me.py that stores five
facts about you in well-named variables, prints them in
complete sentences using f-strings, and has a comment above
each part explaining what it does.
"""

# Declaring each variable. The left side is the variable or "facts" and the right side is the value of the facts
distro = "Arch Linux"
tetrisRecord = 503827
peakAVG = 91.11
favAnime = "Hunter x Hunter"
musicGenre = "Punk rock"

# Prints the the 5 facts.
# The sentences inside the double quotation marks are what gets printed in the terminal.
# The variables within the curly braces are replaced with whatever value it stored
# the "f" character turns the line into an f-string which allows us to use the curly braces the way it is
print(f"My laptop's operating system is not Windows. I use {distro}")
print(f"I am the top 113 player in the Philippines in blitz tetris with the score of {tetrisRecord}")
print(f"My highest average last school year was first semester with an average of {peakAVG}")
print(f"My favorite anime is {favAnime}")
print(f"The kind of songs I like listening to the most is {musicGenre}")