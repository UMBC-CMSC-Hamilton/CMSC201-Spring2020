def anagram_buggy(first_word, second_word):
    first_word = first_word.lower()
    second_word = second_word.upper()
    first_word_dict = {}
    second_word_dict = {}
    for letter in first_word:
        if letter in first_word_dict:
            first_word_dict[letter] += 1
    for letter in second_word_dict:
        if letter in second_word_dict:
            second_word_dict[letter] += 1

    for letter in first_word_dict:
        if first_word_dict[letter] != second_word_dict[letter]:
            return False

    return True
