name = input("Hey, type your name: ")
print("Hello", name, "Welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
# play = should_we_play == "yes"

if should_we_play == 'y' or should_we_play == "yes":
    print("We are going to play a game!")

    direction = input("Do you want to go left or right? ").lower()
    if direction == "left":
        print("We went left and fell off a cliff, gameover!")
    elif direction == "right":
        print("We went right!")
        choice = input("Okay, you now see a bridge, do you want to swim under it or go over it? (swim/cross)").lower()
        if  choice == "swim":
            print("You swam under the bridge and got eaten by a crocodile, gameover!")
        else :
            print("You crossed the bridge and found a treasure chest!")
            treasure = input("Do you want to open it? (yes/no)").lower()
            if treasure == "yes":
                print("You found a pile of gold coins, you win!")
            else:
                print("You left the treasure behind, gameover!")  
    else:
        print("You can't go that way, you died!")
else:
    print("Okay, bye!")