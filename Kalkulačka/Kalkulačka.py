
# Tahle funkce sečte dvě čísla.
def add(x, y):
    return x + y

# Tahle funkce odečte dvě čísla.
def subtract(x, y):
    return x - y

# Tahle funkce vynásobí dvě čísla.
def multiply(x, y):
    return x * y

# Tahle funkce vydělí dvě čísla.
def divide(x, y):
    return x / y


print("Vyberte početní operaci:")
print("1.Sčítání")
print("2.Odčítání")
print("3.Násobení")
print("4.Dělení")

while True:
    # Zjistí, jakou početní operaci chce uživatel použít.
    choice = input("Napište číslo(1/2/3/4): ")

    # Zkontroluje, zda-li uživatel napsal číslo od 1 do 4. Pokud je to jiné číslo, kalkulačka se vypne.
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Zadejte první číslo: "))
        num2 = float(input("Zadejte druhé číslo: "))
        # Pokud uživatel odeslal číslo 1, program si vyžádá dvě čísla, která následně sečte.
        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))
        # Pokud uživatel odeslal číslo 2, program si vyžádá dvě čísla, která následně odečte.
        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))
        # Pokud uživatel odeslal číslo 3, program si vyžádá dvě čísla, která následně vynásobí.
        elif choice == "3":
            print(num1, "*", num2, "=", multiply(num1, num2))
        # Pokud uživatel odeslal číslo 4, program si vyžádá dvě čísla, která následně vydělí.
        elif choice == "4":
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Zjistí, jestli chce uživatel ještě něco vypočítat.
        # Pokud je odpověď ne, opakování se rozbije a kalkulačka se vypne.
        next_calculation = input("Chcete další výpočet? (ano/ne): ")
        if next_calculation == "ne":
          break
    
    else:
        print("Invalid Input")