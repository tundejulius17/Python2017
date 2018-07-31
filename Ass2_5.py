wordset = set()
text = input('Enter some texts: ')
for word in text.split():
    wordset.add(word)
print(wordset)