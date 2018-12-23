
def main():
    word = input("Skriv inn ditt hemmelige ord: ")
    antall_liv = int(input("Velg antall liv: "))
    guess_word = "*" * len(word)

    while antall_liv > 0 and guess_word.find("*") > -1:
        guess = input("Gjett en bokstav: ")
        if guess in word:
            print("{} ligger i det hemmelige ordet".format(guess))
            for i in range(len(word)):
                if guess == word[i]:
                    s = list(guess_word)
                    s[i] = guess
                    guess_word = "".join(s)
        else:
            print("Beklager, {} er ikke i det hemmelige ordet".format(guess))
            antall_liv -= 1

        print("Ditt ord er nå {} og du har {} liv igjen".format(guess_word, antall_liv))

    if guess_word.find("*") < 0:
        print("Gratulerer! Du vant")
    else:
        print("Beklager, ingen liv igjen")

main()
