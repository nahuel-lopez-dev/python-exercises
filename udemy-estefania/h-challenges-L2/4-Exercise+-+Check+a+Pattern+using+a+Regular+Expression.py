import re

regex = "^My[\w\s]+blue$"

string = input("Enter a string to check if a match is found: ")

if re.search(regex, string):
    print("Match")  
else:  
    print("No Match")  

