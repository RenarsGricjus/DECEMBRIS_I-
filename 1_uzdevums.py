def skaitisana(cipars):
    for i in range(1, cipars + 1):
        print(i)

# Get user input for the target number
try:
    cipars = int(input("Ievadiet skaitli: "))
    skaitisana(cipars)
except ValueError:
    print("Ievadiet derīgu skaitli!")