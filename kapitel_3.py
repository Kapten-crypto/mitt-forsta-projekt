# Skapa en lista
bilar = ['volvo', 'tesla', 'bmw', 'audi']

# Skriv ut hela listan
print("Här är min lista:", bilar)

# Komma åt specifika element (Kom ihåg: 0 är först!)
print(f"Den första bilen i listan är: {bilar[0].title()}")
print(f"Den sista bilen i listan är: {bilar[-1].title()}")

# Ändra, lägg till och ta bort
bilar[0] = 'porsche' # Ändrar volvo till porsche
bilar.append('toyota') # Lägger till sist
bilar.insert(1, 'ferrari') # Lägger till på plats 2 (index 1)
del bilar[2] # Tar bort tesla

print("Uppdaterad lista:", bilar)
