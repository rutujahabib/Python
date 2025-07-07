import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#testing code
# print(f"psst, the solution is {chosen_word}.")


#create blanks
display = []
guessed_letters = [] 
for _  in range(word_length):
    display += "_"
# print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}. Try a different letter.")
        continue

    guessed_letters.append(guess)

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
           display[position] = letter

    if guess not in chosen_word:
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          lives -= 1
          print(hangman_art.stages[lives])
          if lives == 0:
            end_of_game = True
            print("You lose.")    
           
    print(f"{'  '.join(display)}")       

    if "_" not in display:
      end_of_game = True
      print("You win!")

   