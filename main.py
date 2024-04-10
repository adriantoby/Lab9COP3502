from encode import encode
from encode import decode

def main():
  option = ""
  while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    option = input("Please enter an option: ")

    if option == "1":
      password = input("Please enter your password to encode: ")
      password = encode(password)
      print("Your password has been encoded and stored!\n")
    elif option == "2":
      decoded = decode(password)
      print(f"The encoded password is {password}, and the original password is {decoded}.\n")
    elif option == "3":
      break

if __name__ == "__main__":
  main()