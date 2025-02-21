print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Run away.")
    print("4. Try to pet the bear.")
    print("5. Try to reason with the bear.")
    print("6. Try to reason with the bear and pet it.")
    print("7. Try to reason with the bear and take the cake.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs")
    elif bear == "3":
        print("You run away and the bear chases you down and eats you.")
    elif bear == "4":
        print("The bear mauls you.")
    elif bear == "5":
        print("The bear speaks philosophy and you die of boredom.")
    elif bear == "6":
        print("The bear speaks on the finer points of quantum physics then mauls you for trying to pet it.")
    elif bear =="7":
        print("While the bear is busy speaking on the teachings of Plato, you take the cake and run away.")
    else:
        print(f"The bear is confused watching you do {bear} and decides to maul you.")

elif door == "2":
    print("You enter a large room with some goblins. They stare at you in suprise, then grab their spears.")
    print("What do you do?")
    print("1. Throw a rock.")
    print("2. Run away.")
    print("3. Shout at them.")
    print("4. Run at them and grab the closest's spear.")

    goblin = input("> ")

    if goblin == "1" or goblin == "2":
        print("The goblins laugh at you and throw the rock back.")
        print("You get hit in the head and die.")
    elif goblin == "3":
        print("The goblins are startled, then stick you like a pig.")
        print("You die.")
    elif goblin == "4":
        print("You grab the spear and the goblins are impressed.")
        print("They give you a choice of weapons to duel with.")
        print("1. Sword")
        print("2. Axe")
        print("3. Bow")
        
        weapon = input("> ")

        if weapon == "1":
            print("You grab the sword and the goblins give you a shield.")
            print("You fight valiantly but are outnumbered.")
            print("You die.")
        elif weapon == "2":
            print("You grab the axe and the goblins give you a shield.")
            print("You strike many down but are outnumbered.")
            print("You die.")
        elif weapon == "3":
            print("You grab the bow and the goblins give you a quiver of arrows.")
            print("You shoot many goblins but are outnumbered.")
            print("You die.")
        else:
            print("The goblins are confused. They Kill you.")
    else:
        print("The goblins are confused. They Kill you.")
else:
    print("You stumble around and fall on a knife and die.  Good job!")