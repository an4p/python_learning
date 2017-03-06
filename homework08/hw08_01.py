import my_file_functions

f = "file_read.txt"
count1 = my_file_functions.word_count(f, "beautiful")
count2 = my_file_functions.symbol_count(f, "u")
count3 = my_file_functions.first_letter_counter(f, "u")
count4 = my_file_functions.letter_in_words_counter(f, "w")
print(count1, count2, count3, count4)