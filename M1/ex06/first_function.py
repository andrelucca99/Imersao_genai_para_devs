import sys

def greeting(name: str) -> None:
  print("Hello", name)

def main():
  if len(sys.argv) != 2 or not sys.argv[1]:
    print("Error: insira um valor!")
  else:
    greeting(sys.argv[1])

if __name__ == "__main__":
  main()