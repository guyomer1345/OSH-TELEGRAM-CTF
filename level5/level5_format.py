flag = "REAL_FLAG"
fake_flag = "START SOLVING STOP PLAYING"

guessed = [" "]
wrong = []

tries = 7

while tries > 0:

    out = ""
    for letter in fake_flag:
        if letter in guessed:
            out = out + letter
        else:
            out = out + "_"

    if out == fake_flag:
        break

    print("Guess the flag:", out)
    print(tries, "chances left")

    guess = input()

    if guess in guessed or guess in wrong:
        print("Already guessed", guess)
    elif guess in fake_flag:
        print("Yay")
        guessed.append(guess)
    else:
        print("Nope")
        tries = tries - 1
        wrong.append(guess)

    print()

if tries:
    print("You guessed correctly!! : ", fake_flag)
else:
    print("You didn't get", fake_flag)