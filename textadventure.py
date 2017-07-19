start = '''
You wake up one morning and go running because you have been feeling really lonely lately.
Half way through your journey you stop in front of a red light and all of a sudden...
the cutest thing pops up. But there's a bike speeding towards it! Do you jump in front of the bike to save it?
'''


print(start)
hi = "Wrong answer. Please try again."

print("Type 'yes' to jump in front or 'no' to not jump .")
user_input = input()
if user_input == "yes":
    print("You now have a new pet and you no longer feel lonely. Now it's time to take it   home to wash up. Do you go left or right?") # finished the story by writing what happens
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        print("Oh look you have a dog!")
        import time
        time.sleep(3)
        print("Your dog just pooped!")
        time.sleep(1)
        print("Pick it up or get fined?")
        print("Type'pick up' to pick it up or 'fined'to get a fine.")
        user_input = input()
        if user_input == 'pick up':
                print("You find $100 under your dog's poop!")
        elif user_input == 'fined':
                print("You go broke HA!")
        else:
            print(hi)
    elif user_input == "right":
        print("Oh look you have a cat!")
        import time
        time.sleep(3)
        print("Your cat has just clawed at someone's face!")
        import time
        time.sleep(1)
        print("Do you wish to abandon your cat or stay with it?")
        print("Type 'abandon' to abandon your cat or 'stay' to stay by your cat's side.")
        user_input = input()
        if user_input == 'abandon':
            print("The people in the neighborhood all saw you run away from you cat and now they will ignore you.")
        elif user_input == 'stay':
            print("Your neighbor sues you but you win the case and you end up becoming really close friends!")
        else:
            print(hi)
    else:
        print(hi)


elif user_input == "no":
    print("YOU'RE A HORRIBLE PERSON AND WILL FOREVER BE LONELY!") # finished the story writing what happens
else:
    print(hi)
