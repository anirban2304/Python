import json
import difflib

data_dictionary = json.load(open("Custom_Dictionary/data.json"))

def return_meaning(word):
    if word in data_dictionary:
        return data_dictionary[word]
    elif len(difflib.get_close_matches(word, data_dictionary.keys())) > 0:
        return "Did you mean "+difflib.get_close_matches(word, data_dictionary.keys())[0]
    else:
        return "Word was not found, try another word"

user_input = input("Enter a word: ")
print(return_meaning(user_input.lower()))
