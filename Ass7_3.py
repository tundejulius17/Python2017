
def search_indexes(str, word, index=0):
    index=str.find(word, index)
    if index>=0:
        print(index)
        search_indexes(str, word, len(word)+index)
search_indexes("live and let live","live")