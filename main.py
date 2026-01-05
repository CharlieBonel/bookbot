from stats import words_in_book, characters_in_book, sort_on, sorted_characters_in_book
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_book = sys.argv[1]
#words_in_book()
#characters_in_book()
character_list = sorted_characters_in_book(path_to_book)
alpha_list = ""
for each in character_list:
    #new_dict = {}
    if each["char"].isalpha() == True:
        alpha_list += f"{each["char"]}: {each["num"]}\n"


report_string = f"""
============ BOOKBOT ============
Analyzing book found at {path_to_book}...
----------- Word Count ----------
{words_in_book(path_to_book)}
--------- Character Count -------
{alpha_list}
============= END ===============
"""
print (report_string)