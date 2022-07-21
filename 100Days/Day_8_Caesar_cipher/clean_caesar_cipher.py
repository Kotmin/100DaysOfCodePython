#repl.it file to remove in clear python version / to swap to something like "cls" or "clear"
from replit import clear

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text,shift_amount,cipher_direction):
  result=""
  
  if not(cipher_direction=="encode" or cipher_direction=="decode"):
    print("That's not a valid direction. You can parse only 'encode' or 'decode'")
    return result
  if cipher_direction=="decode":
    shift_amount*=(-1)
    
  for i in start_text:
    if i not in alphabet:
      result+=i
      continue
    new_index = (alphabet.index(i) + shift_amount ) % len(alphabet)
    result+=alphabet[new_index]

  return result

is_running = True

clear()

print(logo+'\n')


while is_running:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  message = caesar(text,shift,direction)
  
  print(f"There is your message: \n {message}")
  continuation = input("Type 'yes' if you want to go again. Otherwise type 'no'")

  clear()
  
  if continuation.lower().strip() =="no":
    is_running=False
    print("Vale")