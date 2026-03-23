words = ["apple","banana","kiwi","grape","melon","pear"]
# {
#     5: ["apple","grape","melon"],
#     6: ["banana"],
#     4: ["kiwi","pear"]
# }
def group_words_by_length(words: list) -> dict:
    '''

    :param words: list of words
    :return: dict { <length>: [list of words with that length] }
    '''
    dict_words = {}
    for word in words:
        length = len(word)
        if length not in dict_words:
            dict_words[length] = []
        dict_words[length].append(word)
    print(dict_words)
    return dict_words

group_words_by_length(words)