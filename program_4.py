
#Display the contents of a text file in Reverse Order with Slicing
# Open file to read
with open("text_file_program4.txt", "r") as myfile:
   my_data = myfile.read()
# Reversing the data by passing -1 for [start: end: step]
rev_data=my_data[::-1]

# Displaying the reversed data
print('Reversed data',rev_data)


#Display the contents of a text file in Reverse Order by Looping

# Opening the file to read
my_data = open('text_file_program4.txt','r')

# reversing the data
for myLine in my_data:
   l = len(myLine)
   rev_data = ''

while(l>=1):
   rev_data = rev_data + myLine[l-1]
   l=l-1
# Displaying the reversed data
print("Reversed data = ",rev_data) 