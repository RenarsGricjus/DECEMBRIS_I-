def rekinasana(cipars):
    if cipars < 0:
        return "Nederīgs skaitlis"
    else:
        rezultats = 1
        for i in range(2, cipars + 1):
            rezultats *= i
        return rezultats

a = int(input("Ievadiet skaitli: "))
faktoriala_rez = rekinasana(a)

print(f"Faktoriāls skaitlim {a} ir: {faktoriala_rez}")
