import sys

def main():
  if len(sys.argv) != 2 or not sys.argv[1]:
    print("Error: insira um valor!")
  else:
    print(sys.argv[1])

if __name__ == "__main__":
  main()