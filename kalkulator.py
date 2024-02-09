# Funkcja dodawania
def dodawanie(a, b):
    return a + b

# Funkcja odejmowania
def odejmowanie(a, b):
    return a - b

# Funkcja mnożenia
def mnożenie(a, b):
    return a * b

# Funkcja dzielenia
def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    else:
        return a / b

# Funkcja główna
def main():
    print("Prosty kalkulator")

    # Wprowadzenie danych
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    operacja = input("Podaj operację (+, -, *, /): ")
    liczba2 = float(input("Podaj drugą liczbę: "))

    # Wybór operacji
    if operacja == '+':
        wynik = dodawanie(liczba1, liczba2)
    elif operacja == '-':
        wynik = odejmowanie(liczba1, liczba2)
    elif operacja == '*':
        wynik = mnożenie(liczba1, liczba2)
    elif operacja == '/':
        wynik = dzielenie(liczba1, liczba2)
    else:
        wynik = "Nieprawidłowa operacja!"

    # Wyświetlenie wyniku
    print("Wynik:", wynik)

if __name__ == "__main__":
    main()
