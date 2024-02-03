def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero"

if __name__ == "__main__":
    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    choice = input("Wybierz operację (1, 2, 3, 4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(f"{num1} + {num2} = {dodawanie(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {odejmowanie(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {mnozenie(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {dzielenie(num1, num2)}")
    else:
        print("Nieprawidłowy wybór operacji")
