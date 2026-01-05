def get_book_text(path_to_book):
    with open(path_to_book) as book:
        book_contents = book.read()
    return book_contents

def words_in_book(path_to_book):
    book_text = get_book_text(path_to_book)
    book_words = book_text.split()
    words_in_book = len(book_words)
    return f"Found {words_in_book} total words"

def characters_in_book(path_to_book):
    character_dict = {}
    book_text = get_book_text(path_to_book)
    book_text = book_text.lower()
    for character in book_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sorted_characters_in_book(path_to_book):
    sorted_list = []
    character_dict = characters_in_book(path_to_book)
    for each in character_dict:
        new_dict = {}
        new_dict["char"] = each
        new_dict["num"] = character_dict[each]
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
