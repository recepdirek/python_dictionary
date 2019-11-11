import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in  data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? press Y for YES or N for NO :" % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word does not exist. please check it again"
        else:
            return "we didnt understand you"
    else: 
        return "document does not exist"

myword = input ("enter a word: ")
output = translate(myword)

if type(output) == list:
    for item in output:
        print (item)

else: 
    print (output)



