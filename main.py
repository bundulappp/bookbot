def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = open_text(path_to_file)
    words_counter = show_number_of_words(file_contents)
    character_counter = count_characters(file_contents)
    list_of_dictionaries = convert_dict_to_list(character_counter)
    list_of_dictionaries.sort(reverse=True,key=sort_on)
    print_a_report(list_of_dictionaries)
    
def open_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def show_number_of_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    chars_map = dict()
    words = file_contents.split()
    for word in words:
        for char in word:
            if(char.isalpha()):
                char = char.lower()
                if(char in chars_map):
                    chars_map[char]+=1
                else:
                    chars_map[char]=1
    return chars_map

def convert_dict_to_list(dict):
    result=[]
    for key, value in dict.items():
        new_item = {'char': key, 'num': value }
        result.append(new_item)
    return result

def sort_on(dict):
    return dict["num"]

def print_a_report(list_of_dict):
    for item in list_of_dict:
        print(f"The '{item['char']}' character was found {item['num']} times")
main()