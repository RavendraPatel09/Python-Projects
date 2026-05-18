s='Hello there>>djrnf'
clean=''#Initialize an empty string to store cleaned data
for x in s:#Iterate through each character in the string
    if x.isalpha() or x.isspace():#Check if the character is an alphabet or space
        clean+=x#Build the cleaned string
else:
    clean=clean+''    #Add an empty string at the end (optional)    
print('Cleaned string:',clean)
#this is the program to clean unwanted words from the string
  