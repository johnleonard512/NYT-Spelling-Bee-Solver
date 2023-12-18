from itertools import product

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return {line.strip().lower() for line in file}

def is_in_dictionary(word, dictionary_words):
    return word.lower() in dictionary_words

def run_program(letter_list, must_have_element):
  ### MUST CHANGE PATHNAME TO WHEREEVER YOU SAVE WORDS_ALPHA.TXT 
    path = r'C:\Users\John Leonard\Desktop\words_alpha.txt'
    dictionary_words = load_dictionary(path)

    while True:
        print("Hit enter to generate wordlist (or type 'exit' to end): ")
        start_element = input()
        if start_element.lower() == 'exit':
            break

        print(f'All words with 4 or more letters containing "{must_have_element}" :')
        for word_length in range(4, len(letter_list) + 3):
            possible_letter_combos = product(letter_list, repeat=word_length)
            for perm in possible_letter_combos:
                generated_word = ''.join(perm)
                if generated_word.startswith(start_element) and must_have_element in generated_word:
                    if is_in_dictionary(generated_word, dictionary_words):
                        print(generated_word)

if __name__ == "__main__":
    print("-------------------------------")
    print("W E L C O M E  T O  J O H N ' S")
    print("    S P E L L I N G - B E E    ")
    print("          S O L V E R          ")
    print("-------------------------------")
    print(f"""
(Have fun!>    \\     /
           \\    o ^ o   /
            \\  (     ) /
  ____________(%%%%%%%)____________
 (     /   /  )%%%%%%%(  \\   \\     )
(___/___/__/           \\__\\___\\___)
    (     /  /(%%%%%%%)\  \\     )
     (__/___/ (%%%%%%%) \\___\\__)
             /(       )\\
           /   (%%%%%)   \\
                (%%%)
                  !
    """)

    def get_single_letter_input(prompt, used_letters):
        while True:
            user_input = input(prompt).lower()
            if len(user_input) == 1 and user_input.isalpha() and user_input not in used_letters:
                used_letters.add(user_input)
                return user_input
            else:
                print("Please enter a single, non-repeated letter.")

    print("Type a letter and hit enter:")
    used_letters = set()
    letter_list = [get_single_letter_input(f"{i + 1}: ", used_letters) for i in range(7)]

    print("\nEnter the center letter:")
    while True:
        must_have_element = input("> ")
        if must_have_element.lower() not in [letter.lower() for letter in letter_list]:
            print("Oops! That letter isn't in the puzzle! Enter another: ")
        else:
            break

    run_program(letter_list, must_have_element)
