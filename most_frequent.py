import operator
if __name__ == '__main__':
    test_string = 'Missisippi'
    string_dict = dict()
    for letter in test_string:
        if letter not in string_dict:
            string_dict[letter] = test_string.count(letter)
    ordered_answer = sorted(string_dict.items(), key=operator.itemgetter(1), reverse=True)
    print (ordered_answer)
