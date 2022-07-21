
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  encrypted = ""
  for i in text:
    new_index = (alphabet.index(i) + shift ) % len(alphabet)
    encrypted+=alphabet[new_index]
  return encrypted

def decrypt(text,shift):
  decrypted = ""
  for i in text:
    new_index = (alphabet.index(i) - shift ) % len(alphabet)
    decrypted+=alphabet[new_index]
  return decrypted


 # print(encrypt("hello",5))
#print(encrypt("civilization",5))

is_running = True

while is_running:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if direction.lower().strip() =="encode":
    message = encrypt(text,shift)
  if direction.lower().strip() =="decode":
    message = encrypt(text,shift)

  print(f"There is your message: \n {message}")
  continuation = input("Type 'yes' if you want to go again. Otherwise type 'no'")

  if continuation.lower().strip() =="no":
    is_running=False
    print("Vale")



