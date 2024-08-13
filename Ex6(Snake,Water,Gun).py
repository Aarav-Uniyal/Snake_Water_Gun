import random

game = ["S","W","G"]
Computer = random.choice(game)


print ("Welcome to Snake, Water and Gun game!!! ")
def gameplay(F):
    c = 0
    d = 0
    i = 0
    while True:
        i = i + 1
        b = input("Enter S for Snake, W for Water and G for Gun.\n")
        b = b.capitalize()

        if  Computer == "S" and b == "W":
            d = d + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == "S" and b == "G":
            c = c + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == "W" and b == "G":
            d = d + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == "W" and b == "S":
            c = c + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == "G" and b == "S":
            d = d + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == "G" and b == "W":
            c = c + 1
            print(f"Your score - {c}. CPU's score - {d}.")

        elif Computer == b:
            print (f"This one was a tie. Your score - {c}. CPU's score - {d}.")

        if i == 10:
            if c > d:
                print ("You win!!!")
                break

            elif c < d:
                print ("CPU wins.")
                break

            elif c == d:
                print ("Scores are same. Match tied.")
                break
            else:
                print ("Please enter a valid input. Run the program again to play.\n")
                break


if __name__ == '__main__':
    gameplay(Computer)
