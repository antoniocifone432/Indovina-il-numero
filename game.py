import random

def main():
    print("🎮 Benvenuto a Indovina il Numero!")
    print("Sto pensando a un numero tra 1 e 100...")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Inserisci il tuo numero: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Troppo basso!")
            elif guess > secret_number:
                print("📈 Troppo alto!")
            else:
                print(f"🎉 Bravo! Hai indovinato in {attempts} tentativi.")
                break
        except ValueError:
            print("❌ Inserisci un numero valido.")

if __name__ == "__main__":
    main()
