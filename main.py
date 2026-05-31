print("Hello! I am AI Bot. What's your name? ")
name = input()
print(f"Nice to meet you, {name}!")

while True:
    print("\nHow are you feeling today? (good/bad/quit) : ")
    mood = input().lower()

    if mood == "quit":
        break 

    elif mood == "good":
        print("I'm glad to hear that!")
        g = input("Wanna play a game? Yes/No: ")

        if g.lower() == "yes":
            print("Okay! Let's Play.")
            c = input("That was fun! Wanna continue chatting? Yes/No: ")

            if c.lower() == "no":
                print("Okay!")
                break
            else:
                o = input("Want me to count to 100? Yes/No: ")
                if o.lower() == "yes":
                    for i in range(1, 101):
                        print(i)
                else:
                    print(":)")
                continue 

        else:
            print("Okay. No worries!")
            continue

    elif mood == "bad":
        print("I'm sorry to hear that. Hope things get better soon.")
        m = input("Wanna talk? Yes/No: ")

        if m.lower() == "yes":
            print("Go ahead!")
            t = input()
            print("Hmm. I hear you.")
        else:
            print("Okay, sometimes it's hard to put feelings into words.")

        continue 

    else:
        print("I see. Sometimes it's hard to put feelings into words.")
        continue

print(f"\nIt was nice chatting with you, {name}. Goodbye!")