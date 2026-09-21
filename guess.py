import random
import cowsay

low, high = 1,10
liczba = random.randint(low, high)
próba = 1

print(f"Pomyślałem o liczbie między {low} a {high}. Zgadnij jaka to liczba.")

while True:
    while True:
        try:
            strzał = int(input())
            break
        except ValueError:
            print("Musisz podać liczbę")

    animal_fun = random.choice(list(cowsay.char_funcs.values()))

    if liczba == strzał:
        animal_fun(f'Zgadłeś w próbie nr {próba}. Super!')
        break
    else:
        animal_fun(f"Próba nr {próba}: Celuj {'wyżej' if liczba > strzał else 'niżej'}!")
        próba+=1

