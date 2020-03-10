def count_words(file_name):
    word_dict = {}
    with open(file_name) as the_file:
        for word in the_file.read().split():
            if word.upper() != word:
                word = word.lower()
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


def auto_complete_suggestions(word, word_dict):
    suggestions = []

    for key in word_dict:
        if word in key:
            suggestions.append([key, word_dict[key]])

    suggestions.sort(key=lambda x: x[1], reverse=True)

    return suggestions


word_dict = count_words('hamlet_pruned.txt')
word = input('What would you like to auto-complete? ')
while word != 'exeunt':
    print(auto_complete_suggestions(word, word_dict))
    word = input('What would you like to auto-complete? ')
