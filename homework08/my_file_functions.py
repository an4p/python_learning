def word_count(file_name, word):
    '''
    (str, str) -> int

    Counts specified word in a file
    '''
    file = open(file_name)
    counter = 0
    for line in file:
        words = line.lower().split()
        for w in words:
            w = w.strip(".").strip(",").strip("!").strip("*").strip("-")
            if word.lower() == w:
                counter += 1
    file.close()
    return counter
#f = "file_read.txt"
#print(word_count(f, "one"))

def symbol_count(file_name, symbol):
    '''
    (str, str) -> int

    Counts specified symbol in the file
    '''
    file = open(file_name)
    counter = 0
    for line in file:
        for i in range(len(line)):
            if line[i] == symbol:
                counter +=1
    file.close()
    return counter

def first_letter_counter(file_name, letter):
    '''
    (str, str) -> int

    Counts how many words begin with specified letter
    '''
    file = open(file_name)
    counter = 0
    for line in file:
        words = line.lower().split()
        for w in words:
            if w[0].lower() == letter.lower():
                counter += 1
    file.close()
    return counter

def letter_in_words_counter(file_name, letter):
    '''
    (str, str) -> int

    Counts how many words contain specified symbol
    '''
    file = open(file_name)
    counter = 0
    for line in file:
        words = line.lower().split()
        for w in words:
            if w.count(letter):
                counter += 1
    file.close()
    return counter


