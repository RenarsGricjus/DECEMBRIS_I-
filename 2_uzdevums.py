def skaitlis(robeza):
    cipars = 1
    while cipars ** 2 <= 1000:
        cipars += 1

    return cipars
robeza = 1000

rezultats = skaitlis(robeza)
print (f"Pirmais skaitlis kura kvadrāts ir lielāks par 1000 ir: {rezultats}")