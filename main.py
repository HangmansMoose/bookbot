
def sort_on(dict):
    return dict["num"]

def print_letters(list):
    for dic in list:
        print(f"The {dic['char']} character was found {dic['num']} times")
        #print(dic)

def get_total_words(book):
    total_words = 0
    #for line in book:
    words = book.split()
    total_words += len(words)

    print(total_words)

def letter_occurance(book):
    #create the dictionary with all letter values set to 0
    letters = {'a' : 0 , 'b': 0, 'c': 0, 'd' : 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    words = book.split()
    
    for word in words:
        lower_word = word.lower()

        for letter in range(0, len(lower_word)):
            #print([lower_word[letter]])
            key = lower_word[letter]
            if key not in letters:
                continue
            letters[key] += 1

    letters_list = []
    for key in letters:
        temp_dict = {"char" : key, "num" : letters[key]}
        print(temp_dict)
        letters_list.append(temp_dict)

    letters_list.sort(reverse=True, key=sort_on)
        
    print_letters(letters_list)


    
    



def main():
  
    with open('books/frankenstein.txt') as file:
        book = file.read()
        get_total_words(book)
        letter_occurance(book)



if __name__ == '__main__':
    main()
