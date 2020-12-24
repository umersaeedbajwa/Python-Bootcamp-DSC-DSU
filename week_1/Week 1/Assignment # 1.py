

def string_diagonally(n):
    print(f"Name is: {n}")
    for i in range(len(n)):
        print(' '*i, n[i])
                   

def reverse_diagonally(n):
    for j in range(len(n)):
        leangth = len(n)
        print(' '*(leangth-j), n[j])

def main():
    name = input("Enter the name: ")
    string_diagonally(name)
    reverse_diagonally(name)


if __name__ == "__main__":
    main()
    
