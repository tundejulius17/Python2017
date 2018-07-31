text = input('Enter some text: ')

splitted_text = text.split()
word_dict={}
for part in splitted_text:

    if part not in word_dict:
        word_dict.update({part:1})
    else:
        word_dict.update({part:word_dict.get(part) + 1})

for key in word_dict.keys():
    print(key + ':' + str(word_dict.get(key)))

print(word_dict)



