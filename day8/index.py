import string
from art import logo
print(logo)
alphabet = list(string.ascii_lowercase)
length_alp = len(alphabet)
def encode(message: str, shift: int):
  encoded = ""
  for char in message:
    if char in alphabet:
      position = alphabet.index(char)
      new_index = position + shift
      if new_index > length_alp:
        new_index -= position
      encoded += alphabet[new_index]
    else:
      encoded += char
  return encoded


# this is not perfect, but it works (sometimes)
def decode(message: str, shift: int):
  decoded = ""
  for char in message:
    if char in alphabet:
      position = alphabet.index(char)
      new_index = position - shift
      if new_index <= 0:
        new_index += position
      decoded += alphabet[new_index]
    else:
      decoded += char      
  return decoded

operation = input("Would you like to encode or decode a message?\n")

if operation not in ["encode", "decode"]:
  print("Not a valid operation.")
  exit(1)
message = input(f"Message to {operation}: ")
shift = int(input("Type the shift number: "))
shift %= 26
match operation:
  case "encode":
    message = encode(message, shift)
    print(f"The encoded message: {message}")
    exit(0)
  case "decode":
    message = decode(message, shift)
    print(f"The decoded message: {message}")
    exit(0)
  case _:
    print("Not a valid operation.")
    exit(1)