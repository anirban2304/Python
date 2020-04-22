import json
import difflib

data_dictionary = json.load(open("Custom_Dictionary/data.json"))

def return_meaning(word):
    if word in data_dictionary:
        return data_dictionary[word]
    elif word.title() in data_dictionary:
        return data_dictionary[word.title()]
    elif word.upper() in data_dictionary:
        return data_dictionary[word.upper()]
    elif len(difflib.get_close_matches(word, data_dictionary.keys())) > 0:
        question =  "Did you mean %s. Press Y for Yes and N for No: " %(difflib.get_close_matches(word, data_dictionary.keys())[0])
        answer = input(question)
        if answer == 'Y':
           # print("Yes entered")
            return (return_meaning(difflib.get_close_matches(word, data_dictionary.keys())[0]))
        elif answer == "N":
            return ("Sorry no match found")
        else:
            return "We didn't understand your response"
    else:
        return "Word was not found, try another word"

user_input = input("Enter a word: ")
store_meaning = return_meaning(user_input.lower())
if type(store_meaning) == list:
    for meaning in store_meaning:
        print(meaning)
else:
    print(store_meaning)
