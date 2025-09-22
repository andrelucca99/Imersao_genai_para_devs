import sys
import cowsay

def greeting():
    message = "Hello, " + sys.argv[1]
    cowsay.cow(message)

def main():
  if len(sys.argv) != 2 or not sys.argv[1]:
    print("Error: insira um valor!")
  else:
    greeting()

if __name__ == "__main__":
  greeting()