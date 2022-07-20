import random



from hangman_art import stages, logo
from hangman_words import word_list


# word_list = ["aardvark","baboon","camel"]

our_word = random.choice(word_list)

chars = []
chars[:0]=our_word

game_is_pending=True


player_lives = 6



def ret_userchoice(guess):
  blank=""
  for i in range(0,len(guess)-1):
    blank+="_ "
  blank+="_"
  return blank

def in_word(guess,word):
  if guess in word:
    return True
  return False

def draw_on_board(guess,word,game_board):
  for i in range(0,len(word)):
    if guess == word[i]:
      game_board[i] = guess
  return game_board
      
      
      
  
  
# For debugging purposes
print(our_word)
print(logo)

#We can add something like press any button to start

game_board = chars.copy()

print(game_board)

for i in range(0,len(game_board)):
  game_board[i]="_"


print(game_board)
print("\n")




while game_is_pending:
  if '_' not in game_board:
    print("Congrats you won.")
    game_is_pending = False
    continue
  # else:
  #   clear()
  #print list as string
  print(f"{' '.join(game_board):^25}")
  print(f"{stages[player_lives]:^50}")
  
  user_guess = input("Take your guess: ").lower().strip()

  if user_guess in game_board:
    print(f"Hey you have already guessed, '{user_guess} letter' !")
  
  game_board = draw_on_board(user_guess,chars,game_board)

  if not in_word(user_guess,our_word):
    player_lives -=1
    print(f"{user_guess} is not in our word")
    if player_lives == 0:
      game_is_pending = False
      print(stages[player_lives])
      print("You have lost")
    
  