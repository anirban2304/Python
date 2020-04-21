question_list = ("What", "When", "How", "Who")

def process_sentence(user_sentence):
    updated_sentence = user_sentence.title()
    if updated_sentence.startswith(question_list):
        updated_sentence = updated_sentence+"?"
    else:
        updated_sentence = updated_sentence + "."
    return updated_sentence

sentences = []

while True:
    user_input = input("Say something: ")
    if user_input == "end":
        break
    else:
        new_sentence = process_sentence(user_input)
        #print(new_sentence)
        sentences.append(new_sentence)

final_sentence = ""

for sentence in sentences:
    final_sentence = final_sentence+sentence+" "
print(final_sentence)