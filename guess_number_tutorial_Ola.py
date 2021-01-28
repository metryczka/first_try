import random

def start():
    a = input("Będziemy losować liczbę od 1 do....")


    if a.isnumeric():
        b=int(a)
        guess_number(b)
    else:
        print("Nie wprowadziłeś liczby! Spróbuj jeszcze raz!")
        start()


def guess_number(x):
    guess_computer = random.randint(1, x)
    guess = 0

    while guess_computer != guess:
        guess_num = input(f"Podaj liczbę od 1 do {x}: ")
        if guess_num.isnumeric():
            guess=int(guess_num)

            if guess > guess_computer and guess < x:
                print("Twoja liczba jest zbyt wysoka, spróbuj jeszcze raz!")
            elif guess > x:
                print("Towoja liczba jest spoza zakresu")
            elif guess < guess_computer:
                print("Twoja liczba jest zbyt niska, spróbuj jeszcze raz!")
        else:
            print("Nie wprowadziłeś liczby!")
            guess=0
    print(f"Gratulacje, udało ci się zgadnąć, wylosowałem liczbę {guess_computer}")

start()
