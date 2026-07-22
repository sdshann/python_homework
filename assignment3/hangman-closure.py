def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)
        show_word = [letter if letter in guesses else '_' for letter in secret_word]
        print(''.join(show_word))
        return True if '_' not in show_word else False
        
    return hangman_closure
        
secret_word = input("What is your secret word? ")
guess_letter = make_hangman(secret_word)
while True:
    one_letter = input("Next guess? ")
    word_is_complete = guess_letter(one_letter)
    if word_is_complete:
        break
