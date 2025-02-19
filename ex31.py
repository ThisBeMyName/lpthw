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