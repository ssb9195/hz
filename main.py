def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error!"
    return x / y

print("Izvēlies operāciju:")
print("1 - Saskaitīšana")
print("2 - Atņemšana")
print("3 - Reizināt")
print("4 - Dališana")

choice = input("Ievadi numuru 1/2/3/4:")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Ieraksti pirmo skaitli:"))
    num2 = float(input("Ieraksti otro skaitli:"))

    if choice == '1':
        print("Rezultāts:", add(num1, num2))
    
    elif choice == '2':
        print("Rezultāts:", substract(num1, num2))
    
    elif choice == '3':
        print("Rezultāts:", multiply(num1, num2))
    
    elif choice == '4':
        print("Rezultāts:", divide(num1, num2))

else:
    print("Nederīga ievade. Lūdzu, atlasiet pareizo darbību.")