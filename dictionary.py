#Add something that will number the definitions
#Go through bug fix 1 and 2 on udemy
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = word.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no:  " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "This is not in the dictionary"
        else:
            return "We didn't understand your query"
    else:
        return "This is not in the dictionary"

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

#
