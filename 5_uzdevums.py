import time
def sveiki():
    tagad = int(time.strftime("%H"))

    if 5 <= tagad < 12: 
        return "Labrīt!"
    elif 12 <= tagad  <18:
        return "Labdien!"
    else:
        return "Labvakar!"
a = sveiki()
print(a)