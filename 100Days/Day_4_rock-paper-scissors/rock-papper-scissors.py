# from random import randint # Would be better but online host have problem with random lib

# import random module
import random2

states=['r','p','s']
## This function answer does the first player win, first player == p1
def result(p1,p2):
  if p1 == p2:
    print("It's a draw!")
    return False
  if p1=='r' and p2=='s':
    return True
  if p1=='s' and p2=='p':
    return True
  if p1=='p' and p2=='r':
    return True
  return False

def print_graphic(shortcut):
  if shortcut=='r':
    print(rock)
    return
  if shortcut=='p':
    print(paper)
    return
  if shortcut=='s':
    print(scissors)
    return
    
  print('No no no not valid sign to print')
  
  
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# print(rock)

# print(random2.randint(0,1))


game_is_pending=True

# Game loop

while game_is_pending:
  #Placeholder for score
  
  player_choice = input('What do you choose? Type r for Rock, p for Papper or s for Scissors. \n > ')
  
  player_choice = player_choice.strip().lower()
  computer_choice = random2.choice(states)
  
  if not(player_choice in states):
    print("That's not a valid choice. Try again")
    # sleep(10)
    continue

  print("Your choice: \n")
  print_graphic(player_choice)

  print("Computer choice: \n")
  print_graphic(computer_choice)

  if result(player_choice,computer_choice):
    print("You won, congrats")
  else:
    print("You're looser!!!")
  
  